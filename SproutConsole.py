import socket

def __init__():
    #HOST, PORT = '', 5207
    RUN, HOST, PORT = True,'', 80
    sprout_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sprout_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sprout_socket.bind((HOST, PORT))
    sprout_socket.listen(1)
    with open('SproutConsole.html', 'r') as SproutConsoleHtmlFile:
        SproutConsoleHtml=SproutConsoleHtmlFile.read().replace('\n', '')
    print('Sprout Console served on port %s ...' % PORT)
    while (RUN == True):
        client_connection, client_address = sprout_socket.accept()
        request = client_connection.recv(1024)
        print(request)
        
        # Required header that tells the browser how to render the text.
        print("Content-Type: text/html\n\n")  # here text -- not html

        client_connection.sendall(str.encode(SproutConsoleHtml))
        client_connection.close()

__init__()
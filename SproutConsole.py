 def __init__():
        HOST, PORT = '', 5207

        sprout_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sprout_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sprout_socket.bind((HOST, PORT))
        sprout_socket.listen(1)
        print 'Sprout Console served on port %s ...' % PORT
        while True:
            client_connection, client_address = sprout_socket.accept()
            request = client_connection.recv(1024)
            print request
            
            # Required header that tells the browser how to render the text.
            print("Content-Type: text/html\n\n")  # here text -- not html

            page = ('''
                <!DOCTYPE html>
                <html lang = "en">
                
                <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300' rel='stylesheet' type='text/css'>
                <!---https://coolors.co/3d315b-444b6e-708b75-9ab87a-f8f991 COlors-->
                <style>
                body
                    {
                            background-color: #FFFFFF;
                            margin: 0px;
                    }

                    .header-bottom
                    {
                            width:100%;
                            position:fixed;
                            margin: auto;
                            height: 7%;
                            background-color: #004D40;
                            float:left;
                            top:93%;
                            font-family: 'Open Sans';
                            font-size: 10px;
                            padding-left:2%;
                    }

                    .header-side
                    {
                            width:15%;
                            position:fixed;
                            margin: auto;
                            height: 100%;
                            background-color:#26A69A;
                            float:left;
                    }

                    .header-config
                    {
                            width:25%;
                            position:fixed;
                            margin: auto;
                            height: 100%;
                            background-color: 
                            
                    }
                    a{text-decoration: none; color: black;}
                    .link
                    {
                            width: 100%;
                            height: 5%;
                            padding-top:10%;
                            padding-left: 25%;
                            font-family: Arial;
                            text-decoration: none;
                            font-size: 15px;
                            float: center;
                    }

                       .link-active
                    {
                            width: 100%;
                            height: 5%;
                            padding-top:10%;
                            padding-left: 25%;
                            font-family: Arial;
                            text-decoration: none;
                            font-size: 15px;
                            float: center;
                            background-color:white;
                    }

                    .link:hover
                    {
                            width: 80%;
                            height: 5%;
                            padding-top:10%;
                            padding-left: 25%;
                            font-family: Arial;
                            text-decoration: none;
                            font-size: 15px;
                            float: center;
                            background-color: white;
                    }

                    .logolink
                    {
                            width: 85%;
                            height: 10%;
                            padding-top:15%;
                            padding-left: 15%;
                            font-family: Arial;
                            text-decoration: none;
                            font-size: 25px;
                            float: center;
                    }


                    .logolink:hover
                    {
                            width: 85%;
                            height: 10%;
                            padding-top:15%;
                            padding-left: 15%;
                            font-family: Arial;
                            text-decoration: none;
                            font-size: 25px;
                            float: center;
                            background-color: #004D40;
                            
                    }

                    .management-block
                    {
                            left:17%;
                            float:center;
                            position: absolute;
                    }

                    .management-block
                    {
                            width: relative;
                            font-family: 'Open Sans',sans-serif ;
                            font-weight: 300;
                            padding: 3px 10px 10px 10px;
                            height: relative;
                            position: absolute;
                            float: center;
                            margin: auto;
                    }



                </style>
                <title> Sprout Console </title>
                </head>

                <body style = "margin:0px">

                        <div class = "main">
                        <nav class = "header-side">
                                
                                <a href ="">
                                <div class = "logolink">
                                <img src = "http://i.imgur.com/7XA8xpe.png" width = "75%"/>
                                </div></a>
                                
                                <a href ="">
                                <div class = "link-active" id = "console">
                                Console
                                </div></a>
                                
                                <a href ="">
                                <div class = "link" id = "nodes">
                                Nodes
                                </div></a>
                                
                                <a href ="">
                                <div class = "link" id = "state">
                                State
                                </div></a>
                                
                        </nav>
                        </div>
                        
                        <div class = "management">
                                <div class = "management-block">
                                        <h1> Welcome to Console </h1>
                                        <h5 style = "padding-left: 5%";> > Get Started by Adding a Node </h5>
                                        <h5 style = "padding-left: 5%";> > Then Configure it with SproutDSC </h5>
                                        <h5 style = "padding-left: 5%";> > Finally, Check the State of Your Newly Configured Node </h5>
                                        <h5 style = "padding-left: 5%";> > Example: Create a new file called foo.ps1 on a Windows System</h5>
                                        <pre align = "left">
                                        <code style = "font-size:15px">                                       
    Node("foo.foobar.com",[ #In SproutDSC, all configurations are stored in an array.
        File(
        name = "foo.ps1",
        content = "Get-Command",
        ensure = "present",
        path = "C:\\Users\\",
        )# , Needed to seperate configurations.
    ])
                                        </code>
                                        </pre>
                                                 
                                </div>
                        
                        
                                <div class = "management-block">
                                        
                                </div>
                        </div>
                                
                        <div class = "header-bottom">
                        <a href = ""><h1>+NEW</h1></a>
                        </div>
                </body>
                </html>

            ''')
    
            client_connection.sendall(page)
            client_connection.close()
    #__init__()
![Sprout Logo](http://i.imgur.com/7XA8xpe.png)</br><hr>
An accessible, extensible, and self-contained Configuration Management Framework for Linux and Windows.

### The DSL
Sprout uses Python functions and arrays to push in data and configure your machine.
Here is an example of a simple SproutConfig file: 
'''python
# Demo
Config([ #In SproutDSC configurations are an array.
    Directory(
        name = "Wow",
        ensure = "present",
        path = "C:\\Users\\Luke Brady\\Desktop\\"
        ),
    File(
        name = "helloworld.json",
        content = "{\n  hello = 'world'\n}",
        ensure = "present",
        path = "C:\\Users\\Luke Brady\\Desktop\\Wow",
        ),
    ])
'''

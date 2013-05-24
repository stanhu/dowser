Dowser is a CherryPy application that displays sparklines of Python object
counts, and allows you to trace their referents. This helps you track memory
usage and leaks in any Python program, but especially CherryPy sites.

This is a fork of dowser from:

http://www.aminus.net/wiki/Dowser

To use, you need to install some libraries on your system that the python
package PIL depends upon.  On Ubnutu:

```
sudo apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
```

The APT installations put the libraries under /usr/lib/x86_64-linux-gnu and
PIL will search for them in /usr/lib/.  Create symlinks for PIL
to see them.

```
# ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
```

Then, install PIL and cherrypy:

```
pip install PIL cherrypy
```

In your Python application, you just need to add:

```
import cherrypy
import dowser
cherrypy.config.update({'server.socket_port': 8088})
cherrypy.tree.mount(dowser.Root(), '/dowser')
cherrypy.engine.start()
```

This will start a browser on localhost:8088/dowser.

To only see entries that have more than 100 items, use the 'floor'
argument:

```
http://localhost:8088/dowser?floor=1000
```

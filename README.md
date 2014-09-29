torsocks
========

##a tool for connecting to Tor hidden services through Tor's SOCKS5 proxy.

This module provides a function `create_connection` which works similarly to the one built into the `socket` module, except that it handles all the SOCKS5 negotiation at the start. By default it tries to connect to Tor via `localhost:9050`, but you can change this if you have tor set up to listen at some different port. Also, it is written specifically only for connecting to hidden services through Tor, and not for connecting to any old address, although the changes necessary to implement that are trivial, so I probably will do that at some future time (though currently I don't need too so I won't.) To prove to yourself that it works, you should try running the test script in your terminal.

    ./test.py

or

    python3 test.py

This should print out the contents of The Hidden Wiki. To install this to your system, you should probably do this:

    sudo ./setup.py install

**Happy hacking!**

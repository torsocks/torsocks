#!/usr/bin/env python3
import torsocks

if __name__ == '__main__':
    hidden_wiki = torsocks.create_connection(('zqktlwi4fecvo6ri.onion', 80))
    hidden_wiki.sendall(b'GET /wiki/index.php/Main_Page HTTP/1.0\r\n\r\n')
    data = bytearray(200000)
    view = memoryview(data)
    bytes_read = 1
    i = 0
    while (bytes_read != 0) and (i < 200000):
        #This loop should terminate... *fingers crossed*
        bytes_read = hidden_wiki.recv_into(view[i:])
        i += bytes_read
        print(bytes_read)
    print(data.decode())

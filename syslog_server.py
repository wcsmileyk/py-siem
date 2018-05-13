#!/usr/bin/env python

"""
Tiny Syslog Server in Python.

This is a tiny syslog server that is able to receive UDP based syslog
entries on a specified port and save them to a file.
That's it... it does nothing else...
There are a few configuration parameters.
"""

import logging
import socketserver

LOG_FILE = 'youlogfile.log'
HOST, PORT = "0.0.0.0", 514


class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = bytes.decode(self.request[0].strip())
        socket = self.request[1]
        print( "%s : " % self.client_address[0], str(data))
        print(str(data))


if __name__ == "__main__":
    try:
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")

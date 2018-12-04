# from http.server import BaseHTTPRequestHandler, HTTPServer
# import socketserver

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# import urlparse
# import SocketServer
# import matplotlib.pyplot as plt
from PIL import Image
# from io import BytesIO
from cognitive_service import call_cv_api
import json
import base64
from io import BytesIO
import time
import os
from utils import *

"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        length = int(self.headers.getheader('content-length'))
        metadata = self.rfile.read(length)
        # datetime = time.strftime('%Y-%m-%d-%H-%M-%S')
        message = self.process_metadata(metadata)
            # metadata = json.loads(metadata)
        # if not os.path.exists('tmp'):
        #     os.mkdir('tmp')
        # with open(os.path.join('tmp', datetime), 'w') as f:
        #     json.dump(metadata, f)
        # message = self.process_metadata(metadata)
        # message = json.dumps({'message': 'hi'})
        self._set_headers()
        self.wfile.write(message)

    def process_metadata(self, metadata):
        # type = metadata["Type"]
        # data = metadata["data"]
        # if type == "imgs":
        #     data = base64.b64decode(data)
        #     # image = Image.open(BytesIO(data))
        #     # plt.imshow(image)
        #     # plt.show()
        #     message = json.dumps(call_cv_api(data))  # tags of image
        # else:
        #     message = "error"
        if metadata[:2] == '--':
            message = do_upload_image(metadata)
        else:
            metadata = json.loads(metadata)
            if metadata['type'] == 'select':
                message = do_selected_poetry(metadata)
            elif metadata['type'] == 'comment':
                message = do_comment(metadata)
            else:
                message = 'hi'
        return message

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')

    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run(port=8000)
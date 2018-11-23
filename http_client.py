from __future__ import print_function

import requests
import json
from io import BytesIO


class Client:
    def __init__(self, port=8000, url="http://localhost"):
        self.name = "test_client"
        self.port = port
        self.url = url

    def img2tag(self, img_path):
        # image = Image.open()
        # plt.imshow(image)
        with open(img_path, "rb") as f:
            form = {'Type': 'img',
                    'data': f.read()}
            form = json.dumps(form, encoding='utf-16')
            r = requests.post("{0}:{1}".format(self.url, self.port), data=form)
        tags = json.loads(r.text)
        return tags


if __name__ == '__main__':
    client = Client()
    print(client.img2tag("imgs/4.jpg"))
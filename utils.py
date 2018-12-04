# coding=utf-8
import time
import json
from requests_toolbelt import MultipartDecoder
from PIL import Image
from io import BytesIO
import os
import shutil


def generate_id():
    return int(time.time() * 1000)


def do_upload_image(raw_data):
    metadata = raw_data
    id = generate_id()
    bdry = metadata.split("\n")[0][2:]
    decoder = MultipartDecoder(metadata, 'multipart/form-data;boundary={}'.format(bdry))
    image = Image.open(BytesIO(decoder.parts[1].content))
    if not os.path.exists('raw_images'):
        os.mkdir('raw_images')
    image.save('raw_images/{}.jpg'.format(id))
    # Todo: pass image to backend to get poetry
    form = {'id': id,
            'poetry1': u"花开花落，云卷云舒",
            'poetry2': u"床前明月光，疑是地上霜",
            'poetry3': u"苟利国家生死以， 岂因祸福避趋之"}
    return json.dumps(form)


def do_selected_poetry(metadata):
    id = metadata['id']
    choice = metadata['choice']
    # Todo: pass image and selected poetry to get synthesis result

    if not os.path.exists('syn_images'):
        os.mkdir('syn_images')
    shutil.copy('raw_images/{}.jpg'.format(id), 'syn_images/{}_syn.jpg'.format(id))

    base_url = 'poeticimage.eastus.cloudapp.azure.com:8080'
    img_url = '{}/syn_images/{}_syn.jpg'.format(base_url, id)

    form = {'id': id,
            'url': img_url}
    return json.dumps(form)


def do_comment(metadata):
    # Todo: upload comments to database
    id = metadata['id']
    if not os.path.exists('comment'):
        os.mkdir('comment')
    with open('comment/{}.json'.format(id), 'w') as f:
        json.dump(metadata, f)
    import pprint
    pprint.pprint(metadata)
    return json.dumps(metadata)

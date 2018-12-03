from requests_toolbelt import MultipartDecoder


with open("tmp/2018-12-03-14-32-53", "r") as f:
    metadata = f.read()
    bdry = metadata.split("\n")[0][2:]
    decoder = MultipartDecoder(metadata, 'multipart/form-data;boundary={}'.format(bdry))
    image = Image.open(BytesIO(decoder.parts[1].content))
    image.save('test.jpg')
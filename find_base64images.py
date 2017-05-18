tree = html.fromstring(i.cnt_txt)

for sayac, image in enumerate(tree.xpath('//img[contains(@src, "data:image")]/@src')):

    image_type, image_content = image.split(',', 1)
    image_type = re.findall('data:image\/(\w+);base64', image_type)[0]

    _image_savename = "{}{}_{}.{}".format(_img_savepath, i.id, sayac, image_type)
    _image_linkname = "{}{}_{}.{}".format(_img_linkpath, i.id, sayac, image_type)

    i.cnt_txt = i.cnt_txt.replace(image, _image_linkname)

    with open(_image_savename, "wb") as f:
        f.write(image_content.decode('base64'))

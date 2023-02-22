import os

from PIL import Image

from khanshop.settings import MEDIA_ROOT


def make_sized_image(source, size_h, size_w):
    imgname = f'gallery/{source.pk:012}W{size_w:04}H{size_h:04}.jpg'
    imgurl = MEDIA_ROOT / imgname
    if not os.path.isfile(imgurl):
        create_sized_image(source, size_w, size_h, imgurl)
    return imgname


def create_sized_image(source, size_w, size_h, imgurl):
    img = Image.open(source.image)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    old_w, old_h = img.size
    new_w = size_w
    new_h = int(new_w * old_h / old_w)
    if size_h < new_h:
        new_h = size_h
        new_w = int(new_h * old_w / old_h)
    img = img.resize((new_w, new_h), Image.ANTIALIAS)
    img.save(imgurl)

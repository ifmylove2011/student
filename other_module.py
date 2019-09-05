#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('2.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((50,54))
im.save('21.jpg',"JPEG")
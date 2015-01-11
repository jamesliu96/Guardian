#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Guardian
# v1.0.0
# By James Liu (@jamesliu96)
#
# The MIT License (MIT)
#
# Copyright (c) 2015 James Liu <j@jamesliu.info>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""This app will definitely make the 'Guardian always asshole' happy"""

import sys

def main(args):
	from PIL import Image, ImageFilter
	from facepp import API, File

	ONEFACE_MODE = False
	AV_MODE = False

	print "Thanks for using Guardian by James Liu :)"
	with open("guardian.cfg") as f:
		exec(f.read())

	api = API(API_KEY, API_SECRET, SERVER)

	for filename in args[1:]:
		try:
			image = Image.open(filename).convert("RGB")
		except IOError:
			print """ERROR: File doesn't exist or filename not specified.
Usage:   
	python guardian.py [file ...]

Modifications can be made in guardian.cfg"""
			exit()

		size = image.size

		if MULTIFACE_MODE:
			detect_result = api.detection.detect(img = File(filename), mode = "normal")
		else:
			detect_result = api.detection.detect(img = File(filename), mode = "oneface")

		faces = detect_result[r'face']

		alw_perc = ALW / 100.

		if ONEFACE_MODE:
			specs = ()
			for i in range(0, len(faces)):
				center_perc = faces[i][r'position'][r'center'][r'y'] / 100.
				size_perc = faces[i][r'position'][r'height'] / 100. / 2.
				specs += (int((center_perc + size_perc + alw_perc) * size[1]), )
			spec = max(specs)
		else:
			center_perc = faces[0][r'position'][r'center'][r'y'] / 100.
			size_perc = faces[0][r'position'][r'height'] / 100. / 2.
			spec = int((center_perc + size_perc + alw_perc) * size[1])

		if AV_MODE:
			box = (0, spec, size[0], size[1])
			region = image.crop(box)
			region = region.filter(ImageFilter.BLUR)
			region = region.filter(ImageFilter.MinFilter(5))
			image.paste(region, box)
			image.show()
		else:
			box = (0, 0, size[0], spec)
			region = image.crop(box)
			region.show()

if __name__ == "__main__":
	main(sys.argv)

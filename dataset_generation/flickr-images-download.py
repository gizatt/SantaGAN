#!/usr/bin/env python

from flickrapi import FlickrAPI
import json
import urllib
import os

search_tag = "house"
save_folder = "downloaded_flickr_imagesets"
max_num_results = 200

# Complete save path prefix
save_prefix = os.path.join(save_folder, search_tag)

# Flickr parameters
flickr_api_file = "flickr_api_key.secret"
fuser = "gizatt"
with open(flickr_api_file, 'r') as f:
	fkey = f.readline().strip()
	fsecret = f.readline().strip()

print "Key: ", fkey
print "Secret: ", fsecret
flickr = FlickrAPI(fkey, fsecret, format='parsed-json')
extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
trees = flickr.photos.search(text=search_tag, per_page=max_num_results, extras=extras, sort="relevance")
photos = trees['photos']['photo']

if not os.path.exists(save_prefix):
	os.makedirs(save_prefix)

k = 0
for photo in photos:
	print photo
	if "url_c" in photo.keys():
		im_url = photo["url_c"]
	elif "url_m" in photo.keys():
		im_url = photo["url_m"]
	elif "url_o" in photo.keys():
		im_url = photo["url_o"]
	else:
		continue
	save_path = os.path.join(save_prefix, "%05d.jpg" % k)
	print "Downloading ", im_url, " to ", save_path
	urllib.urlretrieve (im_url, save_path)
	k += 1

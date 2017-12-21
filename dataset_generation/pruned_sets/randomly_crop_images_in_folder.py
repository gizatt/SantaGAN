# Based on code from http://code.activestate.com/lists/python-list/706954/

# Given a set of folders whose images we want to crawl and combine,
# crawls each image and takes some number of random square crops
# of it (at random size), and resizes to a fixed size.

import random, os, time
from PIL import Image

in_folders = [
  "positive_christmas/flickr_christmas_decorated_room",
  "positive_christmas/flickr_christmas_decorations_outdoors",
  "positive_christmas/flickr_christmas_presents",
  "positive_christmas/flickr_christmas_tree",
  "positive_christmas/google_christmas_decorations_indoors",
  "positive_christmas/google_christmas_decorations_outdoors",
  "positive_christmas/google_christmas_trees_indoors"
]
out_folder = "positive_christmas/square_all"
#in_folders = [
#  "negative_christmas/flickr_architecture",
#  "negative_christmas/flickr_city_streets",
#  "negative_christmas/flickr_house",
#  "negative_christmas/flickr_kitchen",
#  "negative_christmas/flickr_living_room",
#  "negative_christmas/flickr_tree",
#]
#out_folder = "negative_christmas/square_all"

dx = dy = 500
tilesPerImage = 1

if not os.path.exists(out_folder):
  os.makedirs(out_folder)

k = 0
for folder in in_folders:
    files = os.listdir(folder)
    for file in files:
        try:
            with Image.open(os.path.join(folder, file)) as im:
                w, h = im.size
                if (w > h):
                  resize_ratio = float(dy) / float(h)
                  w_new = int(w * resize_ratio)
                  h_new = dy
                else:
                  resize_ratio = float(dx) / float(w)
                  w_new = dx
                  h_new = int(h * resize_ratio)

                print "New size: (%d, %d) -> (%d, %d)" % (w, h, w_new, h_new)

                im_resized = im.resize((w_new, h_new)) #, Image.ANTIALIAS)
                for i in range(1, tilesPerImage+1):
                    if w_new > dx:
                      x = random.randint(0, w_new-dx-1)
                    else:
                      x = 0
                    if h_new > dy:
                      y = random.randint(0, h_new-dy-1)
                    else:
                      y = 0
                    print("Cropping {}: {},{} -> {},{}".format(file, x,y, x+dx, y+dy))
                    newname = "%05d.jpg" % k
                    im_resized.crop((x,y, x+dx, y+dy))\
                      .save(os.path.join(out_folder, newname))
                    k += 1
        except Exception as e:
            print "Exception caught: ", e


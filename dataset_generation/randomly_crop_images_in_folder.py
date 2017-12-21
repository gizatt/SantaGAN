# Based on code from http://code.activestate.com/lists/python-list/706954/

import random, os, time
from PIL import Image

in_folder = "data_in"
out_folder = "data_out"
os.system("mkdir -p " + out_folder)

dx = dy = 500
tilesPerImage = 10

folders = os.listdir(in_folder)
k = 0
for folder in folders:
    files = os.listdir(in_folder + "/" + folder + "/")
    for file in files:
       try:
           with Image.open(os.path.join(in_folder, folder, file)) as im:
             for i in range(1, tilesPerImage+1):
               w, h = im.size
               if w > dx and h > dy:
                   x = random.randint(0, w-dx-1)
                   y = random.randint(0, h-dy-1)
                   print("Cropping {}: {},{} -> {},{}".format(file, x,y, x+dx, y+dy))
                   newname = "%05d.jpg" % k
                   im.crop((x,y, x+dx, y+dy))\
                     .save(os.path.join(out_folder, newname))
                   k += 1
       except Exception as e:
           print "Exception caught: ", e


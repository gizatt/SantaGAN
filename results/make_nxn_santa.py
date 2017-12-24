# Given indices of a forward and back pass
# (plus info about what model to use),
# generates a 2-by-2 grid of them

import random, os, time
from PIL import Image

model_shorthand = {
  "all": "christmas_decoration_all_cyclegan",
  "indoors": "christmas_decorations_indoors_cyclegan",
  "outdoors": "christmas_decorations_outdoors_cyclegan",
}

N_wide = 6

in_model_forward = "all"
in_set_forward = "test"

in_index_forwards = random.sample(range(500), N_wide**2)

in_path_forwards = os.path.join(model_shorthand[in_model_forward], "%s_latest" % in_set_forward, "images")

path_output = "santa_%dx%d.png" % (N_wide, N_wide)

imgs = [os.path.join(in_path_forwards, "%05d_fake_B.png" % i) for i in in_index_forwards]

imgs_ims = [Image.open(im_path) for im_path in imgs]

side_length = imgs_ims[0].size[0]

# Tile then in Nx2 grid
new_im = Image.new('RGB', (side_length*N_wide, side_length*N_wide))
print new_im.size
# Top row: forward real then fake
for i in range(N_wide):
	for j in range(N_wide):
		new_im.paste(imgs_ims[i*N_wide+j], (side_length*i, side_length*j))

new_im.save(path_output)
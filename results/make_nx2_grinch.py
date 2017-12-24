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

#in_model_forwards = ["indoors", "indoors", "indoors"]
#in_set_forwards = ["test", "test", "test"]
#in_index_forwards = [7, 33, 18]

#in_model_forwards = ["indoors", "indoors", "indoors"]
#in_set_forwards = ["test", "test", "test"]
#in_index_forwards = [34, 66, 167]

#in_model_forwards = ["outdoors", "outdoors", "outdoors"]
#in_set_forwards = ["test", "test", "test"]
#in_index_forwards = [40, 82, 98]

N = 10
in_model_forwards = ["outdoors"]*N
in_set_forwards = ["test"]*N
in_index_forwards = random.sample(range(140), N)

N = len(in_model_forwards)

in_path_forwards = [
	os.path.join(model_shorthand[in_model_forwards[i]], "%s_latest" % in_set_forwards[i], "images") for i in range(N)
	] 

output_strings = ["%s_%s_%05d" % (in_model_forwards[i], in_set_forwards[i], in_index_forwards[i]) for i in range(N)]
path_output = "_and_".join(output_strings) + ".png"
if len(path_output) > 50:
	path_output = "%s_grinch_%dx2.png" % (in_model_forwards[0], N)

forward_origs = [os.path.join(in_path_forwards[i], "%05d_real_A.png" % in_index_forwards[i])  for i in range(N)]
forward_fakes = [os.path.join(in_path_forwards[i], "%05d_fake_B.png" % in_index_forwards[i]) for i in range(N)]

forward_orig_ims = [Image.open(forward_orig) for forward_orig in forward_origs]
forward_fake_ims = [Image.open(forward_fake) for forward_fake in forward_fakes]

side_length = forward_orig_ims[0].size[0]

# Tile then in Nx2 grid
new_im = Image.new('RGB', (side_length*N, side_length*2))
print new_im.size
# Top row: forward real then fake
for i in range(N):
	print i
	new_im.paste(forward_orig_ims[i], (side_length*(i), 0))
	new_im.paste(forward_fake_ims[i], (side_length*(i), side_length))

new_im.save(path_output)
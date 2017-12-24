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

in_model_forward = "all"
in_set_forward = "test"
in_index_forward = 87

in_model_backward = "all"
in_set_backward = "test"
in_index_backward = 9

in_path_forward = os.path.join(model_shorthand[in_model_forward], "%s_latest" % in_set_forward, "images")
in_path_backward = os.path.join(model_shorthand[in_model_backward], "%s_latest" % in_set_backward, "images")

path_output = "%s_%s_%05d_and_%s_%s_%05d.png" % (in_model_forward, in_set_forward, in_index_forward, in_model_backward, in_set_backward, in_index_backward)


forward_orig = os.path.join(in_path_forward, "%05d_real_A.png" % in_index_forward)
forward_fake = os.path.join(in_path_forward, "%05d_fake_B.png" % in_index_forward)

backward_orig = os.path.join(in_path_backward, "%05d_real_B.png" % in_index_backward)
backward_fake = os.path.join(in_path_backward, "%05d_fake_A.png" % in_index_backward)

forward_orig_im = Image.open(forward_orig)
forward_fake_im = Image.open(forward_fake)
backward_orig_im = Image.open(backward_orig)
backward_fake_im = Image.open(backward_fake)

side_length = forward_orig_im.size[0]

# Tile then in 2x2 grid
new_im = Image.new('RGB', (side_length*2, side_length*2))

# Top row: forward real then fake
new_im.paste(forward_orig_im, (0, 0))
new_im.paste(forward_fake_im, (side_length, 0))
# Bottom row: backward fake then real
new_im.paste(backward_fake_im, (0, side_length))
new_im.paste(backward_orig_im, (side_length, side_length))

new_im.save(path_output)
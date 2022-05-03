from PIL import Image as img
import numpy as np

ll = img.open(r"lemur.png")
ff = img.open(r"flag.png")

nl = np.array(ll)
nf = np.array(ff)
img.fromarray(nl^nf).show()
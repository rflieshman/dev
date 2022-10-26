import numpy as np 
import pandas as pd
import trimesh as tm
import scipy as sp
import sklearn as sk

from matplotlib import pyplot as plt
from clodsa.augmentors.augmentorFactory import createAugmentor
from clodsa.transformers.transformerFactory import transformerGenerator
from clodsa.techniques.techniqueFactory import createTechnique
import cv2


ar = np.random.rand(100)

print(ar)

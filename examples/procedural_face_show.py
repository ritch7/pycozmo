#!C:/Users/ich/anaconda3/envs/pycoz/python.exe

import pycozmo


# Render a 128x64 procedural face with default parameters.
face = pycozmo.procedural_face.ProceduralFace()
im = face.render()
im.show()

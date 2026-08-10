import cv2

window1 = 'Color Calibration'
window2 = 'Processing'
red = (0 , 0 , 255)
blue = (255 , 0 , 0)
green = (0 , 255 , 0)
camerID = 0
FontFace = cv2.FONT_HERSHEY_SIMPLEX
pre_time = 0
d = 5
sigmacolor = 1
sigmaspace = 1
GaussianSigma = 1
strGaussian = 'Gaussian Output ...'
strBilateral = 'Bilateral Output ...'
STR = 'Output ...'
FPS = []
fps = 0
dt = 1/35

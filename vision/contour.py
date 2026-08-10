import cv2
import numpy as np

def Aspect(w , h):
    if h>0:
        ratio = w / h
    else:
        ratio = 0
    return ratio

def Circularity(area , perimeter):
    if perimeter>0:
        ratio = 4 * np.pi * area / perimeter ** 2
        ratio = round(ratio , 2)
    else:
        ratio = 0
    return ratio

def Solidity(contour , area):
    if contour is not None:
        hull = cv2.convexHull(contour)
        AreaHull = cv2.contourArea(hull)
        if AreaHull != 0:
            ratio = area / AreaHull
            ratio = round(ratio , 2)
        else:
            ratio =0
    else:
        ratio = 0
    return ratio

def BoundingRect(mask):
    x , y , w , h = cv2.boundingRect(mask)
    return x , y , w , h

def Perimeter(contour):
    if contour is not None:
        P = cv2.arcLength(contour , True)
    else:
        P = 0.0 
    return int(P)

def Centroid(contour):
    if contour is not None:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        else:
            return None , None
    else:
        return None , None
    return cx , cy
    

def FindContours(mask):
    contours, hierarchy = cv2.findContours(mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    return contours

def ContourArea(contour):
    if contour is not None:
        area = cv2.contourArea(contour)
    else:
        area = None
    return area

def LargestContour(mask):
    contours = FindContours(mask)
    if len(contours) != 0:
        largest = max(contours , key= cv2.contourArea)
    else:
        largest = None 
    return largest

def DrawContour(frame , contour):
    if contour is not None:
        cv2.drawContours(frame , [contour] , -1 , (0 , 255 , 0) , 2)
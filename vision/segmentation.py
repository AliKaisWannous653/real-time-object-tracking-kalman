import cv2
import numpy as np
from vision.preprocessing import ProcessFrame

def nothing(x):
    pass

def init(window1 , window2 , camerID):
    CreateTrackBarColor(window1 , nothing)
    CreateTrackBarProcess(window2 , nothing)
    cap = cv2.VideoCapture(camerID)
    return cap

def CreateTrackBarColor(window , method):
    cv2.namedWindow(window)
    cv2.resizeWindow(window, 670, 230)

    cv2.createTrackbar('l_h' , window , 0 , 255 , method)
    cv2.createTrackbar('l_s' , window , 0 , 255 , method)
    cv2.createTrackbar('l_v' , window , 0 , 255 , method)
    cv2.createTrackbar('u_h' , window , 255 , 255 , method)
    cv2.createTrackbar('u_s' , window , 255 , 255 , method)
    cv2.createTrackbar('u_v' , window , 255 , 255 , method)

def CreateTrackBarProcess(window , method):
    cv2.namedWindow(window)
    cv2.resizeWindow(window, 670, 230)

    cv2.createTrackbar('KOpen' , window , 0 , 5 , method)
    cv2.createTrackbar('KClose' , window , 0 , 5 , method)
    cv2.createTrackbar('KGaussian' , window , 0 , 5 , method)
    cv2.createTrackbar('KBilateral' , window , 0 , 5 , method)
    cv2.createTrackbar('SigmaColor' , window , 0 , 20 , method)
    cv2.createTrackbar('SigmaSpace' , window , 0 , 20 , method)

def GetColorCalibration(window):
    l_h = cv2.getTrackbarPos('l_h' , window)
    l_s = cv2.getTrackbarPos('l_s' , window)
    l_v = cv2.getTrackbarPos('l_v' , window)

    u_h = cv2.getTrackbarPos('u_h' , window)
    u_s = cv2.getTrackbarPos('u_s' , window)
    u_v = cv2.getTrackbarPos('u_v' , window)

    lower = np.array([l_h , l_s , l_v])
    upper = np.array([u_h , u_s , u_v])
    return lower , upper

def GetProcessing(window):
    k_o = cv2.getTrackbarPos('KOpen' , window)
    k_c = cv2.getTrackbarPos('KClose' , window)
    k_g = cv2.getTrackbarPos('KGaussian' , window)
    k_b = cv2.getTrackbarPos('KBilateral' , window)
    s_c = cv2.getTrackbarPos('SigmaColor' , window)
    s_s = cv2.getTrackbarPos('SigmaSpace' , window)
    k_o = 2 * k_o + 1
    k_c = 2 * k_c + 1
    k_g = 2 * k_g + 1
    k_b = 2 * k_b + 1
    return k_o , k_c , k_g , k_b , s_c , s_s

def ProcessMask(mask , k_o , k_c):
    if k_o == 1 and k_c == 1:
        return mask
    else:
        if k_o != 1:
            mask = cv2.morphologyEx(mask , cv2.MORPH_OPEN , np.ones((k_o , k_o)))
        if k_c != 1:
            mask = cv2.morphologyEx(mask , cv2.MORPH_CLOSE , np.ones((k_c , k_c)))
        return mask


def DetectMask(frame , window1 , window2 , GaussianSigma , lower , upper):
    k_o , k_c , k_g , k_b , s_c , s_s = GetProcessing(window2)
    frame = ProcessFrame(frame , k_g , k_b , s_c , s_s , GaussianSigma)
    hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame , lower , upper)
    mask = ProcessMask(mask , k_o , k_c)
        
    return mask
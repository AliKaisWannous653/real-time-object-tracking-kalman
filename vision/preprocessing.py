import cv2

def GaussianFilter(frame , KernalSize , GaussianSigma):
    frame_G = cv2.GaussianBlur(frame , KernalSize , GaussianSigma)
    return frame_G

def MedianFilter(frame , MedianKernalSize):
    frame_M = cv2.medianBlur(frame , MedianKernalSize)
    return frame_M

def BilateralFilter(frame , d , sigmacolor , sigmaspace):
    frame_B = cv2.bilateralFilter(frame ,d , sigmacolor , sigmaspace )
    return frame_B

def ProcessFrame(frame , k_g , k_b , s_c , s_s , GaussianSigma):
    if  k_g == 1 and k_b == 1 :
        return frame
    else:
        if k_g != 1:
            frame = GaussianFilter(frame , (k_g , k_g) , GaussianSigma)
        if k_b != 1:
            frame = BilateralFilter(frame , k_b , s_c , s_s)
        return frame
    
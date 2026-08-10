import cv2
import numpy as np
import config
from utils.visualization import visualize , PlotCurves , Trajectory , PlotError
import utils.TIME
from vision.segmentation import init , DetectMask , GetColorCalibration
import matplotlib.pyplot as plt
import vision.contour
from tracker.KalmanTracker import KalmanFilter
import utils.STDNoises

cap = init(config.window1 , config.window2 , config.camerID)
utils.TIME.print_system_info(cap)
idx = 0
kf = KalmanFilter(
    dt=config.dt,
    x0=0,
    y0=0,
    P0=1000,
    q1=30.15,
    q2 = 20.45,
    r1= 2.01,
    r2 = 1.44
)

while True:
    ret , frame = cap.read()
    idx += 1
    config.fps = utils.TIME.fbsCal ()

    if ret:
        lower , upper = GetColorCalibration(config.window1)
        mask = DetectMask(frame , config.window1 , config.window2 , config.GaussianSigma , lower , upper)
        cnt = vision.contour.LargestContour(mask)
        prediction = kf.predict()
        config.predict_x.append(prediction[0 , 0])
        config.predict_y.append(prediction[1 , 0])
        if cnt is not None:
            cx , cy = vision.contour.Centroid(cnt)
            area = vision.contour.ContourArea(cnt)
            S = vision.contour.Solidity(cnt , area)
            P = vision.contour.Perimeter(cnt)
            C = vision.contour.Circularity(area , P)
            x , y , w , h = vision.contour.BoundingRect(cnt)
            measurement = np.array([[cx], [cy]], dtype=float)
            if not np.all(np.isfinite(measurement)):
                print("BAD MEASUREMENT:", measurement)
                break

            estimate = kf.update(measurement)

            config.estimates_x.append(float(estimate[0, 0]))
            config.estimates_y.append(float(estimate[1, 0]))

            config.CX.append(cx)
            config.CY.append(cy)
            vision.contour.DrawContour(frame , cnt)
        else:
            cx , cy = None , None
            estimate = prediction
            C = 0
            S = 0
            P = 0        
        visualize(frame , lower , upper , mask , idx , config.STR , (cx , cy) , S , C , estimate , prediction)
        
        if cv2.waitKey(1)& 0xff == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

# Comparing between estimated results and measurments 

PlotCurves()

utils.STDNoises.RMSE (config.estimates_x , config.estimates_y , config.CX , config.CY)

# Results of this Experience

config.VX , config.VY = utils.STDNoises.CalVelocity(config.CX , config.CY , config.dt , config.VX , config.VY)
config.delta_VX , config.delta_VY = utils.STDNoises.CalDeltaVelocity(config.VX , config.VY , config.delta_VX , config.delta_VY)

utils.STDNoises.DescribeResults(config.FPS , config.CX , config.CY , config.VX , config.VY , config.delta_VX , config.delta_VY)

Trajectory(config.CX , config.CY , config.estimates_x , config.estimates_y)


# --------------------------------------------------
# Measurement - Estimate Difference
# --------------------------------------------------
PlotError(config.CX , config.CY , config.estimates_x , config.estimates_y)
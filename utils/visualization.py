import cv2
import config
import numpy as np
import matplotlib.pyplot as plt

def visualize(frame , lower , upper , mask , i , STR , c , S , C , e , p):
    lower_str = 'lower = [' + str(lower[0]) + ',' + str(lower[1]) + ',' + str(lower[2]) + ']'
    upper_str = 'upper = [' + str(upper[0]) + ',' + str(upper[1]) + ',' + str(upper[2]) + ']'
    if c[0] is not None:
        frame = cv2.circle(frame , (int(c[0]) , int(c[1])) , 15 , (255 , 0 , 0) , -1)
    frame = cv2.circle(frame , (int(e[0 , 0]) , int(e[1 , 0])) , 10 , (0 , 255 , 0) , -1)
    frame = cv2.circle(frame , (int(p[0 , 0]) , int(p[1 , 0])) , 5 , (0 , 0 , 255) , -1)
    frame = cv2.putText(frame ,'Solidity: ' + str(S) , (20 , 60) , config.FontFace , 0.6 , config.red , 1)
    frame = cv2.putText(frame ,'Circularity: ' + str(C) , (400 , 60) , config.FontFace , 0.6 , config.red , 1)
    frame = cv2.putText(frame , lower_str , (400,20) , config.FontFace , 0.6 , config.red , 1)
    frame = cv2.putText(frame , upper_str , (20,20) , config.FontFace , 0.6 , config.red , 1)
    frame = cv2.putText(frame , 'FBS: ' + str(int(config.fps)) ,(290 , 20) , config.FontFace , 0.6, config.red , 1)
    frame = cv2.putText(frame , 'index:' + str(i)  ,(290 , 60) , config.FontFace , 0.6, config.blue , 1)
    cv2.imshow('mask' , mask)
    cv2.imshow(STR , frame)
    cv2.resizeWindow('mask', 670, 440)
    cv2.resizeWindow(STR, 670, 440)


def PlotCurves():
    plt.figure()
    plt.plot(config.FPS)
    plt.xlabel('frames')
    plt.ylabel('fps')
    plt.title('fps curve')
    plt.show()

    plt.figure(figsize = (7,7))
    plt.subplot(2,1,1)
    plt.plot(config.CX, label='Measured X')
    plt.plot(config.estimates_x, label='Kalman Estimate X' , linestyle='--')
    plt.plot(config.predict_x, label='Kalman Predict X' , linestyle='--')

    plt.ylabel('X position (pixels)')
    plt.title('X Position: Measurement vs Kalman')
    plt.legend()
    plt.grid()

    plt.subplot(2,1,2)

    plt.plot(config.CY, label='Measured Y')
    plt.plot(config.estimates_y, label='Kalman Estimate Y' , linestyle='--')
    plt.plot(config.predict_y, label='Kalman Predict X' , linestyle='-.')

    plt.xlabel('Frame')
    plt.ylabel('Y position (pixels)')
    plt.title('Y Position: Measurement vs Kalman')
    plt.legend()
    plt.grid()
    plt.show()

def Trajectory(CX , CY , estimates_x , estimates_y):
    plt.figure(figsize=(8, 6))

    plt.plot(
        CX,
        CY,
        label='Measured Centroid'
    )

    plt.plot(
        estimates_x,
        estimates_y,
        '--',
        label='Kalman Estimate'
    )

    # Starting point
    plt.scatter(
        CX[0],
        CY[0],
        marker='o',
        s=80,
        label='Start'
    )

    # Ending point
    plt.scatter(
        CX[-1],
        CY[-1],
        marker='x',
        s=100,
        label='End'
    )

    plt.xlabel('X position (pixels)')
    plt.ylabel('Y position (pixels)')
    plt.title('Centroid Trajectory: Measurement vs Kalman')

    plt.gca().invert_yaxis()
    plt.axis('equal')
    plt.grid()
    plt.legend()

    plt.show()

def PlotError(CX , CY , estimates_x , estimates_y):
    N = min(
        len(CX),
        len(CY),
        len(estimates_x),
        len(estimates_y)
    )

    measured_x = np.array(CX[:N], dtype=float)
    measured_y = np.array(CY[:N], dtype=float)

    estimated_x = np.array(estimates_x[:N], dtype=float)
    estimated_y = np.array(estimates_y[:N], dtype=float)

    error_x = measured_x - estimated_x
    error_y = measured_y - estimated_y
    error_total = np.sqrt(error_x ** 2 + error_y ** 2)
    
    frames = np.arange(N)

    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.plot(frames, error_x)

    plt.axhline(
        0,
        linestyle='--',
        linewidth=1
    )

    plt.ylabel('Error X (pixels)')
    plt.title('Measurement–Estimate Difference')
    plt.grid(True)


    plt.subplot(3, 1, 2)

    plt.plot(frames, error_y)

    plt.axhline(
        0,
        linestyle='--',
        linewidth=1
    )

    plt.ylabel('Error Y (pixels)')
    plt.grid(True)


    plt.subplot(3, 1, 3)

    plt.plot(frames, error_total)

    plt.ylabel('Position Difference (pixels)')
    plt.xlabel('Frame')

    plt.grid(True)

    plt.tight_layout()
    plt.show()
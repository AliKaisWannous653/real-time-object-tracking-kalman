import numpy as np

def CalVelocity(X , Y , dt , VX , VY):
    if len(X) == len(Y):
        for i in range(1,len(X)):
            vx = (X[i] - X[i-1]) / dt
            vy = (Y[i] - Y[i-1]) / dt
            VX.append(vx)
            VY.append(vy)
        return VX , VY
  
def CalDeltaVelocity(VX , VY , delta_VY , delta_VX):
    for i in range(1,len(VX)):
        Dvx = VX[i] - VX[i-1]
        Dvy = VY[i] - VY[i-1]
        delta_VX.append(Dvx)
        delta_VY.append(Dvy)
    return delta_VX , delta_VY

def DescribeResults(FPS , CX , CY , VX , VY , delta_VX , delta_VY):
    print(f'mean of FPS: {int(np.mean(FPS))}')
    print(f'STD of FPS: {np.std(FPS)}')

    print('-------------------------------')
    
    print(f'mean of CX: {int(np.mean(CX))}')
    print(f'STD of CX: {np.std(CX)}')

    print(f'mean of CY: {int(np.mean(CY))}')
    print(f'STD of CY: {np.std(CY)}')

    print('-------------------------------')

    print(f'mean of VX: {int(np.mean(VX))}')
    print(f'STD of VX: {np.std(VX)}')

    print(f'mean of VY: {int(np.mean(VY))}')
    print(f'STD of VY: {np.std(VY)}')

    print('-------------------------------')

    print(f'mean of delta_VX: {int(np.mean(delta_VX))}')
    print(f'STD of delta_VX: {np.std(delta_VX)}')

    print(f'mean of delta_VY: {int(np.mean(delta_VY))}')
    print(f'STD of delta_VY: {np.std(delta_VY)}')


def RMSE (x_predict , y_predict , x_real , y_real):
    rmse_x = 0
    rmse_y = 0
    for i in range(len(x_predict)):
        rmse_x += (x_predict[i] - x_real[i]) ** 2
        rmse_y += (y_predict[i] - y_real[i]) ** 2
    rmse_x = (rmse_x / len(x_predict)) ** 0.5
    rmse_y = (rmse_y / len(y_predict)) ** 0.5
    print(f'RMSE in X-axis is: {rmse_x}')
    print(f'RMSE in Y-axis is: {rmse_y}')   
import numpy as np

class KalmanFilter:
    def __init__(self , dt , x0 , y0 , P0 ,q1 ,q2 , r1 , r2):
        self.x = np.array([[x0] , [y0] , [0] , [0]] , dtype = float)
        self.F = np.array([[1 , 0 , dt , 0] , [0 , 1 , 0 , dt] , [0 , 0 , 1 , 0] , [0 , 0 , 0 , 1]] , dtype = float)
        self.H = np.array([[1 , 0 , 0 , 0] , [0 , 1 , 0 , 0]] , dtype = float)
        self.P = np.eye(4 , dtype = float) * P0
        self.Q = np.array([[(dt ** 4) * (q1 ** 2) / 4 , 0 , (dt ** 3) * (q1 ** 2) / 2 , 0] ,
                           [0 , (dt ** 4) * (q2 ** 2) / 2 , 0 , (dt ** 3) * (q2 ** 2) / 2] ,
                           [(dt ** 3) * (q1 ** 2) / 2 , 0 , (dt ** 2) * (q1 ** 2) , 0] ,
                           [0 , (dt ** 3) * (q2 ** 2) / 2 , 0 , (dt ** 2) * (q2 ** 2)]])
        self.R = np.diag(np.array([r1 **2 , r2 **2]))
    
    def predict(self):
        self.x = np.dot(self.F , self.x)
        self.P = np.dot(np.dot(self.F , self.P) , self.F.T) + self.Q
        return self.x.copy()
    
    def update(self , z):
        res = z - np.dot(self.H , self.x)
        S = np.dot(np.dot(self.H , self.P) , self.H.T) + self.R
        K = np.dot(np.dot(self.P , self.H.T) , np.linalg.inv(S))
        self.x = self.x + np.dot(K , res)
        self.P = np.dot(np.eye(4) - np.dot(K , self.H) , self.P)
        return self.x.copy()
    
    def GetPosition(self):
        return self.x[:2] 

    def GetVelocity(self):
        return self.x[2:] 
    
    def reset(self , x0 ,y0 , P0):
        self.x = np.array([[x0] , [y0] , [0] , [0]] , dtype = float)
        self.P = np.eye(4 , dtype = float) * P0


import cv2
import numpy as np

def grises(A):
    B = np.zeros((len(A),len(A[0])))
    for ren in range (0,len(A)):
        for col in range(0,len(A[0])):
            resultado = 0
            for i in range(0,len(A[0][0])):
                resultado += A[ren][col][i]
                resultado = int(res/len(A[0][0]))
                B[i][j] = resultado
    return B


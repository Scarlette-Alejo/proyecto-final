<<<<<<< HEAD
cala de grises
def escalagrises(A):
    B=np.zeros(len A[0],len A[1])
    for i in range (0,len(A)):
        for j in range (0,len(A[0])):
            suma = 0
            for k in range(0,len(A[0][0])):
                suma = A[i][j][k]
                suma = int(suma/len(A[0][0]))
                B[i][j]=suma
    return B
#convolucion sin padding
def sinpadding(A,B):
    C = np.zeros(len (A),len A[0]))
    for i in range (0, len(A)):
        for j in range(0,len A[0])):
        suma = 0
            for p in range (0, len (B)):
                for d in range(0,len(B[0])):
                suma +=A[i+p][j+d]*B[p][d]
                C[i][j]=suma
    return C
                                                                                                                                                                        #convolucion con padding
def conpadding(A):
    B = np.zeros((len(A)+2,len(a[0])+2))
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            B[i+1][j+1]=A[i][j]
    return B
                                                                                                                                                                        #funcion white black
                                                                                                                                                                        def whiteblack(A):
                                                                                                                                                                            B = np.zeros(len A[0],len A[1])
                                                                                                                                                                            for i range (0,len(A)):
                                                                                                                                                                                for j in range(0,len(A[0]):
                                                                                                                                                                                        if A[i][j] > 128:
                                                                                                                                                                                        B[i][j]=255
                                                                                                                                                                    
                                                                                                                                                                            return B
                                                                                                                                                                            F = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
                                                                                                                                                                            imagenx = cv2.imread("spider.jpg")
                                                                                                                                                                            imagenx = cv2.cvtColor(imagenx,cv2.COLOR_BGR2RGB)
                                                                                                                                                                            imagenx2 = escalagrises(imagenx)
                                                                                                                                                                            cv2.imwrite("imagengris.jpg", imagenx2)
                                                                                                                                                                            cv2.imshow("imagenx2",imagenx2)
    cv2.waitKey(0)

                                                                                                                                                                            impadding = conpadding(imagenx2)
                                                                                                                                                                            impadding = sinpadding(impadding, F)
                                                                                                                                                                            cv2.imwrite("padding.jpg", impadding)

                                                                                                                                                                            imsinpadding = sinpadding(imagenx2, F)
                                                                                                                                                                            cv2.imwrite("sinpad.jpg", imsinpadding)

                                                                                                                                                                            imgBW = whiteblack(imagenx2)
                                                                                                                                                                            cv2.imwrite("blancoNegro.jpg", imgBW)

                                                                                                                                                                            import cv2
                                                                                                                                                                            import numpy as np
                                                                                                                                                                        def escalagrises(imagen):
                                                                                                                                                                            imag=cv2.imread("spider.jpg")
    imageA=imagen.shape[0]
                                                                                                                                                                            imagH=imagen.shape[1]
                                                                                                                                                                            matriz=np.zeros((imagA,imagH),np.uint8)
                                                                                                                                                                            for i in range(imagenA):
                                                                                                                                                                                for j in range(imagenH):

            matriz[i,j]=(imag[i,j,2] + imag[i,j,1] + imag[i,j,0])/3
                                                                                                                                                                                                                                                                                                                                                            cv2.imwrite("imagengris.jpg",matriz)
                                                                                                                                                                                                                                                                                                                                                            escalagrises("spider.jpg")
=======
#funcion escala de grises
def escalagrises(A):
    B=np.zeros(len A[0],len A[1])
    for i in range (0,len(A)):
        for j in range (0,len(A[0])):
            suma = 0
            for k in range(0,len(A[0][0])):
                suma = A[i][j][k]
                suma = int(suma/len(A[0][0]))
                B[i][j]=suma
    return B
#convolucion sin padding
def sinpadding(A,B):
    C = np.zeros(len (A),len A[0]))
    for i in range (0, len(A)):
        for j in range(0,len A[0])):
            suma = 0
            for p in range (0, len (B)):
                for d in range(0,len(B[0])):
                    suma +=A[i+p][j+d]*B[p][d]
                    C[i][j]=suma
    return C
#convolucion con padding
def conpadding(A):
    B = np.zeros((len(A)+2,len(a[0])+2))
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            B[i+1][j+1]=A[i][j]
    return
#funcion white black
def whiteblack(A):
    B = np.zeros(len A[0],len A[1])
    for i range (0,len(A)):
        for j in range(0,len(A[0]):
                if A[i][j]>128:
                B[i][j]=255
    return B
    
F = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
imagenx = cv2.imread("spider.jpg")
imagenx = cv2.cvtColor(imagenx,cv2.COLOR_BGR2RGB)
imagenx2 = escalagrises(imagenx)
cv2.imwrite("imagengris.jpg", imagenx2)

impadding = conpadding(imagenx2)
impadding = sinpadding(impadding, F)
cv2.imwrite("padding.jpg", impadding)

imsinpadding = sinpadding(imagenx2, F)
cv2.imwrite("sinpad.jpg", imsinpadding)

imgBW = whiteblack(imagenx2)
cv2.imwrite("blancoNegro.jpg", imgBW)

import cv2
import numpy as np
def escalagrises(imagen):
    imag=cv2.imread("spider.jpg")
    imageA=imagen.shape[0]
    imagH=imagen.shape[1]
    matriz=np.zeros((imagA,imagH),np.uint8)
    for i in range(imagenA):
        for j in range(imagenH):
            matriz[i,j]=(imag[i,j,2] + imag[i,j,1] + imag[i,j,0])/3
    cv2.imwrite("imagengris.jpg",matriz)
escalagrises("spider.jpg")
>>>>>>> 300f1e6659ff302d238b4c77b87ab3a8b81a54cc

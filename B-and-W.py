def blanco_negro(B):
    B = np.zeros((len(A),len(A[0])))
    for ren in range(0,len(A)):
        for col in range(0,len(A[0])):
            if A[ren][col] < 128:
                B[ren][col] = 255
    return B


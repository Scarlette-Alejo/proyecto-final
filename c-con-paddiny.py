def con_padd (B):
    B = np.zeros((len(A))+2,len(A[0])+2))
    for ren in range(0,len(A)):
        for col in range(0,len(A[0])):
            B[ren+1][col+1] = A[ren][col]
    return B

def convolucion(A,B):
    C = np.zeros(len(B)-(len(A)-len(B)),len(B)-(len(A)-len(B)))
    n = 0
    for ren in range(len(C)):
        for col in range(len(C[0])):
            resultado = 0 
            for ren2 in range(len(B)):
                for col2 in range(len(B[0])):
                    resultado += A[ren+ren2][col+col2]*B[ren2][col2]
                    if resultado > 255:
                        resultado = 255
                        C[ren][col] = resultado
    return C 

A = [[1,2,3,4,5],
    [5,4,3,2,1],
    [6,7,8,9,10],
    [10,9,8,7,6],
    [10,20,30,40,50]]
for linie in A:
    print(linie)
for rand in range(len(A)):
    print(f'Suma elementelor din randul {rand + 1} este {sum(A[rand])}')
suma = [sum(x) for x in zip(*A)]
diag_princ = []
diag_sec = []
for i in range(len(A)):
    print(f'Suma elementelor din coloana {i + 1} este {suma[i]}')
    for j in range(len(A[0])):
        if i == j:
            diag_princ.append(A[i][j])
        if i + j == len(A) - 1:
            diag_sec.append(A[i][j])
print(f'Diagonala principala {diag_princ}')
print(f'Diagonala secundara {diag_sec}')
n=int(input())
mat,diag,nondiag=[],[],[]
for i in range(0,n):
    col=list(input().split())
    mat.append(col)
for i in range(0,n):
    for j in range(0,n):
        if(i==j or i+j==n-1):
            if mat[i][j] not in diag:
                diag.append(mat[i][j])
        else:
            if mat[i][j] not in nondiag:
                nondiag.append(mat[i][j])
if(len(diag)==1 and len(nondiag)==1):
    print("yes")
else:
    print("no")

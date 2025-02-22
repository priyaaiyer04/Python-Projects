import sys
def transpose(matrix):
    if len(matrix[0])>len(matrix):
        for i in range(len(matrix[0])-len(matrix)):
            matrix.append([])
        for i in matrix:
            if len(i)==0:
                for j in range(len(matrix[0])):
                    i.append(sys.maxsize)
    
    elif len(matrix[0])<len(matrix):
        x=len(matrix[0])
        for i in matrix:
            j=0
            while j<(len(matrix)-x):
                i.append(sys.maxsize)
                j+=1
    l=[]             
    for j in range(len(matrix)):            
        for i in range(len(matrix[0])):
                x=str(i)+str(j)
                y=x[::-1]
                if l.count(x)==0 or l.count(y)==0:
                    l.append(x)
                    l.append(y)
                    if matrix[i][j]:
                        t=matrix[i][j]
                        matrix[i][j]=matrix[j][i]
                        matrix[j][i]=t
                
    for i in matrix:
        if i.count(sys.maxsize)==len(matrix[0]):
            matrix.remove(i)
    
    for i in matrix:
        x=i.count(sys.maxsize)
        for j in range(x):
            i.remove(sys.maxsize)
            
m=[[1,2,3,10],[4,5,6,11],[7,8,9,12]]
print(transpose(m))
print(m)
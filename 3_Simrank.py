import numpy as np

path=str(input("input file name,with .txt:"))
def File_max(path):
    A=list()
    fp = open(path, "r")
    for line in iter(fp):
        line1=line.strip().split(",")
        for i in range(len(line1)):
            if int(line1[i]) not in A:
                A.append( int(line1[i]) )      
    fp.close()
    return max(A)

def FiletoAD(path):
    size=File_max(path)
    A=np.zeros((size,size))
    fp = open(path, "r")
    for line in iter(fp):
        line1=line.strip().split(",")
        A[int(line1[0])-1][int(line1[1])-1]=1
    fp.close()
    return A


def simrank(C=0.5):
    Matrix=FiletoAD(path)
    Mt=Matrix.transpose()
    print(Mt)
    
    ind_vi=[]
    for i in Mt:
        ind_vi.append(sum(i))
    print((ind_vi))
    size=Matrix.shape[0]
    S=np.zeros((size,size))
    for i in range(size):
        S[i][i]=1
    
    for i in range(size):
        for j in range(size):
            if (i==j):
                break
            summation=0
            for index in range(len(ind_vi)):
                if ( (Mt[i][index]==1) and (Mt[j][index]==1) ):
                    summation+=1
            S[i][j]= round  ( C / (ind_vi[i]*ind_vi[j]) *summation  ,3 )
      
    for i in range(size):
        for j in range(size):
            if (j>i):
                S[i][j]=S[j][i]
    S=np.nan_to_num(S)
    print(S)
    return S
    
    
simrank()
    

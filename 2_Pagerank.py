import numpy as np
from scipy.sparse import csc_matrix
from scipy.linalg import norm


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

def pageRank(G, s = .85, maxerr = .05):

    n = G.shape[0]


    A = csc_matrix(G,dtype=np.float)
    rsums = np.array(A.sum(1))[:,0]
    print("rs",rsums)
    ri, ci = A.nonzero()
    A.data /= rsums[ri]
    print(A)


    sink = rsums==0

    ro, r = np.zeros(n), np.ones(n)
    interation=1

    while np.sum(np.abs(r-ro)) > maxerr:
        print(interation)
        print(np.sum(np.abs(r-ro)))
        ro = r.copy()

        for i in range(0,n):
            Ai = np.array(A[:,i].todense())[:,0]
            Di = sink / float(n)
            r[i] = ro.dot( Ai*s + Di*(1-s) )
        interation+=1
    return r/np.linalg.norm(r)




if __name__=='__main__':
    path=str(input("input file name,with .txt:"))
    G=FiletoAD(path)
    print(G)
    k= pageRank(G,s=.85)
    print('a',k)


        
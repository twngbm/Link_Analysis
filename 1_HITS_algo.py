import numpy as np
from scipy.linalg import norm
from scipy.sparse import csc_matrix
import matplotlib.pyplot as plt
adj_list_path=str(input("input file name,with .txt:"))

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
    

MM=FiletoAD(adj_list_path)
print(MM)
PhiMat = csc_matrix(MM)
print(PhiMat)
print(PhiMat.transpose())
hubs=[]
auths=[]
def HITS_coherence(MM):

    if (MM.sum()==0):
        return np.array([0])

    PhiMat = MM
    epsilon = 0.0001
    M, N = PhiMat.shape
    auth0 = np.ones([M, 1])
    hubs0 = np.ones([M, 1])
    print(auth0,"\n",hubs0)
   
    auth1=np.dot(PhiMat.transpose(), hubs0)
    hubs1=np.dot(PhiMat, auth1)
    hubs1 = (1.0/norm(hubs1, 2))*hubs1
    auth1 = (1.0/norm(auth1, 2))*auth1
    print ('a',auth1)
    print ('b',hubs1)
    iteration = 0

    while(   (norm (auth1-auth0, 2)+(norm(hubs1-hubs0, 2))) > epsilon):
        iteration += 1
        print('value%s:%.6f'%(iteration , norm (auth1-auth0, 2)+(norm(hubs1-hubs0, 2))))
        auth0 = auth1
        hubs0 = hubs1
        auth1=np.dot(PhiMat.transpose(), hubs0) 
        hubs1=np.dot(PhiMat, auth0 )

        hubs1 = hubs1/np.linalg.norm(hubs1)
        auth1 = auth1/np.linalg.norm(auth1)

        hubs.append(hubs1[1][0])
        auths.append(auth1[1][0])
        print("iter%s"%iteration)
        print ('hub:',hubs1.transpose())
        print ('auth1:',auth1.transpose())
        print('--')


k=HITS_coherence(MM)

plt.figure()
plt.figure(figsize=[6,6])
plt.title("Hubs & Auths\n")
plt.plot(hubs,'-ro',label='hubs of vetext1')
plt.plot(auths,'-go',label='auths of vetext1')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()



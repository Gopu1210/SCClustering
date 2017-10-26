import pandas as pd
import numpy as np
import random
import math

def eucledian_dist(a,b):
    ans = float(np.sqrt(np.sum((a-b)**2)))
    return ans

if __name__== '__main__':
    df = pd.read_csv('SPECTF_New.csv')
    df = df.sample(frac=1)
    #print df.head()
    df = df.as_matrix()
    print df.shape
    no_of_clusters = 2
    m = 2
    rows = random.sample(range(0,df.shape[0]),no_of_clusters)
    centers = []
    for i in range(no_of_clusters):
        centers.append(df[rows[i],:df.shape[1]-1])
    centers = np.array(centers,dtype=np.float)
    #print centers
    membership_matrix = np.zeros((df.shape[0],no_of_clusters),dtype=np.float)

    delta = 0.01
    itr=0
    flag=1

    while itr<500 and flag==1:
        print "--------------------------------------------------------------------------------------------"
        for i in range(membership_matrix.shape[0]):
            for j in range(membership_matrix.shape[1]):
                numerator = eucledian_dist(df[i,:44],centers[j,:])
                if numerator==0:
                    membership_matrix[i,j] = 1
                    for k in range(j):
                        membership_matrix[i,k] = 0
                    break
                else:
                    sumratios = 0
                    for k in range(centers.shape[0]):
                        dist = eucledian_dist(df[i,:44],centers[k,:])
                        if dist==0:
                            ratio = 0
                        else:
                            ratio = float(numerator)/dist
                        ratio = math.pow(ratio,2.0/(m-1))
                        sumratios += ratio
                    membership_matrix[i,j] = 1/float(sumratios)

        '''
        for i in range(membership_matrix.shape[0]):
            print np.sum(membership_matrix[i])
        '''
        #print centers
        flag=0
        for i in range(centers.shape[0]):
            numerator=np.zeros(44)
            denominator=0
            for j in range(df.shape[0]):
                #print df[j,:44].shape
                numerator = numerator + (df[j,:44] * math.pow(membership_matrix[j,i],m))
                denominator += math.pow(membership_matrix[j,i],m)
            if all(i<delta for i in centers[i]-(numerator/denominator)) is False:
                flag=1
            centers[i] = numerator/denominator
        itr+=1
        print membership_matrix
        print itr
        print "--------------------------------------------------------------------------------------------"

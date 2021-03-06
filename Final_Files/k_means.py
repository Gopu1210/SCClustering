import pandas as pd
import numpy as np
import math
import random

if __name__== '__main__':
    df = pd.read_csv('SPECTF_New.csv')
    #df = df.sample(frac=1)
    #print df.head()
    df = df.as_matrix()
    no_of_clusters = 2
    rows = random.sample(range(0,df.shape[0]),no_of_clusters)
    #rows = [30,80]
    centers = []
    for i in range(no_of_clusters):
        centers.append(df[rows[i],:df.shape[1]-1])
    centers = np.array(centers,dtype=np.float)
    clusters = np.zeros(no_of_clusters,dtype=np.object)

    print centers

    k=0
    flag=1

    while k<10 and flag==1:
        for i in range(clusters.shape[0]):
            clusters[i] = []

        for i in range(df.shape[0]):
            distances = []
            for j in range(no_of_clusters):
                a = df[i,:df.shape[1]-1]
                b = centers[j]
                distances.append(np.sqrt(np.sum((a-b)**2)))
            #print distances
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append((i,df[i,44]))
        flag=0
        for i in range(clusters.shape[0]):
            indices = clusters[i]
            arr = np.zeros(44,dtype=np.float)
            for j in range(len(indices)):
                arr = arr + df[(indices[j])[0],:df.shape[1]-1]
            arr = arr/len(indices)
            if np.array_equal(arr,centers[i]) is False:
                flag=1
            centers[i] = arr
        #print clusters.shape
        k+=1
        print "---------------------------------------------------------------------------------------------------------------"
        print centers
        print clusters
        print k

    # Finding Accuracy
    no_of_yes = np.zeros(no_of_clusters,dtype=int)
    no_of_no = np.zeros(no_of_clusters,dtype=int)

    for itr in range(clusters.shape[0]):
        yes_ct = 0
        no_ct = 0
        indices = clusters[itr]
        for itr2 in range(len(indices)):
            if((indices[itr2])[1] == "Yes"):
                yes_ct = yes_ct + 1
            else:
                no_ct = no_ct + 1
        no_of_yes[itr] = yes_ct
        no_of_no[itr] = no_ct

    print(no_of_yes)
    print(no_of_no)

    # If 1st cluster is Yes and 2nd cluster is No
    ac1 = (no_of_yes[0] + no_of_no[1])/float(df.shape[0])
    ac2 = (no_of_yes[1] + no_of_no[0])/float(df.shape[0])
    print max(ac1,ac2)



import numpy as np 
import operator

def Creatdataset():
    group=np.array([[1,101],[5,89],[108,5],[115,8]])
    labels=['Liebgeschichte','Liebgeschichte','Action','Action']
    return group,labels

def Classify(inx,dataSet,labels,K):
    dataSetSize=dataSet.shape[0]
    #shape 0返回的是行，1返回的是列，这里是确定里面有4个数据 每个数据有两个特征
    diffMat=np.tile(inx,(dataSetSize,1))-dataSet 
    Sqm=diffMat**2
    Sqm_distance=Sqm.sum(axis=1)
    #sum 0表示行相加，1表示列相加
    distance=Sqm_distance**0.5
    sortedDisIndex=distance.argsort()
    classout={}
    for i in range(K):
        votelabel=labels[sortedDisIndex[i]]
        classout[votelabel]=classout.get(votelabel,0)+1 
    sortedclassout=sorted(classout.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclassout[0][0]


if __name__ == "__main__":   
    group,labels=Creatdataset()
    test=[101,20]
    test_class=Classify(test,group,labels,3)
    print(test_class) 
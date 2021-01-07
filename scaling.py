import numpy as np
import copy
def scaling (data, a = 0, b = 1, columnIndices = 0, verbose = False) :

    """
    Scales data between a user specified range.
    
    Args:

    Returns:
    
    """

    dataScaled = copy.deepcopy(data)
    for i in range(len(columnIndices)) :
        minX = min(data.iloc[:, columnIndices[i]])
        maxX = max(data.iloc[:, columnIndices[i]])
        for j in range(len(data.iloc[:, columnIndices[i]])):
            div = (data.iloc[j, i] - minX)/(maxX-minX)
            dataScaled.iloc[j, i] = ((b[i]-a[i])*div)+a[i]

            if (verbose) :
                print('data.iloc      [', +j, ',', +i, '] = ', +data.iloc[j, i])
                print('dataScaled.iloc[', +j, ',', +i, '] = ', +dataScaled.iloc[j, i])
                print(" ")

        if (verbose) :        
            cor = np.corrcoef(dataScaled.iloc[:, columnIndices[i]], data.iloc[:, columnIndices[i]])
            print('Normalised covariance matrices of scaled vs original data (',+columnIndices[i],') = ')
            print(cor)
            
    return dataScaled


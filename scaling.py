import numpy as np
import copy

def scaling (data, a = [0], b = [1], columnIndices = [0], verbose = False) :

    """
    Scales data between a user specified range.
    
    Args:
        data (pandas dataframe, required): dataframe object to be scaled.
        a (list, optional): New minimum value to scale data to. If multiple columns are to be scaled,
                            list new minimum value for each column (that needs scaling) in order left to right.
                            For example, if column 0, 3 and 4 need scaling, and the new min for col 0 is -1,
                            new min for col 3 is 74 and new min for col 4 is 20, then a = [-1, 74, 20]. Defaults to [0].

        b (list, optional): New maximum value to scale data to. If multiple columns are to be scaled,
                            list new maximum value for each column (that needs scaling) in order left to right.
                            Example is same as arg (a), but listing new maximum rather than new minimum. Defaults to [1].

        columnIndices (list, optional): Indices of columns to be scaled. For example, if the data has 5 columns but only the
                                        first, fourth and fifth need scaling, then columnIndices = [0, 3, 4]. Defaults to [0].
                                        
        verbose (Boolean, optional): True prints original value and scaled value, and normalised covariance matrices of scaled vs original data. Defaults to False.

    Returns:
        `dataScaled`: 

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


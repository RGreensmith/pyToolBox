import numpy as np
def scaling (data, a = 0, b = 1, columnIndices = 0) :

    """
    Scales data between a user specified range.
    
    Args:

    Returns:

    """
    dataScaled = data
    for i in range(len(columnIndices)) :
        minX = min(data[:, columnIndices[i]])
        maxX = max(data[:, columnIndices[i]])
        for j in range(len(data[:,columnIndices])) :
            div = (data[j, i] - minX)/(maxX-minX)
            dataScaled[j, i] = ((b-a)*div)+a
        cor = np.corrcoeff(dataScaled[:, columnIndices[i]], data[:, columnIndices[i]])
        print('Correlation coefficient between original and scaled data (',+columnIndices[i],') = ',+cor)
    


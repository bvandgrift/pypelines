from statistics import mean, pstdev, pvariance


def aMean(data, dargs={}):
    return mean(data)


def aStDev(data, dargs={}):
    return pstdev(data)


def aVariance(data, dargs={}):
    return pvariance(data)

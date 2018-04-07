from statistics import mean, pstdev  # , pvariance
from scipy.signal import medfilt


def fList(data):
    return list(data)


def fPlusOne(data, dargs={}):
    return map(lambda x: x + 1, data)


def fSquare(data, dargs={}):
    return map(lambda x: x * x, data)


def fFillMissing(data, dargs={}):
    fill = dargs.get('fill') or mean(data)
    return map(lambda x: x or fill)


def fRemoveOutliers(data, dargs={}):
    drift = dargs.get('drift') or 1.25
    mu = mean(data)
    stdev = pstdev(data, mu)
    return filter(lambda x: abs(x - mu) < (stdev * drift))


def fDamp(data, dargs={}):
    scale = dargs.get('scale') or 2
    mu = mean(data)
    return map(lambda x: mu + (x - mu) / scale)


def fMedian3(data, dargs={}):
    return medfilt(data, 3)


def fMedianN(data, dargs={}):
    width = dargs.get('width') or 5
    return medfilt(data, width)

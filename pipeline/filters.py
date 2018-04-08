from statistics import mean, pstdev  # , pvariance
from scipy.signal import medfilt


def fPlusOne(frame):
    frame['data'] =  map(lambda x: x + 1, frame['data'])
    return frame


def fSquare(frame):
    frame['data'] = map(lambda x: x * x, frame['data'])
    return frame


def fFillMissing(frame):
    thinned = filter(lambda x: x, frame['data'])
    fill = frame['props'].get('fill') or mean(thinned)
    frame['data'] = map(lambda x: x or fill, frame['data'])
    return frame


def fRemoveOutliers(frame):
    drift = frame['props'].get('drift') or 2.0
    mu = mean(frame['data'])
    stdev = pstdev(frame['data'], mu)
    frame['data'] = filter(lambda x: abs(x - mu) < (stdev * drift), frame['data'])
    return frame


def fDamp(frame):
    scale = frame['props'].get('scale') or 2
    mu = mean(frame['data'])
    frame['data'] = map(lambda x: mu + (x - mu) / scale, frame['data'])
    return frame


def fMedian3(frame):
    data = list(map(lambda x: float(x), frame['data']))
    frame['data'] = medfilt(data, 3)
    return frame


def fMedianN(frame):
    width = frame.get('props').get('width') or 5
    frame['data'] =  medfilt(frame['data'], width)
    return frame


def fList(frame):
    frame['data'] = list(frame['data'])
    return frame

from statistics import mean, pstdev  # , pvariance
from scipy.signal import medfilt, savgol_filter
from scipy import ndimage

import numpy as np
import sys


def fPlusOne(frame):
    frame['data'] =  map(lambda x: x + 1, frame['data'])
    return frame


def fAddOffset(frame):
    offset = frame['props'].get('offset') or 0
    frame['data'] = map(lambda x: x + offset, frame['data'])
    return frame


def fSquare(frame):
    frame['data'] = map(lambda x: x * x, frame['data'])
    return frame

def fSmooth(frame):
    smoothing = frame['props'].get('smoothing') or 5
    # frame['data'] = savgol_filter(np.array(frame['data']), smoothing, (smoothing - 1))
    frame['data'] = ndimage.generic_filter(np.array(list(frame['data'])), np.nanmean, size=3, mode='constant', cval=np.NaN)
    return frame


def fFillMissing(frame):
    thinned = filter(lambda x: x, frame['data'])
    fill = frame['props'].get('fill') or mean(thinned)
    frame['data'] = map(lambda x: x or fill, frame['data'])
    return frame


def avgOutlier(val, mu, stdev, drift):
    if (abs(val - mu) < (stdev * drift)):
        return val
    sys.stdout.write('.')
    return mu


def fRemoveOutliers(frame):
    drift = frame['props'].get('drift') or 2.0
    data = list(map(lambda x: float(x), frame['data']))
    mu = mean(data)
    print(mu)
    stdev = pstdev(data, mu)

    frame['data'] = list(map(lambda x: avgOutlier(x, mu, stdev, drift), data))
    print(frame)

    return frame


def fDamp(frame):
    scale = frame['props'].get('dampness') or 2
    mu = mean(list(frame['data']))
    frame['data'] = list(map(lambda x: mu + (x - mu) / scale, frame['data']))
    return frame


def fMedian3(frame):
    data = list(map(lambda x: float(x), frame['data']))
    frame['data'] = medfilt(data, 3)
    return frame


def fMedianN(frame):
    kernel_size = frame.get('props').get('kernel_size') or 5
    data = list(map(lambda x: float(x), frame['data']))
    frame['data'] = medfilt(data, kernel_size)
    return frame


def fList(frame):
    frame['data'] = list(frame['data'])
    return frame

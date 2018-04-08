from statistics import mean, pstdev, pvariance


def aMean(frame):
    frame['summary'].update({'mean': mean(frame['data'])})
    return frame


def aStDev(frame):
    frame['summary'].update({'standardDeviation': pstdev(frame['data'])})
    return frame


def aVariance(frame):
    frame['summary'].update({'variance': pvariance(frame['data'])})
    return frame

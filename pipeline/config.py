

from pipeline import fPlusOne, fSquare, fList, fMedian3, fDamp, fRemoveOutliers, fFillMissing, fAddOffset
from pipeline import fMedianN, fSmooth
from pipeline import lCSV, lRawCSV, lJSON, lDebug
from pipeline import aMean, aStDev, aVariance


class PipelineConfig(dict):
    analyzers = [aMean, aStDev, aVariance]
    filters = [fSquare, fPlusOne, fList]
    loggers = [lCSV, lJSON]
    # ops = [lRawCSV, fFillMissing, fMedian3, fDamp, fAddOffset, fList, aMean, aStDev, aVariance, lCSV, lJSON]
    # ops = [fAddOffset, fRemoveOutliers, fMedianN, fDamp, fList, aMean, aStDev, aVariance, lCSV, lJSON]
    ops = [fAddOffset, fRemoveOutliers, fMedianN, fDamp, fMedianN, fSmooth, fList]

    # ops = [fList, aMean, lCSV, lJSON]
    properties = {
        'drift': 2.5,
        'kernel_size' : 9,
        'raw.csv':  'raw-new.csv',
        'out.csv':  'out-new.csv',
        'out.json': 'out-new.json',
        'offset': 15,
        'dampness': 3,
        'smoothing': 13
    }

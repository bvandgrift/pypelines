

from pipeline import fPlusOne, fSquare, fList, fMedian3, fDamp, fRemoveOutliers, fFillMissing
from pipeline import lCSV, lRawCSV, lJSON
from pipeline import aMean, aStDev, aVariance


class PipelineConfig(dict):
    analyzers = [aMean, aStDev, aVariance]
    filters = [fSquare, fPlusOne, fList]
    loggers = [lCSV, lJSON]
    # ops = [lRawCSV, fFillMissing, fMedian3, fDamp, fList, aMean, aStDev, aVariance, lCSV, lJSON]
    ops = [fDamp, fMedian3, fList, lCSV, lJSON]
    properties = {
        'drift': 2.5,
        'out.csv':  'out.csv',
        'out.json': 'out.json',
    }

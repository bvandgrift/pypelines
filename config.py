
from pipeline import fPlusOne, fSquare, fList, lCSV, lJSON


class config:
    filters = [fSquare, fPlusOne]
    loggers = [lCSV, lJSON]

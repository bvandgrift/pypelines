from toolz.functoolz import thread_last


class Pipeline:
    props = {}
    filters = []
    analyzers = []
    loggers = []
    ops = []

    def __init__(self, c={}):
        # check for local config
        from .config import PipelineConfig
        config = PipelineConfig()

        self.filters = config.filters
        self.analyzers = config.analyzers
        self.loggers = config.loggers
        self.props = config.properties
        self.ops = config.ops

    def process(self, data):
        frame = {'summary': {}, 'props':  self.props, 'data': data}

        # thread_last(frame, *self.filters)
        # thread_last(frame, *self.analyzers)
        # thread_last(frame, *self.loggers)
        thread_last(frame, *self.ops)
        return frame

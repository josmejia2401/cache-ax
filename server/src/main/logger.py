import logging


def getLogger(name, format=None, level=None):
    if not format:
        format = '%(name)s: %(message)s'
    if not level:
        level = logging.DEBUG
    logging.basicConfig(level=level, format=format, filename=name+'.log', force=True)
    logger = logging.getLogger(name)
    return logger

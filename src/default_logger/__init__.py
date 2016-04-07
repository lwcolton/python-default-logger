import logging

def get_default_logger(name, level=None):
    logger = logging.getLogger(name)
    logger.handlers = []
    if level is None:
        level = logging.INFO
    logger.setLevel(level)
    logger.propogate = False
    formatter =logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

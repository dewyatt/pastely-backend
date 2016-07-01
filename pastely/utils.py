import configparser

def get_config_ini(path):
    cfg = configparser.RawConfigParser()
    # No case folding
    cfg.optionxform = lambda opt: opt
    cfg.read(path)
    return cfg['pastely']

from toml import load,dump

def readToml(path):
    #ReadToml
    try:
        with open(path,"r") as arq:
            config = load(arq)
    except FileNotFoundError:
        config = {}
        return config

def exportToml(path,config):
    #ExportToml
    with open(path,"w") as arq:
        dump(config,arq)

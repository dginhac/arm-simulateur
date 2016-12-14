import time

_settings = {"PCbehavior": "+8",        # Can be "+0", "+8", "real"
             "PCspecialbehavior": True, # True or False, whether we want to turn on or off the +4 for PC
                                        # with special instructions (STR from PC and dataop with PC shifted by register)
             "runmaxit": 1000}          # Maximum number of non-stop iterations

def getSetting(name):
    return _settings[name]

def setSettings(settings):
    pass
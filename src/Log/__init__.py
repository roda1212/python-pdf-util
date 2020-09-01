import sys

def Info(val:str):
    sys.stdout.write(val)
    sys.stdout.flush()

def Error(val:str):
    sys.stderr.write('[Error] ' + val)
    sys.stderr.flush()

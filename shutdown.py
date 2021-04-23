import subprocess as sp
def shutdown():
    print("Shutting down system")
    sp.call("shutdown /s")
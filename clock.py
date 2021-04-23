import datetime
def tim():
    now = datetime.datetime.now()
    h=int(now.hour)
    m=int(now.minute)
    s=int(now.second)
    print(h,':',m,':',s)

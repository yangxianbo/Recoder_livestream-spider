import time,os

def scan_file(path,today,deleteday):
    _FILE_=[]
    path=path.rstrip('/')
    for  root,dirs,files in os.walk(path):
        for filename in files:
            filepath=os.path.join(root,filename)
            create_time=os.path.getctime(filepath)
            passday=int((today-create_time)/86400)
            if passday >= int(deleteday):
                _FILE_.append(os.path.join(root,filename))
    return _FILE_

today=time.time()
pathlist='/data/luzhi_new'
dlist=scan_file(pathlist,today,8)
for i in dlist:
    os.remove(i)


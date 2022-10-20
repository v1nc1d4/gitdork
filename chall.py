import os
import sys
import zipfile 
import shutil

sys.setrecursionlimit(2000)

def create_zip(wdir, name):
    zwdir = f"{wdir}/{name}"
    oldz = f"{int(name)+1}.zip"
    print(oldz)
    if oldz in os.listdir(wdir):
        shutil.move(f"{wdir}/{oldz}", zwdir)
    zipf = zipfile.ZipFile(f"{wdir}/{str(name)}.zip",
            'w', 
            zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(zwdir):
        for file in files:
            zipf.write(os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file),
                    os.path.join(zwdir, '..')))
    zipf.close()
    shutil.rmtree(zwdir)

def create_flag(wdir, nwdir, name):
    if not os.path.exists(f"{wdir}/{nwdir}/{name}/fl4g.txt"):
            with open(f"{wdir}/{nwdir}/{name}/fl4g.txt", 'w') as flag:
                flag.write("Flag here!")

def create_fd(wdir, nwdir, name, ln):
    name = str(f"{name:0{ln}d}")
    os.mkdir(f"{wdir}/{nwdir}/{name}")
    os.mknod(f"{wdir}/{nwdir}/{name}/{name}")
    if name == "1337":
        create_flag(wdir, nwdir, name)
    if int(name) == 1:
        create_zip(wdir, nwdir)
    else:
        return create_fd(wdir, nwdir, int(name) - 1, ln)

def main():
    mwdir = "working"
    for num in reversed(range(1, 1338)):
        os.mkdir(f"{mwdir}/{str(num)}")
        nwdir = str(num)
        create_fd(mwdir, nwdir, num, (len(str(num))))
                         
main()

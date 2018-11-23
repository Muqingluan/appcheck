import sys
import json
import zipfile

def parsershumeng(apkpath):
    apkarrary = []
    findapk = []
    with open(apkpath + '/savedata.json') as json_file:
        apkarrary = json.load(json_file)
    for i in apkarrary:
        print "check tongdun and apk name is " + i
        z = zipfile.ZipFile(i, 'r')
        for i in z.namelist():
            if i.find('libdu.so'):
                findapk.append(i)
                with open(apkpath + '/tongdunapk.json', 'w') as json_file:
                    json_file.write(json.dumps(findapk))
import sys
import json
import zipfile

def parsertongdun(apkpath):
    apkarrary = []
    findapk = []
    with open(apkpath + '/savedata.json') as json_file:
        apkarrary = json.load(json_file)
    print "apk count is %d" % len(apkarrary)
    for j in apkarrary:
        print "check tongdun and apk name is " + j
        try:
            z = zipfile.ZipFile(j, 'r')
            for i in z.namelist():
                if i.find('tongdun') != -1 or i.find('fm-core') != -1:
                    findapk.append(j)
                    with open(apkpath + '/tongdunapk.json', 'w') as json_file:
                        json_file.write(json.dumps(findapk))
        except:
            continue

    print "find tongdun app count is %d" % len(findapk)


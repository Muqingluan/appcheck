
import zipfile
import sys,os
import json

jiagu_magic = [
'libexecdll.so',
'libexecdllgame.so',
'ijm_lib',
'libexecmain.so',
'libjiagu.so',
'libjiagu_art.so',
'libsecpreload.so',
'meta-data',
'libbangcle_crypto_tool.so',
'libSecShell.so',
'nagain.data',
'libDexHelper.so',
'libhobi.so',
'libhobi.so',
'libshella',
'tencent_stub',
'libdemolish.so',
'libdemolish.so',
'ali',
'libbaiduprotect.so',
'libbaiduprotect.so',
'libkdp.so',
'libkdp.so',
'libCmbShield.so',
'libCmbShield.x86.so']


if __name__ == "__main__":
    apk = sys.argv[0]
    print "checkapk name is " + apk
    z = zipfile.ZipFile(apk, 'r')
    for i in z.namelist():
        for j in jiagu_magic:
            if i.find(i):
                print "yi jing jia gu!!"


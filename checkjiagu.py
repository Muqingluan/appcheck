
import zipfile
import sys,os
import json


jiagu_magic = [
'.appkey',
'libjiagu.so',
'libjiagu-x86.so',
'SecShell0.jar',
'libSecShell.so',
'classes0.jar',
'libDexHelper.so',
'libdexjni.so',
'dx-enc.data',
'dx-resp.data',
'libdxn.so',
'libjdi.so',
'libx3g-ind.so',
'libx3g-ld.so',
'libstee.so',
'libx3g.so',
'af.bin',
'ijiami.ajm',
'libexec.so',
'af.bin',
'libexec.so',
'libexecmain.so',
'classes.dex',
'libhdog.so',
'libvdog.so',
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
'libCmbShield.x86.so'
]

def checkjiagu(apkpath):
    z = zipfile.ZipFile(apkpath, 'r')
    for i in z.namelist():
        for j in jiagu_magic:
            if i.find(i):
                print "yi jing jia gu!!"



import sys
from yingyongbao import yingyongbaodownload
from checktongdun import parsertongdun

if __name__ == "__main__":

    print "-----ying yong bao downloading-----"
    print sys.path[0]
    savepath = sys.path[0] + "/yingyongbao/"
    yingyongbaodownload(savepath)

    print "-----start checking tongdun app -----"
    parsertongdun(savepath)

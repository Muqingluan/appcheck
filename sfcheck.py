# coding=utf-8

import urllib2
import sys,os
import BeautifulSoup

def sfcheck(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req).read()
    bobj= BeautifulSoup(response,"html.parser")




if __name__ == "__main__":

    print "-----ying yong bao downloading-----"
    url = "https://sf.taobao.com//json/get_search_court_list.htm?location_code=510122&category=50025969&st_param=1&auction_start_seg=0&auction_start_from=2018-06-01&auction_start_to=2018-06-01"
    sfcheck(url)
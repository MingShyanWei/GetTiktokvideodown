import requests as rq
from bs4 import BeautifulSoup
import os
import sys


x = "http://www.tiktokvideodown.com/vod-play-id-129190-sid-1-pid-{i}.html"

episodeSt = 1
episodeEd = 53

for i in range(episodeSt, episodeEd):

    # Get Html
    url = x.format(i=i)
    response = rq.get(url)
    body = response.text

    # Get m3u8 path
    st = body.find("https:\/\/pptv.com-h-pptv.com\/")
    ed = body[st::].find("m3u8") + len("m3u8") + st
    m3u8 = body[st:ed]

    # youtube-dl
    os.system("youtube-dl {m3u8} --output {i:0>2}.mp4".format(m3u8=m3u8, i=i))


from bilibili_api import video, sync, Credential
import pandas as pd
v = video.Video(bvid='BV1MN4y177PB')

dms = sync(v.get_danmakus(0))
pd.DataFrame(dms).to_csv('danmu.csv')

for dm in dms:
    print(dm)
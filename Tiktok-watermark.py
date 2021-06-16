import requests
import re

urls = input('请输入抖音分享链接：')

paa = re.compile(r'https://v.douyin.com/(.*?)/')
# 匹配video
urls = re.findall(paa,urls)
if urls == []:
    print('未检到链接')
else:
    urls = 'https://v.douyin.com/%s/' % (urls[0])
    print('检测到链接：',urls)
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }

    b = requests.get(urls,headers,allow_redirects=False)
    location = b.headers['location']
    pa = re.compile(r'video/(.*?)/')
    # 匹配video
    fl = re.findall(pa,location)

    url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + str(fl[0])


    f = requests.get(url,headers).json()

    item_list = f['item_list']
    play_addr = item_list[0]
    video = play_addr['video']
    play_addr = video['play_addr']
    uri = play_addr['uri']
    # print(uri)

    uril = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&ratio=720p&line=0' % (uri)

    print('去水印链接：',uril)
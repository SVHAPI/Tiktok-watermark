import requests
import re
import time
# 抖音去除自带水印，仅支持抖音自带水印！！！
print('抖音去除自带水印，仅支持抖音自带水印！！！')

def mian():
    
    urls = input('请输入抖音分享链接：')

    paa = re.compile('https://v.douyin.com/(.*?)/')
    # 匹配输入内容是否带抖音链接
    urls = re.findall(paa,urls)
    if urls == []:
        print('未检到链接')
    else:
        urls = 'https://v.douyin.com/%s/' % (urls[0])
        print('='*40)
        print('检测到链接：',urls)
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X; zh-cn) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/18D61 Quark/5.1.1.1219 Mobile',
        }

        b = requests.get(urls,headers,allow_redirects=False)
        location = b.headers['location']
        pa = re.compile('video/(.*?)/')
        # 匹配video
        fl = re.findall(pa,location)
        # 获取分享链接中返回的location链接
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + str(fl[0])

        f = requests.get(url,headers).json()

        item_list = f['item_list']
        
        if item_list == []:
            print('作品已被作者下架!')
        else:
            print('='*15,'视频详情','='*15)
            list0 = item_list[0]

            author = list0['author']
            print('作者昵称：',author['nickname'])

            author = list0['author']

            print('作者账号：',author['unique_id'])
            create_time = list0['create_time']
            timeArray = time.localtime(create_time)
            otherStyleTime = time.strftime("%Y年%m月%d日 %H:%M:%S", timeArray)
            print('发布时间：',otherStyleTime)
            statistics = list0['statistics']
            comment_count = statistics['comment_count']
            # 视频评论量
            digg_count = statistics['digg_count']
            # 视频点赞量
            share_count = statistics['share_count']
            # 视频分享量
            print('点赞量：',digg_count,'评论量：',comment_count,'分享量：',share_count) 
            share_info = list0['share_info']
            share_title = share_info['share_title']
            print('视频文案：',share_title)
             

            if list0['images'] == None:
                # 判断链接类型 图集/视频
                print('作品类型：视频')
                print('='*40)
                video = list0['video']
                play_addr = video['play_addr']
                uri = play_addr['uri']
                print('='*15,'解析内容','='*15)
                uril = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&ratio=720p&line=0' % (uri)
                
                print('去水印视频链接：',uril)
                print('='*40)
            else:
                images = list0['images']
                ss = '作品类型：图集  共%s张图片' % (len(images))
                print(ss)
                print('='*15,'解析内容','='*15)
                for i in images:
                    uri = i['uri']
                    urlss = 'https://p1.douyinpic.com/img/%s~noop.jpeg' % (uri)
                    print('去水印图片链接：',urlss)
                video = list0['video']
                play_addr = video['play_addr']
                print('图集背景音乐：',play_addr['uri'])
                print('='*40)


while True:
    mian()
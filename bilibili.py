from bilibili_api import comment, sync
import pandas as pd

from bilibili_api import settings

settings.proxy = "http://27.157.204.34:44440" # 里头填写你的代理地址

async def main():
    # 存储评论
    comments = []
    # 页码
    page = 3601
    # 当前已获取数量
    count = 0
    while page <= 4000:
        # 获取评论
        c = await comment.get_comments(898762590, comment.ResourceType.VIDEO, page)
        # 存储评论
        comments.extend(c['replies'])
        # 增加已获取数量
        count += c['page']['size']
        # 增加页码
        page += 1

        #if count >= c['page']['count']:#
            # 当前已获取数量已达到评论总数，跳出循环
            #break
            
    

    # 打印评论
    comment_only=[]
    time=[]
    for cmt in comments:
        comment_only.append(cmt['content']['message'])
        time.append(cmt['reply_control']['time_desc'])
        #print(f"{cmt['member']['uname']}: {cmt['content']['message']}")

    pd.DataFrame(comment_only).to_csv('comment25.csv')
    pd.DataFrame(time).to_csv('time25.csv')
    # 打印评论总数
    print(f"\n\n共有 {count} 条评论（不含子评论）")


sync(main())
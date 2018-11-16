import json
import time
import urllib.request




import itchat

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:

        while True:
            # 图灵机器人API使用方法
            # 接口地址
            api_url = "http://openapi.tuling123.com/openapi/api/v2"
            # 图灵机器人传送的数据都是json格式的参数
            req = {
                # 获取的信息
                "perception":
                    {
                        # perception 下的信息分类
                        # 文本信息
                        "inputText":
                            {
                                "text": msg['Text']
                            },

                        # 地理位置信息
                        "selfInfo":
                            {
                                # 地址信息
                                "location":
                                    {
                                        "city": "武汉",
                                        "province": "武汉",
                                        "street": "光谷大道"
                                    }
                            }
                    },
                # 图灵机器人APi接口信息
                "userInfo":
                    {
                        # 图灵机器人API的接口
                        "apiKey": "0ed496abc4954f9eb2146850dc399450",
                        "userId": "e9a89d17e75c8c50",
                        'groupId': "图灵机器人",
                        'userIdName': "小l"
                    }
            }
            # print(req)
            # 将字典格式的req编码为utf8的字符串
            req = json.dumps(req).encode('utf8')
            # print(req)
            # 爬虫的知识 利用urllib.request.Request爬取图灵机器人的API并发送请求
            http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
            # 获取图灵机器人的回复
            response = urllib.request.urlopen(http_post)
            #
            response_str = response.read().decode('utf8')
            # print(type(response_str))
            response_dic = json.loads(response_str)
            # print(response_dic)
            # api 的异常信息
            intent_code = response_dic['intent']['code']
            # results 输出的结果集 0

            results_text = response_dic['results'][0]['values']['text']

            # print('code：' + str(intent_code))

            return results_text


if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
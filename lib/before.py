'''
    用于消息请求前的数据处理

    一般用于安全、鉴权等业务逻辑

    如果类的 __init__ 方法返回 none 或 false ，当前的请求将不会被处理。
    接口会返回一个错误。

'''

class XSS:
    ''' xss 攻击防护，对敏感符号进行转译。'''
    def __init__(self,request):
        pass

class SQL:
    ''' 这里不写，你不用SQL拼接语句不就好了嘛！ '''
    pass


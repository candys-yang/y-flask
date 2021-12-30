'''
    用于消息请求前的数据处理

    如果类的 __init__ 方法返回 false ，当前的请求将不会被处理。
    接口会返回一个错误。

    True  检查通过
    False 检查不通过
'''
import logging
from flask import current_app

import config

############################################
#   before_request
############################################
class XSS:
    ''' xss 攻击防护'''
    def __init__(self,request):
        self.request = request

    def Status(self):
        for i in self.request.args: 
            if self.CheckStr(self.request.args[i]) == False: 
                logging.warn("E-5001.001  XSS检查不通过，位置：request.args 。")
                return False
        for i in self.request.form: 
            if self.CheckStr(i) == False: 
                logging.warn("E-5001.002  XSS检查不通过，位置：request.form 。")
                return False
            if self.CheckStr(self.request.form[i]) == False: 
                logging.warn("E-5001.003  XSS检查不通过，位置：request.form 。")
                return False
        for i in self.request.headers:
            l = list(i)
            if self.CheckStr(str(l[0])) == False: 
                logging.warn("E-5001.004  XSS检查不通过，位置：request.headers 。")
                return False
            if self.CheckStr(str(l[1])) == False: 
                logging.warn("E-5001.005  XSS检查不通过，位置：request.headers 。")
                return False
        if self.request.is_json:
            kvl = self.JsonEach(self.request.get_json())
            ct = ''
            for i in kvl: ct = ct + str(i)
            if self.CheckStr(ct) == False: 
                logging.warn("E-5001.006  XSS检查不通过，位置：request.json 。")
                return False
        return True

    def CheckStr(self,s:str):
        ''' 检查非法字符 

            带有危险字符，False
        '''
        if s.find("<") > -1: return False
        if s.find(">") > -1: return False
        if s.find("&") > -1: return False
        return True

    def JsonEach(self,j:dict):
        ''' 遍历所有的键值

            Returns:[k,v]
        '''
        re = []
        for i in j:
            if type(j[i]) == str:
                re.append(i)
                re.append(j[i])
            if type(j[i]) == dict:
                re.append(i)
                for ii in self.JsonEach(j[i]):
                    re.append(ii)
        return re


############################################
#   after_request
############################################

class ApiCount:
    ''' 用于统计 api 接口调用情况 '''
    def __init__(self,request) -> None:
        print(request.base_url)
        print(request.method)

        pass



############################################
#   app
############################################

class App:
    ''' 用于app.py的扩展 '''
    def __init__(self) -> None:...

    def InitConfig(self):
        ''' 
            config.py   如果使用 ETCD 作为配置中心
            则需要在config.py.ETCD_MAP编写应用与 ETCD 配置中心配置项的映射关系。
        '''

        # with current_app.app_context():
        #     if 'test' not in current_app.config:
        #         current_app.config.update({"test":1111111111})
        #     nn = current_app.config['test']
        #     nn += 1
        #     current_app.config['test'] = nn
        #     return str(current_app.config['test']) 

import click
from flask import Flask
from flask import request,Response,current_app
import datetime

from werkzeug.wrappers import response

import config
from lib import cmd
from lib import app_handle


app = Flask(__name__)

def flask_app_context():
    """
    """
    with current_app.app_context():
        if 'test' not in current_app.config:
            current_app.config.update({"test":1111111111})
        nn = current_app.config['test']
        nn += 1
        current_app.config['test'] = nn
        return str(current_app.config['test']) 

cmd.Application(app)



''' 请求消息处理 '''
@app.before_request
def reqs():
    print('\n',app_handle.App().Test())
    if app_handle.XSS(request).Status() == False:
        re = config.RESPONSE
        re['results'] = '-500'
        re['text'] = 'E-5001  请求内容包含非法字符：<, >, & 。请检查整个请求报文中，是否包含了这些字符。'
        return re,500
    app_handle.ApiCount(request)
    pass

''' 返回消息处理'''
@app.after_request
def req(environ:Response):
    return environ



#########################################################
# 注入接口路由
#   https://dormousehole.readthedocs.io/en/latest/views.html#api
#
#   第一个参数为url路径，view_func 为类库的路径（加上 .as_view() 初始化）
#########################################################
'''
app.add_url_rule(
    '/test/<path:subpath>',view_func=ClassName.as_view('test'))

class ClassNAME(MethodView):
    #定义路由的类
    def get(self,subpath):return config.RESPONSE
'''


#########################################################
# 常规的 Flask 写法
#   如果使用了路由注入，不应使用 @app.route() 来重复注册路由。
#########################################################

@app.route('/', methods=["POST", "GET"])
def Index(): 
    # print(request.args)
    # print(request.form)
    # print(request.headers)
    # if request.is_json: print(request.get_json())
    # print(request.get_data())
    # print(request.host)
    # print(request.user_agent)
    # print(request.cookies)
    # print(request.__dir__())

    return config.RESPONSE




if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.debug = True
    app.run()
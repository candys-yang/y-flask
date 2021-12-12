import click
from flask import Flask
from flask import request
import datetime

import config
from lib import cmd
from lib import before


app = Flask(__name__)
cmd.Application(app)



''' 请求消息处理 '''
@app.before_request
def reqs():
    before.XSS(request)
    pass


@app.route('/', methods=["POST", "GET"])
def Index(): 
    return config.RESPONSE

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
    def get(self,subpath):return config.RESPONSE

'''


if __name__ == '__main__':

    app.config['JSON_AS_ASCII'] = False
    app.debug = True
    app.run()
'''
    为 Flask 应用提供命令行操作的模块

    Application 应用内置的命令
    Develop     用于开发者自定义的命令

'''
import click

# class Main():
#     ''' 主函数 '''
#     def __init__(self,app):
        
#         @app.cli.command("create-user")
#         @click.argument("name")
#         @click.option('-name', prompt='Your name', help='The person to greet.')
#         def create_user(name):
#             '''创建'''
#             print(name)
#             print(app.open_session(request))
#             return 'create user ' + str(name)
        
class Application():
    ''' Flask 脚手架内置的命令 ''' 
    def __init__(self,app):
        ''' 实例化 Flask 脚手架内置命令。 '''
        @app.cli.command("migrate")
        def __V_Migrate(): 
            ''' 通过 config.py 配置文件进行ORM模型迁移（Sqlalchemy）。 ''' 
            self.Migrate()
        
    def Migrate(self):
        pass
    
    pass

class Develop():
    ''' 开发者自定义的命令 '''
    
    pass

    
    
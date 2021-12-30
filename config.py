'''
    应用配置文件
    
'''
APPNAME = 'Y-Flask'

# 配置模式
#   这里设定配置模式是使用 etcd 还是使用本地配置文件的方式。
#   如果设置为 etcd ，需要配置 etcd 相关的配置项。
#   如果设置为 local，需要配置 本地配置项的相关参数
CONFIG_MOD = "etcd"


# 远程配置项
#   ETCD_URL        应用配置的主目录可以使用[]定义多个地址
#                   应当使用etc其他节点的相同url路径。
#   ETCD_USER       ETCD授权用户
#   ETCD_PWD        ETCD授权用户的密码
#   ETCD_CA         ETCD的客户端CA证书路径
#   ETCD_MAP        若使用ETCD作为配置中心，则需要在此编写键值的映射关系。
#                   ETCD_MAP = {
#                       MYSQL_MASTER = {
#                           "active": True, 
#                           "host": ETCD对应配置的主键名称, 
#                           "user": ETCD对应配置的主键名称,
#                           "password": ETCD对应配置的主键名称, 
#                           "db": ETCD对应配置的主键名称
#                       }
#                    }

ETCD_URL = "http://127.0.0.1:2379/your_app_name"
ETCD_USER = "yourname"
ETCD_PWD = "password"
ETCD_CA = "client-key.pem"
ETCD_MAP = {

}




# 本地配置项
#   MYSQL_MASTER    数据库主节点配置
#   MYSQL_SALVE     数据库只读节点配置
#   REDIS           缓存数据配置。
#                       dir 表示app脚手架的信息保存在什么目录
#
MYSQL_MASTER = {
    "active": False, 
    "host": "127.0.0.1", 
    "user": "",
    "password": "", 
    "db": ""
}
MYSQL_SALVE = {
    "active": False, 
    "host":"127.0.0.1", 
    "user": "",
    "password": "", 
    "db": ""
}
REDIS = {
    "host": "",
    "password": "",
    "db":0,
    "dir":APPNAME + ":cache" 
}

# 数据返回模板（默认返回值）
RESPONSE = {
    "status": "-1", 
    "text": "E-5000  请求失败，服务器未能正确处理该请求。", 
    "results": {}
}

# XSS 
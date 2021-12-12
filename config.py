'''
    应用配置文件
    
'''

# 配置模式
#   这里设定配置模式是使用 etcd 还是使用本地配置文件的方式。
#   如果设置为 etcd ，需要配置 etcd 相关的配置项。
CONFIG_MOD = "etcd"


# 远程配置项
#   ETCD_URL        应用配置的主目录可以使用[]定义多个地址
#                   应当使用etc其他节点的相同url路径。
#   ETCD_USER       ETCD授权用户
#   ETCD_PWD        ETCD授权用户的密码
#   ETCD_CA         ETCD的客户端CA证书路径
ETCD_URL = "http://127.0.0.1:2379/your_app_name"
ETCD_USER = "yourname"
ETCD_PWD = "password"
ETCD_CA = "client-key.pem"


# 本地配置项
#   MYSQL_MASTER    数据库主节点配置
#   MYSQL_SALVE     数据库只读节点配置
#   REDIS           缓存数据配置
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
    "db":0
}

# 数据返回模板（默认返回值）
RESPONSE = {
    "status": "-1", 
    "text": "请求失败，服务器未能正确处理该请求。", 
    "results": {}
}
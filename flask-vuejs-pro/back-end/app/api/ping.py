# 定义我们第一个路由函数，当客户端访问 /ping 时返回包含 Pong! 的 JSON 数据，创建 api/ping.py：
from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify('Pong!')
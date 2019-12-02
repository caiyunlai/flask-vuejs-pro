# 应用启动文件
from app import create_app, db
from app.models import User

app = create_app()

# 由于更新了该文件，必须在terminal重新设置FLASK_APP环境变量，即set FLASK_APP=app.py
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}



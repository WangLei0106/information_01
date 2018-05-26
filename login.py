from flask import Flask

# 创建app
app = Flask(__name__)

@app.route('/')
def index():

    return 'index'


if __name__ == '__main__':

    app.run()

from flask import Flask
app = Flask(__name__) #定位目前資料載入的位置用來判別template,static資料夾位置

@app.route('/')
def hello_world():
    return 'Hello, World!'

    
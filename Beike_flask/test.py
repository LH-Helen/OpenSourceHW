from flask import Flask, render_template
from mysql import Mysql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/echarts')
def getdata():
    db = Mysql()
    items=db.getItems()
    return render_template('echarts.html',items=items)

if __name__ == '__main__':
    app.run(debug=True)	#debug=True发生错误时会返回发生错误的地方

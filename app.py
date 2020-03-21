from flask import Flask, render_template
from flask import url_for, escape
app = Flask(__name__)


name = 'luxuanqing'
movies = [
    {'title': '心灵想要大声呼喊', 'year': '2015'},
    {'title': '声之形', 'year': '2016'},
    {'title': '烟花', 'year': '2017'},
    {'title': '紫罗兰永恒花园外传：永远与自动手记人偶', 'year': '2019'}
]


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', name=name, movies=movies)


@app.route('/user/<name>')
def user_page(name):
    return 'User: {}'.format(escape(name))


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

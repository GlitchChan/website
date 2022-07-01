from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
async def index():
    return render_template('index.jinja2', page='Home')


if __name__ == '__main__':
    app.run()

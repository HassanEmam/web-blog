from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_method():
    return "Hello Flask! My first App"

if __name__ == '__main__':
    app.run(port=4999)
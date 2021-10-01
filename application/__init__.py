from flask import Flask
app = Flask (__name__)

@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello Earth !! </h1>"


app = Flask(__name__)
print(app)


if __name__=='__init__':
    app.run()






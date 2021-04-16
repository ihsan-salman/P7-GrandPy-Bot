from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

#if __name__ == "__main__":
#   app.run()

# Config options
app.config.from_object('config')

app.config['SECRET_KEY']

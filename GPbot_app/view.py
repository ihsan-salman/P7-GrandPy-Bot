from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
    return jsonify({
    	"name": "ihsan"
    	})

#if __name__ == "__main__":
#   app.run()

# Config options
app.config.from_object('config')

app.config['SECRET_KEY']


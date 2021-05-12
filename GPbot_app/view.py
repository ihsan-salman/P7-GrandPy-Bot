from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")
	if request.method == 'GET':
		print(request.form['text_output'])



#if __name__ == "__main__":
#   app.run()
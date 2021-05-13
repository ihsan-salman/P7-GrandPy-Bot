from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		print(request.url())
	return render_template("index.html")

@app.route('/input', methods=['GET', 'POST'])
def input():
	if request.method == 'POST':
		print(request.args.get('text_output'))
	return ''


#if __name__ == "__main__":
#   app.run()
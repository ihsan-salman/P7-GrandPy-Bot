from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ask')
def input():
	print(request.args.get('question'))
	return jsonify(resultat='thierno et ihsan vous saluent')


#if __name__ == "__main__":
#   app.run()
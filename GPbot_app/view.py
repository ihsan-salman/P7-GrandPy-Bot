from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html")
	if request.method == 'POST':
		msg = request.form.get('text_input')
		print(msg)



#if __name__ == "__main__":
#   app.run()
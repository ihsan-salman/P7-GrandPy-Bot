from flask import Flask, render_template, request, jsonify

import GPbot_app.funct as function


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ask')
def input():
    # Parse the question input to keep the important information
    print(function.parse('question'))
    parsed_question = function.parse('question')
    # Return 2 sentences of wiki about the information
    wiki_summary = function.wiki_info(parsed_question)
    print(wiki_summary)
    #
    geocode_adress = function.gmap_adress(parsed_question)
    print(geocode_adress)
    # Base url
    url = function.gmap_img(geocode_adress)
    print(url)
    # Return json information for js
    return jsonify(wiki=wiki_summary, adress=geocode_adress, img_url=url)

if __name__ == "__main__":
   app.run()
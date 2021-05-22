'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from flask import Flask, render_template, request, jsonify

import GPbot_app.funct as function


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ask')
def input():
    # Init grandpy sentences
    gp_sentences = function.gp_sentences
    # Parse the question input to keep the important information
    question = request.args.get('question')
    parsed_question = function.parse(question)
    #
    geocode_adress = function.gmap_adress(parsed_question)
    print(geocode_adress)
    # Return 2 sentences of wiki about the information
    wiki_summary = gp_sentences[1] + function.wiki_info(geocode_adress)
    print(wiki_summary)
    # Base url
    google_map_url = function.gmap_link(geocode_adress)
    print(google_map_url)
    # Return json information for js
    return jsonify(wiki=wiki_summary, adress=geocode_adress,
                   img_url=google_map_url)

if __name__ == "__main__":
    app.run()
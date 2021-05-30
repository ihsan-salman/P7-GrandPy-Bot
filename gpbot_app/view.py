'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from flask import Flask, render_template, request, jsonify

import gpbot_app.helper as helper


APP = Flask(__name__)


@APP.route('/')
def index():
    '''Return the html page code'''
    return render_template("index.html")


@APP.route('/ask')
def give_info():
    '''Return a wikipedia summary, a gmap adress and and
       and url for an image of the wished'''
    # Parse the question input to keep the important information
    question = request.args.get('question')
    parsed_question = helper.parse(question)
    # return the corresponding adress of the parsed information
    geocode_adress = helper.gmap_adress(parsed_question)
    # Return 2 sentences of wiki about the information
    wiki_summary = helper.wiki_info(parsed_question)
    # Base url
    google_map_url = helper.gmap_link(geocode_adress)
    # Return json information for javascript
    return jsonify(wiki=wiki_summary, adress=geocode_adress,
                   img_url=google_map_url)


if __name__ == "__main__":
    APP.run()

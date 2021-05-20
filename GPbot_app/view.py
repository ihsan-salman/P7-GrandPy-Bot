from flask import Flask, render_template, request, jsonify
import googlemaps
import wikipedia
import pprint
from config import API_KEY, STOPWORDS


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ask')
def input():
    question = request.args.get('question')
    parsed_word = []
    question_parse = question.split()
    for word in question_parse:
        if word not in STOPWORDS and word not in ('?', '!'):
            parsed_word.append(word)
    parsed_question = ' '.join(parsed_word)
    print(parsed_question)

    wikipedia.set_lang("fr") 
    gmaps = googlemaps.Client(key=API_KEY)
    try:
        geocode_adress = ''
        geocode_result = gmaps.geocode(parsed_question)
        geocode_adress = geocode_result[0]['formatted_address']
        pprint.pprint(geocode_result)
        pprint.pprint(geocode_adress)
    except googlemaps.exceptions.HTTPError:
        print('rentrez une adresse valide')

    try:
        wiki_summary = ''
        wiki_summary = wikipedia.summary(parsed_question, sentences=2)
        print(wiki_summary)
    except wikipedia.exceptions.WikipediaException:
        print('rentrez une recherche valide')
    return jsonify(wiki=wiki_summary, adress=geocode_adress)


#if __name__ == "__main__":
#   app.run()
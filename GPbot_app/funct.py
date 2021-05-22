'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from flask import request
import googlemaps
import wikipedia
import pprint
from config import API_KEY, STOPWORDS

def parse(input_sentence):
	# Parse the question input to keep the important information
    question = request.args.get(input_sentence)
    parsed_word = []
    question_parse = question.split()
    for word in question_parse:
        if word not in STOPWORDS and word not in ('?', '!'):
            parsed_word.append(word)
    parsed_question = ' '.join(parsed_word)
    return parsed_question

def wiki_info(parsed_info):
    wikipedia.set_lang("fr")
    # Return 2 sentences of wiki about the information
    try:
        wiki_summary = ''
        wiki_summary = wikipedia.summary(parsed_info, sentences=2)
        return wiki_summary
    except wikipedia.exceptions.WikipediaException:
        print('rentrez une recherche valide')

def gmap_adress(parsed_info):
    gmaps = googlemaps.Client(key=API_KEY)
    # Return the adress of the input information
    try:
        geocode_result = gmaps.geocode(parsed_info)
        geocode_adress = geocode_result[0]['formatted_address']
        return geocode_adress
    except googlemaps.exceptions.HTTPError:
        print('rentrez une adresse valide')

def gmap_img(adress):
    # Base url
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    # Updated url
    url = base_url + "center=" + adress + "&zoom=13&size=300x300&key=" + API_KEY
    return url

gp_sentences = ["Bien sûr mon poussin ! La voici : ",
                "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?"]

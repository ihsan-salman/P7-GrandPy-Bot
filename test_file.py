import gpbot_app.helper as helper
import json

def test_parsed():
    '''test the parsed information'''
    parsed_info = helper.parse('ihsan le la les ils salman')
    print(parsed_info)
    assert parsed_info == 'ihsan salman'

def test_gmap_response():
    gmap_adress = helper.gmap_adress('la tour eiffel')
    with open('json/gmap.json') as json_data:
        data_dict = json.load(json_data)
    assert data_dict[0]['formatted_address'] == gmap_adress

def test_wiki_response():
    wiki_info = helper.wiki_info('la tour eiffel')
    print(wiki_info)
    assert wiki_info == 'La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.'
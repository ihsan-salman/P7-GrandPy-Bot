'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


import json
import gpbot_app.helper as helper


def test_parsed():
    '''test the parsed information'''
    parsed_info = helper.parse('la tour eiffel')
    print(parsed_info)
    assert parsed_info == 'tour eiffel'


def test_gmap_response():
    '''test the adress function with a parsed information'''
    gmap_adress = helper.gmap_adress(helper.parse('la tour eiffel'))
    with open('gpbot_app/json/gmap.json') as json_data:
        data_dict = json.load(json_data)
    assert data_dict[0]['formatted_address'] == gmap_adress


def test_wiki_response():
    '''test the wikipedia sentences with a parsed infomation'''
    wiki_info = helper.wiki_info(helper.parse('la tour eiffel'))
    with open('gpbot_app/json/wiki.json') as json_data:
        data_dict = json.load(json_data)
    assert wiki_info == data_dict[0]["wiki_info"]


def test_gmap_link():
    '''test the gmap link with an adress'''
    gmap_link = helper.gmap_link(
        helper.gmap_adress(helper.parse('la tour eiffel')))
    with open('gpbot_app/json/gmap_link.json') as json_data:
        data_dict = json.load(json_data)
    assert gmap_link == data_dict[0]["gmap_link"]


def test_ask_view():
    '''test the value return by the ask view'''
    parsed_info = helper.parse('la tour eiffel')
    gmap_adress = helper.gmap_adress(parsed_info)
    wiki_info = helper.wiki_info(parsed_info)
    gmap_link = helper.gmap_link(gmap_adress)
    json_info = {"parsed_info": parsed_info, "gmap_adress": gmap_adress,
                 "wiki_info": wiki_info, "gmap_link": gmap_link}
    with open('gpbot_app/json/view.json') as json_data:
        data_dict = json.load(json_data)
    assert json_info == data_dict[0]

'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


import gpbot_app.helper as helper


def test_parsed():
    '''test the parsed information'''
    parsed_info = helper.parse('la tour eiffel')
    assert parsed_info == 'tour eiffel'


def test_wiki_response(monkeypatch):
    '''test the wikipedia sentences with a parsed infomation'''
    result = {"La Liberté éclairant le monde, (en anglais : Liberty Enligh"
              "tening the World), ou simplement Liberté, plus connue sous"
              "le nom de statue de la Liberté (Statue of Liberty), est l'"
              "un des monuments les plus célèbres des États-Unis. Cette s"
              "tatue monumentale est située à New York, sur la Liberty Is"
              "land, au sud de Manhattan, à l'embouchure de l'Hudson et à "
              "proximité d'Ellis Island."}

    def mockreturn(*param):
        return result

    monkeypatch.setattr(
        "gpbot_app.helper.wiki_info", mockreturn
    )

    assert helper.wiki_info("statue liberté") == result


def test_gmap_link(monkeypatch):
    '''test the gmap link with an adress'''
    result = {"https://maps.googleapis.com/maps/api/staticmap?center=Statue"
              "%20of%20Liberty%20National%20Monument,%20New%20York,%20NY%20"
              "10004,%20USA&zoom=13&size=300x300&key=AIzaSyD2PvH-FLa3KhGyY7"
              "Z02VLMG-J8al41JrI"}

    def mockreturn(*param):
        return result

    monkeypatch.setattr(
        "gpbot_app.helper.gmap_link", mockreturn
    )
    assert helper.gmap_link("statue liberté") == result


def test_gmap_adress(monkeypatch):
    """test the gmap adress with an parsed information"""
    result = {"Statue of Liberty National Monument, New York, NY 10004, USA"}

    def mockreturn(*param):
        return result

    monkeypatch.setattr(
        "gpbot_app.helper.gmap_adress", mockreturn
    )

    assert helper.gmap_adress("statue liberté") == result


def test_ask_view(monkeypatch):
    '''test the value return by the ask view'''
    result = {"parsed_info": "statue liberté",
              "gmap_adress": "Statue of Liberty National Monument, New Yor"
              "k, NY 10004, USA",
              "wiki_info": "La Liberté éclairant le monde, (en anglais : L"
              "iberty Enlightening the World), ou simplement Liberté, plus"
              " connue sous le nom de statue de la Liberté (Statue of Libe"
              "rty), est l'un des monuments les plus célèbres des États-Un"
              "is. Cette statue monumentale est située à New York, sur la"
              " Liberty Island, au sud de Manhattan, à l'embouchure de l'"
              "Hudson et à proximité d'Ellis Island.",
              "gmap_link": "https://maps.googleapis.com/maps/api/staticma"
              "p?center=Statue%20of%20Liberty%20National%20Monument,%20New"
              "%20York,%20NY%2010004,%20USA&zoom=13&size=300x300&key=AIzaS"
              "yD2PvH-FLa3KhGyY7Z02VLMG-J8al41JrI"}

    def mockreturn1(*param):
        return result["parsed_info"]

    def mockreturn2(*param):
        return result["gmap_adress"]

    def mockreturn3(*param):
        return result["wiki_info"]

    def mockreturn4(*param):
        return result["gmap_link"]

    monkeypatch.setattr(
        "gpbot_app.helper.parse", mockreturn1
    )
    monkeypatch.setattr(
        "gpbot_app.helper.gmap_adress", mockreturn2
    )
    monkeypatch.setattr(
        "gpbot_app.helper.wiki_info", mockreturn3
    )
    monkeypatch.setattr(
        "gpbot_app.helper.gmap_link", mockreturn4
    )

    parsed_info = helper.parse('statue liberté')
    gmap_adress = helper.gmap_adress('statue liberté')
    wiki_info = helper.wiki_info('statue liberté')
    gmap_link = helper.gmap_link('statue liberté')
    json_info = {"parsed_info": parsed_info, "gmap_adress": gmap_adress,
                 "wiki_info": wiki_info, "gmap_link": gmap_link}
    assert json_info == result

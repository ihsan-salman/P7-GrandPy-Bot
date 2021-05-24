import gpbot_app.helper as helper


def test_parsed():
    parsed_info = helper.parse('ihsan le la les ils salman')
    print(parsed_info)
    #assert parsed_info == 'ihsan salman'

'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


import os
from gpbot_app import APP

if __name__ == '__main__':
    APP.debug = True
    port = int(os.environ.get("PORT", 8080))
    APP.run(host='0.0.0.0', port=port)

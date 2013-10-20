MusicBrainz Database Tools
==========================

Installation:

    virtualenv --system-site-packages e
    . e/bin/activate
    pip install -r requirements.txt
    python setup.py develop

Configuration:

	cp settings.py.sample settings.py
	vim settings.py

Start the development server:

    MBDATA_API_SETTINGS=`pwd`/settings.py python -m mbdata.web.app


#!task/bin/python

from app import app



app.config.from_object(__name__)
app.run(debug=True, host='0.0.0.0', port=8000)

import os
from bottle import run, sys, Bottle

from backend.handlers import app
from backend.static_handlers import staticHandler
from backend.page_handlers import pageHandler

app.merge(staticHandler)
app.merge(pageHandler)
run(app, host='localhost', port=os.environ.get('PORT', 5000))
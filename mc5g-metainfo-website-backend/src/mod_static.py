#!/usr/bin/python3

import os
import quart

UI_ROOT='/ui/v2/'

STATIC_PATH=os.environ['STATIC_PATH']

mod = quart.Blueprint('static', __name__, static_folder=STATIC_PATH, static_url_path='', url_prefix='')

# Redirect all UI paths hitting the server to index.html since this is a single page application.
@mod.route('{}<path:target>'.format(UI_ROOT))
@mod.route('{}'.format(UI_ROOT), defaults={'target': ''})
async def uiRedirect(target):
  return await quart.send_from_directory(STATIC_PATH, 'index.html')

if UI_ROOT != '/':
  # Redirect root resource to UI.
  @mod.route('/')
  async def homepage():
    return quart.redirect(UI_ROOT)

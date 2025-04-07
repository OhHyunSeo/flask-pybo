from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcb \xafQ\x0b\xc2\x0e\xb4s\xb2\x8b\x00\x92\xd3C\x91'

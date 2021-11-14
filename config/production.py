from config.default import *

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'bbs.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user='postgres',
        pw='9906',
        url='localhost',
        db='diary'
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xc3\x08\xa1\x89K\x00-\x1a\x98\xa7\x8a\x00\x1d`\x02\x9c'
import os

secret = os.getenv('SECRET', 'shhh its a secret')
db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/london-chic')

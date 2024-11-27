import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://avnadmin:AVNS_RqY9EXjcvPpzDwoQHci@library-webapp-db-aubreyocenar96-3671.e.aivencloud.com/defaultdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
from peewee import Model, SqliteDatabase, CharField, TextField

db = SqliteDatabase("translations.db")

class TranslationModel(Model):
    text = TextField()
    initial_lang = CharField()
    final_lang = CharField()
    translation = TextField(null = True)

    class Meta:
        database = db

db.connect()
db.create_tables([TranslationModel])
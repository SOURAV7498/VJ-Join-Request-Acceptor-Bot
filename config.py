from os import environ

API_ID = int(environ.get("API_ID", "21140176"))
API_HASH = environ.get("API_HASH", "b081ec8da8cf5263a6593041c1ae2a3b")
BOT_TOKEN = environ.get("BOT_TOKEN", "8154114614:AAHj1qd68lQl0bIIpci7Cq1eWuwGph53Adg")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "1003168773809"))
ADMINS = int(environ.get("ADMINS", "6222491731"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://gouravbolange_db_user:yos9d73FCsyLpiI6@cluster0.wxnzgc0.mongodb.net/?retryWrites=true&w=majority&joinrequetbot=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "joinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))

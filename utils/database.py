import secrets
from pymongo import MongoClient
from urllib.parse import urlparse
from utils.errors import Error
from utils.secure import *
from utils.conf import CONF

class Database:
    # config the db connection
    host = MongoClient(CONF["DB_URI"])
    db = host.shouft
    collection = db.urls

    # add url to db
    def addUrl(self, url):
        try:
            #if url is valid
            if validUrl(url):
                refer = secrets.token_hex(7)
                self.collection.insert_one({ # insert the {url, refer} document in the db collection
                    "url": encrypt(url),
                    "refer": refer
                })
                return refer # return the refer, in other cases return error
            else:
                return Error.INVALID_URL
        
        except:
            return Error.GENERAL_ERROR
        
    # get url from db
    def getUrl(self, refer):
        # fast validation
        if len(refer) != 14: 
            return Error.INVALID_REFER
        
        # if the refer is in the collection --> return the associated url, else return error
        try:
            url = self.collection.find_one({"refer": refer})
            return decrypt(url["url"])
        
        except:
            return Error.GENERAL_ERROR

# url validation function
def validUrl(url):
    try:
        parse = urlparse(url)
        return all([parse.scheme, parse.netloc])
    
    except:
        return False

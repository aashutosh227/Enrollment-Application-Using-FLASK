#This file has the configuration modules that stores configurations across application
import os

class Config(object):
    #This key is used for security purpose in the application while it interacts across the server
    #It is used as signature key to make sure anything sent across server is not been altered or hacked
    #For e.g when using form or setting cookies the key is used to check is they are altered or not.
    #If altered then session is set as invalid.
    SECRET_KY = os.environ.get('SECRET_KEY') or "illusion" 
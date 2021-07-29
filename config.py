import os
class Config():
    REGISTERED_USERS = {
        #variable names in all caps indicate that that variable will be a constant
        'kevinb@codingtemple.com': {'name':'Kevin', 'password': 'abc123'},
        'johnl@codingtemple.com': {'name':'John', 'password': 'Colt45'},
        'joel@codingtemple.com': {'name':'Joel', 'password': 'MorphinTime'}
    }
#pip install flask forms
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'You-will-never-guess'
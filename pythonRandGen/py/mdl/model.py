'''
Created on 21 sept. 2016

@author: dlrr
'''
from faker import Faker

class Model(object):
    
    #Constructor
    def __init__(self):
        self.init_vars()
        self.lista_items = []
        self.lista_items.append(self.config_id)
        self.lista_items.append(self.account_deal_id)
        self.lista_items.append(self.facility_id)
        
    def init_vars(self):
        self.fake = Faker()
        self.config_id = self.fake.pydecimal(left_digits=None, right_digits=None, positive=True)
        self.account_deal_id = self.fake.pystr(min_chars=None, max_chars=20)
        self.facility_id = self.fake.pystr(min_chars=None, max_chars=20)     
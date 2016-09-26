'''
Created on 21 sept. 2016

@author: dlrr
'''

class modelCounterParty:
    
    def __init__(self, model):
        self.model = model 
        
    def getItems(self):
        if len(self.model.lista_items) > 3:
            to_remove = self.model.lista_items[3]
            self.model.lista_items.remove(to_remove)
        coustomer_id = self.model.fake.pydecimal(left_digits=None, right_digits=None, positive=True)
        self.model.lista_items.append(coustomer_id)
        print(coustomer_id)
        return self.model.lista_items
    
    def getFileName(self):
        return 'model_counterparty.csv'
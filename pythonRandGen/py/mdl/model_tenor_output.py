'''
Created on 21 sept. 2016

@author: dlrr
'''
class modelTenorOutput:
    
    def __init__(self, model):
        self.model = model 
        
    def getItems(self):
        return self.model.lista_items
    
    def getFileName(self):
        return 'model_tenor_output.csv'
# -*- coding: utf-8 -*-
import csv

from py.mdl.model import Model
from py.mdl.model_tenor_output import modelTenorOutput
from py.mdl.model_collateral import modelCollateral
from py.mdl.model_oth_rep import modelOthRep
from py.mdl.model_counterparty import modelCounterParty
from py.mdl.non_model_oth_rep import nonModelOthRep
from py.mdl.model_core_calc_output import modelCoreCalcOutput
from py.mdl import model_counterparty


class mainModule:
    
    def prompt(self):
        print( "###### Generador Accounts ######\n\n")
        print( "cantidad de accounts?" )
        accounts = input("Introduce tu opcion:\n")
        accounts = int(accounts)
        print( "cantidad de counter_party (x account)" )
        counterparty = input("Introduce tu opcion:\n")
        counterparty = int(counterparty)
        print( "cantidad de collateral (x account)" )
        collateral = input("Introduce tu opcion:\n")
        collateral = int(collateral)
        #Limpiamos la pantalla
        #self.clearShell()
        self.main(accounts, collateral, counterparty)
        
    def main(self, accounts, collateral, counterparty ):
        for i in range(accounts):
            lista_model_core_calc_output = []
            lista_model_tenor_output = []
            lista_model_oth_rep = []
            lista_non_model_oth_rep = []
            model = Model()
            model_core_calc_output = modelCoreCalcOutput(model)
            model_tenor_output = modelTenorOutput(model)  
            model_oth_rep =  modelOthRep(model)
            non_model_oth_rep = nonModelOthRep(model)   
            model_counterparty = modelCounterParty(model)
            #print("model_core_calc_output\n" + str( model_core_calc_output.getItems() ))
            #print("model_tenor_output\n" + str( model_tenor_output.getItems() ))  
            #print("model_oth_rep\n" + str( model_oth_rep.getItems() ))
            #print("non_model_oth_rep\n" + str( non_model_oth_rep.getItems() ))   
            lista_model_core_calc_output.append(model_core_calc_output.getItems())
            lista_model_tenor_output.append(model_tenor_output.getItems())
            lista_model_oth_rep.append(model_oth_rep.getItems())
            lista_non_model_oth_rep.append(non_model_oth_rep.getItems())
            self.genFile(lista_model_core_calc_output, model_core_calc_output.getFileName() )
            self.genFile(lista_model_tenor_output, model_tenor_output.getFileName())
            self.genFile(lista_model_oth_rep, model_oth_rep.getFileName())
            self.genFile(lista_non_model_oth_rep, non_model_oth_rep.getFileName()) 
            model_collateral = modelCollateral(model)
            #print("len model_collateral " + str( len(model_collateral.getItems()) ))
            #print("model_collateral\n" + str( model_collateral.getItems() ))
            self.genCollateralFile(model_collateral, collateral)
            model_counterparty = modelCounterParty(model)
            #print("len model_counterparty " + str( len(model_counterparty.getItems()) ))
            #print("model_counterparty\n" + str( model_counterparty.getItems() ))
            self.genCounterPartyFile(model_counterparty, counterparty)

    ''' 
       TODO: cuando escribe dos collateral el segundo sobre-escribe el primer fichero
    '''
    def genCollateralFile(self, model_collateral, collateral):
        print("colateral: " + str(collateral) )
        csvsalida = open(model_collateral.getFileName(), 'a', newline='')
        for j in range(collateral):
            lista_model_collateral = []
            salida = csv.writer(csvsalida)
            lista_model_collateral.append(model_collateral.getItems())
            salida.writerows(lista_model_collateral)
            del salida
        csvsalida.close()
    
    def genCounterPartyFile(self, model_counterparty, counterparty):
        print("counter party: " + str(counterparty) )
        csvsalida = open(model_counterparty.getFileName(), 'a', newline='')
        for j in range(counterparty):
            lista_model_counterparty = []
            salida = csv.writer(csvsalida)
            lista_model_counterparty.append(model_counterparty.getItems())
            salida.writerows(lista_model_counterparty)
            del salida
        csvsalida.close()                        
    
    def genFile(self, lista_items, file_name):
        csvsalida = open(file_name, 'a', newline='')
        salida = csv.writer(csvsalida)
        salida.writerows(lista_items)
        del salida
        csvsalida.close()

if __name__ == "__main__":
    mainModule = mainModule()
    mainModule.prompt()

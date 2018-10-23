#coding: utf-8

import os
import os.path
import codecs
import json
import datetime

class Database_cl(object):

    def __init__(self):
        self.data_o = None

    def read_mitarbeiter(self, id_spl):
        data_opl = None
        if id_spl != None:
            data_opl = self.data_o['mitarbeiter']['list'][id_spl]
        return data_opl

    def read_kunde(self, id_spl):
        data_opl = None
        if id_spl != None:
               data_opl = self.data_o['kunde']['list'][id_spl]
        return data_opl

    def read_projekt(self, id_spl):
        data_opl = None
        if id_spl != None:
               data_opl = self.data_o['projekt']['list'][id_spl]
        return data_opl

    def update_projekt(self, id_spl, data_opl):
        self.data_o['projekt']['list'][id_spl] = data_opl
        self.saveData_p()
        return

    def update_kunde(self, id_spl, data_opl):
        self.data_o['kunde']['list'][id_spl] = data_opl
        self.saveData_p()
        return

    def update_mitarbeiter(self, id_spl, data_opl):
        self.data_o['mitarbeiter']['list'][id_spl] = data_opl
        self.saveData_p()
        return

    def create_mitarbeiter(self, data_opl):
        self.data_o['mitarbeiter']['list'][id_spl] = data_opl
        self.saveData_p()
        return

    def create_kunde
        
        return

    def create_projekt

        return

    def delete_mitarbeiter(self, id_spl):
        del self.data_o['mitarbeiter']['list'][id_spl]
        self.saveData_p()
        return

    def delete_kunde(self, id_spl):
        del self.data_o['kunde']['list'][id_spl]
        self.saveData_p()
        return

    def delete_projekt(self, id_spl):
        del self.data_o['projekt']['list'][id_spl]
        self.saveData_p()
        return

    def saveData_p(self):
        with codec.open(os.path.join('data', 'pis.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o)

    def readData_p(self): 
        try: 
            fp_o = codecs.open(os.path.join('data', 'webteams.json'), 'r', 'utf-8') 
        except: 
            # Datei neu anlegen 
            self.data_o = {} 
            for loop_i in range(0,15): ## Änderungen vornehmen für dei 15 als Anzahl der einträge
                self.data_o[str(loop_i)] = ['', '', '', '', '', '', '', ''] 
                self.saveData_p() 
        else: 
            with fp_o: 
                self.data_o = json.load(fp_o)
        return

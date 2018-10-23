#coding: utf-8

import codecs
import os.path
import string

class View_cl(object):
    def __init__(self):
        pass

    def createList_px(self, data_opl):
        markup_s =''
        markup_s += self.readFile_p('liste0.tpl')
        
        markupTpl_s = self.readFile_p('liste1.tpl')
        lineT_o = string.Template(markupTpl_s)
        #Schleife zur Erstellung der Tabellenzeilen
        #!!!! Aufgabe dynamisch Anzahl der Zeilen erstellen!!!!

        for loop_i in range(0,15):
            data_a = data_opl[str(loop_i)]
            markup_s += lineT_o.safe_substitute(
            #!!!! Datenstruktur hinzufügen!!!!                                  
      

            "projektnummer": int(data_opl["projektnummer"]),
            "pbezeichung": data_opl["pbezeichung"],
            "pbeschreibung": data_opl["pbezeichung"],
            "pzeitraum": data_opl["pzeitraum"],
            "pbudget": data_opl["pbudget"],
            "kid": data_opl["kid"], #!!! Verweis auf Kundenid erstellen
            "mids": data_opl["mids"] ##!!! Neue Liste für alle Mitarbeiter inkl. Stunden ???
        }                                 



            markup_s += self.readFile_p('liste2.tpl')

        return markup_s

    def createForm_px(self, id_spl, data_opl):

        markup_s = ''
        markup_s += self.readFile_p('form0.tpl')
        markupTpl_s = self.readFile_p('form1.tpl')
        lineT_o = string.Template(markupTpl_s)
        markup_s = lineT_o.safe_substitute(
            #!!! Aufgabe Datenstruktur hinzufügen!!! 


 
            "projektnummer": int(data_opl["projektnummer"]),
            "pbezeichung": data_opl["pbezeichung"],
            "pbeschreibung": data_opl["pbezeichung"],
            "pzeitraum": data_opl["pzeitraum"],
            "pbudget": data_opl["pbudget"],
            "kid": data_opl["kid"], #!!! Verweis auf Kundenid erstellen
            "mids": data_opl["mids"] ##!!! Neue Liste für alle Mitarbeiter inkl. Stunden ???
    


            )

        markup_s += self.readFile_p('form2.tpl')
        return markup_s


    def readFile_p(self, fileName_spl):
        content_s =''
        with codecs.open(os.path.join('content', fileName_spl), 'r', 'uft-8') as fp_o:
            content_s = fp_o.read()
        return content_s

    
#coding: utf-8
import cherrypy

from .database import Database_cl
from .view import View_cl

class Application_cl(object):
    def __init__(self):
        self.db_o = Database_cl()
        self.view_o = View_cl()

    @cherrypy.expose

    def index(self):
        return self.view_o.create_start_p()

    @cherrypy.expose

    def add_projekt(self):
        return self.create_projekt_form_p()
    @cherrypy.expose

    def add_kunde(self):
        return self.create_kunde_form_p()
    @cherrypy.expose

    def add_mitarbeiter(self):
        return self.create_mitarbeiter_form_p()
    @cherrypy.expose

    def edit_Mitarbeiter(self,id):
        return self.create_mitarbeiter_form_p(id)
    @cherrypy.expose

    def edit_Kunde(self,id):
        return self.create_kunde_form_p(id)
    @cherrypy.expose

    def edit_Projekt(self,id):
        return self.create_projekt_form_p(id)
    @cherrypy.expose

    def save_projekt(self, **data_opl):
        id_s = data_opl["id_s"]
        data_a =  { 
            "projektnummer": int(data_opl["projektnummer"]),
            "pbezeichung": data_opl["pbezeichung"],
            "pbeschreibung": data_opl["pbezeichung"],
            "pzeitraum": data_opl["pzeitraum"],
            "pbudget": data_opl["pbudget"],
            "kid": data_opl["kid"], #!!! Verweis auf Kundenid erstellen
            "mids": data_opl["mids"] ##!!! Neue Liste für alle Mitarbeiter inkl. Stunden ???
        }

        if id_s != "None":
        #Update
            self.db_o.update_projekt(id_s, data_a)
        else:
        #Erstellen
            id_s = self.db_o.create_projekt(data_a)
        return self.create_projekt_list()
    @cherrypy.expose

    def save_kunde(self, **data_opl):
        id_s = data_opl["id_s"]
        data_a = {
            "nummer": int(data_opl["nummer"]),
            "kbezeichnung": data_opl["kbezeichnung"],
            "ap": data_opl["ap"],
            "ort": data_opl["ort"]
            }

        if id_s != "None":
            self.db_o.update_kunde(data_a)
        else:
            id_s = self.db_o.create_kunde(data_a)
        return self.create_kunde_list()
    @cherrypy.expose

    def save_mitarbeiter(self, **data_opl):
        id_s = data_opl["id_s"]
        data_a = {
            "mname": data_opl["mname"],
            "mvorname": data_opl["mvorname"],
            "funktion": data_opl["funktion"]
            }
        if id_s != "None":
            self.db_o.update_mitarbeiter(data_a)
        else:
            id_s = self.db_o.create_mitarbeiter(data_a)
        return self.create_mitarbeiter_list()
    @cherrypy.expose

    def delete_projekt(self, id):
        self.db_o.delete_projekt(id)
        return self.create_projekt_list()
    @cherrypy.expose

    def delete_kunde(self, id):
        self.db_o.delete_kunde(id)
        return self.create_kunde_list()
    @cherrypy.expose

    def delete_mitarbeiter(self, id):
        self.db_o.delete_mitarbeiter(id)
        return self.create_mitarbeiter_list()
    @cherrypy.expose

    def create_projekt_list(self):
        data_o = self.db_o.readData_p()
        return self.view_o.create_projekt_form(data_o)
    @cherrypy.expose

    def create_kunde_list(self):
        data_o = self.db_o.readData_p()
        return self.view_o.create_kunde_form(data_o)
    @cherrypy.expose

    def create_mitarbeiter_list(self):
        data_o = self.db_o.readData_p()
        return self.view_o.create_mitarbeiter_form(data_o)
    @cherrypy.expose

    def default(self, *arguments, **kwargs):
        msg_s = "unbekannte Anforderung: " +\
            str(arguments) + \
            ' ' +\
            str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
    default.exposed = True

    def create_projekt_form_p(self, id_spl = None):
        if id_spl != None:
            data_o = self.db_o.read_projekt(id_spl)
        else:
            data_o = {
                "projektnummer": '',
                "pbezeichung": '',
                "pbeschreibung": '',
                "pzeitraum": '',
                "pbudget": '',
                "kid": '',
                "mids": ''
                }
        return self.view_o.create_projekt_form(id_spl, data_o)

    def create_kunde_form_p(self, id_spl = None):
        if id_spl != None:
            data_o = self.db_o.read_kunde(id_spl)
        else:
            data_o = {
                "nummer": '',
                "kbezeichnung": '',
                "ap": '',
                "ort": ''
                }
        return self.view_o.create_kunde_form(id_spl, data_o)

    def create_mitarbeiter_form_p(self, id_spl = None):
        if id_spl != None:
            data_o = self.db_o.read_mitarbeiter(id_spl)
        else:
            data_o = {
                "mname": '',
                "mvorname": '',
                "funktion": ''
                }
        return self.view_o.create_mitarbeiter_form(id_spl, data_o)
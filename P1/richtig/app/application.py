# coding: utf-8
import json
import cherrypy
from .database import Database_cl
from .view import View_cl

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------
	
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.db_o = Database_cl()
		self.view_o = View_cl()
	@cherrypy.expose

	#-------------------------------------------------------
	def index(self):
	#-------------------------------------------------------
		return self.view_o.createstart_px();
	@cherrypy.expose
	
	def addKunde(self):
	#-------------------------------------------------------
		return self.createKundeForm_p()
	@cherrypy.expose
	#-------------------------------------------------------
	def addMitarbeiter(self):
	#-------------------------------------------------------
		return self.createMitarbeiterForm_p()
	@cherrypy.expose

	def addProjekt(self):
	#-------------------------------------------------------
		return self.createProjektForm_p()
	@cherrypy.expose
	
	def editKunde(self, id):
	#-------------------------------------------------------
		return self.createKundeForm_p(id)
	@cherrypy.expose
	
	def editMitarbeiter(self, id):
	#-------------------------------------------------------
		return self.createMitarbeiterForm_p(id)
	@cherrypy.expose

	def editProjekt(self, id):
	#-------------------------------------------------------
		return self.createProjektForm_p(id)
	@cherrypy.expose
	

	def saveKunde(self, **data_opl):
	#-------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = {
		        "bezeichnung": data_opl["bezeichnung"]
		        , "ap": data_opl["ap"]
		        , "nummer": data_opl["nummer"]
			, "ort": data_opl["ort"]
		}
		if id_s != "None":
		# Update-Operation
			self.db_o.updateKunde_px(id_s, data_a)
		else:
		# Create-Operation
			id_s = self.db_o.createKunde_px(data_a)
			
		return self.createKundeList()	
	@cherrypy.expose

	#-------------------------------------------------------
	def saveMitarbeiter(self, **data_opl):
	#-------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = {
			"name": data_opl["name"]
			, "vorname": data_opl["vorname"]
			, "funktion": data_opl["funktion"]
		}
		if id_s != "None":
		# Update-Operation
			self.db_o.updateMitarbeiter_px(id_s, data_a)
		else:
		# Create-Operation
			id_s = self.db_o.createMitarbeiter_px(data_a)
					
		return self.createMitarbeiterList()	
	@cherrypy.expose

	def saveProjekt(self, **data_opl):
	#-------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = {
		        "nummer": data_opl["nummer"]
		        , "bezeichnung": data_opl["bezeichnung"]
		        , "beschreibung": data_opl["beschreibung"]
			, "zeitraum": data_opl["zeitraum"]
			, "budget":data_opl["budget"]
			, "kunden-id":data_opl["kunden-id"]
			, "mitarbeiter-id":data_opl["mitarbeiter-id"]
			, "stunden":data_opl["stunden"]
		}
		if id_s != "None":
		# Update-Operation
			self.db_o.updateProjekt_px(id_s, data_a)
		else:
		# Create-Operation
			id_s = self.db_o.createProjekt_px(data_a)
			
		return self.createProjektList()	
	@cherrypy.expose


	def deleteKunde(self, id):
	#-------------------------------------------------------
		self.db_o.deleteKunde_px(id)
		return self.createKundeList()
	@cherrypy.expose

	#-------------------------------------------------------
	def deleteMitarbeiter(self, id):
	#-------------------------------------------------------
		self.db_o.deleteMitarbeiter_px(id)
		return self.createMitarbeiterList()
	@cherrypy.expose

	def deleteProjekt(self, id):
	#-------------------------------------------------------
		self.db_o.deleteProjekt_px(id)
		return self.createProjektList()
	@cherrypy.expose


	def createKundeList(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()		
		return self.view_o.createKundeList_px(data_o)
	@cherrypy.expose

	def createMitarbeiterList(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()			
		return self.view_o.createMitarbeiterList_px(data_o)
	@cherrypy.expose

	def createProjektList(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()		
		return self.view_o.createProjektList_px(data_o)
	@cherrypy.expose



	def createKundeForm_p(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readKunde_px(id_spl)
		else:
			data_o = {
			        "bezeichnung": '', 
			        "ap": '', 
			        "nummer": '',
				"ort":'',
			}
		return self.view_o.createKundeForm_px(id_spl, data_o)

	#-------------------------------------------------------
	def createMitarbeiterForm_p(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readMitarbeiter_px(id_spl)
		else:
			data_o = {
			        "name": '', 
			        "vorname": '', 
			        "funktion": '',
			}
		return self.view_o.createMitarbeiterForm_px(id_spl, data_o)

	def createProjektForm_p(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readProjekt_px(id_spl)
		else:
			data_o = {
			        "nummer": '', 
			        "bezeichnung": '', 
			        "beschreibung": '',
				"zeitraum": '',
				"budget": '',
				"kunden-id": '',
				"mitarbeiter-id": '',
				"stunden": '',
			}
		return self.view_o.createProjektForm_px(id_spl, data_o)



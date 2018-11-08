# coding: utf-8
import os
import os.path
import codecs
import json
import datetime
#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
	
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.data_o = None
	
	#-------------------------------------------------------
	def readKunde_px(self, id_spl):
	#-------------------------------------------------------
	
		data_opl = None
		if id_spl != None:
			data_opl = self.data_o['kunde']['list'][id_spl]
			
		return data_opl

	def updateKunde_px(self, id_spl, data_opl):
	#-------------------------------------------------------
		self.data_o['kunde']['list'][id_spl] = data_opl
		self.saveData_p()
		return

	def createKunde_px(self, data_opl):
	#-----------------------------------------------------
		self.data_o['kunde']['list'].update({self.data_o['kunde']['count']: ''})
		self.data_o['kunde']['list'][self.data_o['kunde']['count']] = data_opl
		self.data_o['kunde']['count'] += 1
		self.saveData_p();
		return 

	def deleteKunde_px(self, id_spl):
	#-------------------------------------------------------
		del self.data_o['kunde']['list'][id_spl]
		self.saveData_p()

		return

	#-------------------------------------------------------
	def readMitarbeiter_px(self, id_spl):
	#-------------------------------------------------------
	
		data_opl = None
		if id_spl != None:
			data_opl = self.data_o['mitarbeiter']['list'][id_spl]
			
		return data_opl

	def updateMitarbeiter_px(self, id_spl, data_opl):
	#-------------------------------------------------------
		self.data_o['mitarbeiter']['list'][id_spl] = data_opl
		self.saveData_p()
		return

	def createMitarbeiter_px(self, data_opl):
	#-----------------------------------------------------

		self.data_o['mitarbeiter']['list'].update({self.data_o['mitarbeiter']['count']: ''})
		self.data_o['mitarbeiter']['list'][self.data_o['mitarbeiter']['count']] = data_opl
		self.data_o['mitarbeiter']['count'] += 1
		self.saveData_p();
		return 

	def deleteMitarbeiter_px(self, id_spl):
	#-------------------------------------------------------
		del self.data_o['mitarbeiter']['list'][id_spl]
		self.saveData_p()

		return

	#-------------------------------------------------------
	def readProjekt_px(self, id_spl):
	#-------------------------------------------------------
	
		data_opl = None
		if id_spl != None:
			data_opl = self.data_o['projekt']['list'][id_spl]
			
		return data_opl

	def updateProjekt_px(self, id_spl, data_opl):
	#-------------------------------------------------------
		self.data_o['projekt']['list'][id_spl] = data_opl
		self.saveData_p()
		return

	def createProjekt_px(self, data_opl):
	#-----------------------------------------------------
		self.data_o['projekt']['list'].update({self.data_o['projekt']['count']: ''})
		self.data_o['projekt']['list'][self.data_o['projekt']['count']] = data_opl
		self.data_o['projekt']['count'] += 1
		self.saveData_p();
		return 

	def deleteProjekt_px(self, id_spl):
	#-------------------------------------------------------
		del self.data_o['projekt']['list'][id_spl]
		self.saveData_p()

		return


	def readData_p(self):
	#-------------------------------------------------------
		fp_o = codecs.open(os.path.join('data', 'data.json'), 'r', 'utf-8')
		with fp_o:
			self.data_o = json.load(fp_o)
		return self.data_o

	def saveData_p(self):
		with codecs.open(os.path.join('data', 'data.json'), 'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o, indent = 3)





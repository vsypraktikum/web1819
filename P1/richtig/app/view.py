# coding: utf-8

import mako
import codecs
import os.path
import string
from mako import template
from mako.lookup import TemplateLookup

# ----------------------------------------------------------
class View_cl(object):
# ----------------------------------------------------------
	
    # -------------------------------------------------------
    def __init__(self):
    # -------------------------------------------------------
        pass
    
    # -------------------------------------------------------
    def createstart_px(self):
    # -------------------------------------------------------
        return self.readFile_p('index.html')
    
    # -------------------------------------------------------
    def createKundeList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['kunde']['list']
        template_o = template.Template(self.readTemplate_p('kunden_list.tpl'))
        return template_o.render(data_o = data_opl)  
 
    def createKundeForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        template_o = template.Template(self.readTemplate_p('kunden_form.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl)

    def createMitarbeiterList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['mitarbeiter']['list']
        template_o = template.Template(self.readTemplate_p('mitarbeiter_list.tpl'))
        return template_o.render(data_o = data_opl)  
 
    def createMitarbeiterForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        template_o = template.Template(self.readTemplate_p('mitarbeiter_form.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl)

    def createProjektList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['projekt']['list']
        template_o = template.Template(self.readTemplate_p('projekt_list.tpl'))
        return template_o.render(data_o = data_opl)  

    def createProjektForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        template_o = template.Template(self.readTemplate_p('projekt_form.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl)



    def readFile_p(self, fileName_spl):
    # -------------------------------------------------------   
        content_s = ''

        with codecs.open(os.path.join('static', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
            
        return content_s
    
    # -------------------------------------------------------
    def readTemplate_p(self, fileName_spl):
    # -------------------------------------------------------   
        content_s = ''
    
        with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
                
        return content_s
        
    

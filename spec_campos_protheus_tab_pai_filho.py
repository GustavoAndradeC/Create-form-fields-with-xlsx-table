#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

import matplotlib.pyplot as plt


# In[5]:


def type_textarea(row):
    campo = str(row["campo"]).strip()
    tamanho = str(row["tamanho"]).strip()
    titulo_pt = str(row["titulo_pt"]).strip()
    titulo_en = str(row["titulo_en"]).strip()
    titulo_es = str(row["titulo_es"]).strip()
    opcoes = str(row["opcoes"]).strip()
    
    linha = opcoes.split("=")[1]
    
    #Test if this field is mandatory
    if (row["obrigatorio_adc"] == 'S'):
        obrigatorio = "<strong>*</strong>"
    else:
        obrigatorio = ""
    
    #Used to add label options to properties file
    i18n_file('new',campo,titulo_pt,titulo_en,titulo_es) 
    
    
    tag_textarea = '''
                            <td style="padding: 2px 1px;">
                              <textarea class="form-control" rows="'''+linha+'''" id="'''+campo+'''" name="'''+campo+'''" maxlength="'''+ tamanho  +'''" style="resize: none;"></textarea>
                            </td>'''
    return tag_textarea


# In[6]:


def type_zoom(row):
    campo = str(row["campo"]).strip()
    tamanho = str(row["tamanho"]).strip()
    px_width   = str(row["px_width"]).strip()
    titulo_pt = str(row["titulo_pt"]).strip()
    titulo_en = str(row["titulo_en"]).strip()
    titulo_es = str(row["titulo_es"]).strip()
    opcoes = str(row["opcoes"]).strip()
    
    #Test if this field is mandatory
    if (row["obrigatorio_adc"] == 'S'):
        obrigatorio = "<strong>*</strong>"
    else:
        obrigatorio = ""
    
    #Used to add label options to properties file
    i18n_file('new',campo,titulo_pt,titulo_en,titulo_es)    
    
    #Join the information into a tag
    tag_zoom = '''
                            <td style="padding: 2px 1px;width:'''+ px_width  +'''px;">
                                <input type="zoom" class='col-xs-12 col-sm-12 col-md-12' id="'''+campo+'''" name="'''+campo+'''" style="width:'''+ px_width  +'''px;" data-zoom="'''+opcoes+'''"/>
                            </td>'''
    
    return tag_zoom


# In[7]:


def type_input(row):
    campo     = str(row["campo"]).strip()
    tamanho   = str(row["tamanho"]).strip()
    px_width   = str(row["px_width"]).strip()
    titulo_pt = str(row["titulo_pt"]).strip()
    titulo_en = str(row["titulo_en"]).strip()
    titulo_es = str(row["titulo_es"]).strip()
    tipo_cp   = str(row["tipo"]).strip()
    editavel  = str(row["editavel_adc"]).strip()
    
    
    #Test if this field is mandatory
    if (row["obrigatorio_adc"] == 'S'): #TODO
        obrigatorio = "<strong>*</strong>"
    else:
        obrigatorio = ""
    
    #Used to add label options to properties file
    i18n_file('new',campo,titulo_pt,titulo_en,titulo_es)
    
    #Join the information into a tag
    tag_text = ''
    if tipo_cp:
        tag_text = '''
                            <td style="padding: 2px 1px;">
                                <input type="'''+ tipo_cp  +'''" name="'''+ campo  +'''" id="'''+ campo  +'''" class="form-control" style="width:'''+ px_width  +'''px;"  maxlength="'''+ tamanho  +'''" '''+ ('readonly' if editavel == 'N' else '') + '''>
                            </td>
        '''
    return tag_text


# In[8]:


def type_select(row):
    campo = str(row["campo"]).strip()
    tamanho = str(row["tamanho"]).strip()
    px_width   = str(row["px_width"]).strip()
    titulo_pt = str(row["titulo_pt"]).strip()
    titulo_en = str(row["titulo_en"]).strip()
    titulo_es = str(row["titulo_es"]).strip()
    opcoes = str(row["opcoes"])
    
    #Test if this field is mandatory
    if (row["obrigatorio_adc"] == 'S'):
        obrigatorio = "<strong>*</strong>"
    else:
        obrigatorio = ""
    
    #Used to add label options to properties file
    i18n_file('new',campo,titulo_pt,titulo_en,titulo_es)
     
    #Add all the options of select item
    options = ""
    options_select_arr = opcoes.split("|")
    for idx,opt in enumerate(options_select_arr):
        value = opt.strip().split("=")
        tag_opt= campo+"_SLCT_"+str(idx)
        #Add options label's to properties file
        i18n_file('new',tag_opt,value[1],'','')
        options += '''          
                                    <option value="'''+ value[0] +'''">i18n.translate("'''+ tag_opt +'''")</option>'''
        
    #Join the information into a tag
    tag_select = '''
                            <td style="padding: 2px 1px;width:'''+ px_width  +'''px;">
                                <select class='form-control' name="'''+ campo +'''" id="'''+ campo +'''">
                                    <option></option>'''+ options +'''
                                </select>
                            </td>
    '''
    return tag_select    


# In[9]:


i18n_file_dict_pt = {}
i18n_file_dict_en = {}
i18n_file_dict_es = {}
def i18n_file(arg, cod, title_pt, title_en, title_es):
    if arg == 'create':
        file_pt = open("pt_BR.properties","w",encoding='utf-8')
        file_en = open("en_US.properties","w",encoding='utf-8')
        file_es = open("es.properties","w",encoding='utf-8')
        for key in i18n_file_dict_pt:
            title_pt = i18n_file_dict_pt[key]
            str_pt = key + '=' +  title_pt + '\n'
            file_pt.write(str_pt)
            
            
            title_en = i18n_file_dict_en[key]
            if(title_en == '' or title_en == 'nan' ):
                title_en = title_pt                
            str_en = key + '=' +  title_en + '\n'
            file_en.write(str_en)
            
            title_es = i18n_file_dict_es[key]
            if(title_es == '' or title_es == 'nan' ):
                title_es = title_pt  
            str_es = key + '=' +  title_es + '\n'
            file_es.write(str_es)            
        file.close()
        return 
    elif arg == 'new':
        i18n_file_dict_pt[cod] = title_pt
        i18n_file_dict_en[cod] = title_en
        i18n_file_dict_es[cod] = title_es
        return
    else:
        return        


# In[10]:


def write_array_to_file(file, array, name):
    file.write('var '+name+' = [')
    auxiliar=1
    length=len(array)
    for item in array:
        if(auxiliar == length):
            file.write('"'+item+'"')
        else:
            file.write('"'+item+'", ')
        if(auxiliar%10 == 0 and auxiliar!=length):
            file.write('//'+str(auxiliar)+'\n')
        auxiliar+=1
        
    file.write(']; //'+str(auxiliar-1)+'\n\n')


# In[11]:


def generate_javascript():
      
    obrigatorio_arr = []
    oculto_arr = []
    visivel_arr = []
    editavel_arr = []  
    integravel_arr = []
    salva_fluig_arr = []
    
    
    for index, row in data_frame.iterrows():
        campo = str(row["campo"]).strip()
        
        if(row["obrigatorio_adc"]=='S'):
            obrigatorio_arr.append(campo)
        if(row["oculto_adc"]=='S'):
            oculto_arr.append(campo)
        else:
            visivel_arr.append(campo)
        if(row["editavel_adc"]=='S'):
            editavel_arr.append(campo)
        if(row["fluig_salva"]=='S'):
            salva_fluig_arr.append(campo)
        if(row["integracao"]=='S'):
            integravel_arr.append(campo)

    file = open("arraysCampos.js","w")
    
    write_array_to_file(file,visivel_arr,'arraysCamposVisivel')
    write_array_to_file(file,oculto_arr,'arraysCamposOculto')
    write_array_to_file(file,obrigatorio_arr,'arraysCamposObr')
    write_array_to_file(file,salva_fluig_arr,'arraysCamposFluig')
    write_array_to_file(file,editavel_arr,'arraysCamposEditavel')
    write_array_to_file(file,integravel_arr,'arraysCamposIntegravel')        
  
    file.close()      


# In[12]:


#Read CSV with the data
#data_frame = pd.read_csv("spec_campos_root.csv", sep=";",encoding='utf-8')

#Generate JavaScript Files
#generate_javascript()

def thead_label(row):
    campo     = str(row["campo"]).strip()
   # tamanho   = str(row["tamanho"]).strip()
    titulo_pt = str(row["titulo_pt"]).strip()
    titulo_en = str(row["titulo_en"]).strip()
    titulo_es = str(row["titulo_es"]).strip()
    tipo_cp   = str(row["tipo"]).strip()
    #editavel  = str(row["editavel_adc"]).strip()
    
    
    #Test if this field is mandatory
    if (row["obrigatorio_adc"] == 'S'): #TODO
        obrigatorio = "<strong>*</strong>"
    else:
        obrigatorio = ""
    
    #Used to add label options to properties file
    i18n_file('new',campo,titulo_pt,titulo_en,titulo_es)
    
    #Join the information into a tag
    tag_text = ''
    if tipo_cp:
        tag_text = '''  
                            <td style="padding: 2px 1px;"><label for="'''+ campo  +'''" id="'''+ campo  +'''_L"><strong>i18n.translate("'''+ campo  +'''")</strong>'''+ obrigatorio +'''</label></td>'''
    return tag_text

# In[13]:


inicio = '''
<html>
    <body>
    <form name="form" role="form">'''

final = '''
    </body>
    </form>
</html>'''

#Create HTML file
file = open("sample.html","w")
#file.write(inicio)

#Read CSV with the data
data_frame = pd.read_csv("spec_campos_protheus_tab_pai_filho.csv", sep=";",encoding='utf-8')

#Generate JavaScript Files
generate_javascript()

#Generate HTML file
#Iterate over folders
for idx,folder in enumerate(data_frame.aba.unique()):
    #Used to add label options to properties file
    folder_label='FOLDER_'+str(idx)
    i18n_file('new',folder_label,str(folder).strip(),"","")
    tag_init_folder='''
    
        <!--***************************** ''' + str(folder).strip().upper() + ''' ********************************-->
        <div class="panel" id="p-quad-ativ">
            <div class="panel-heading collapsible-nblue" id="cabecalho">
                <h3 style="color:#ffffff;margin:0px 0px;" id="txt_obrig">
                    <strong>i18n.translate("'''+folder_label+'''")</strong>
                </h3>
            </div>

            <div class="panel-body">
                <table tablename="tb_indic_produto" id="tb_indic_produto" class="table table-hover" noaddbutton="true" nodeletebutton="true">'''
    file.write(tag_init_folder)
    
    
    
    df_folder = data_frame.loc[data_frame['aba'] == folder]    
    
    #Iterate over sections 
    #INICIO DA LISTA THEAD DA TABLE 
    for idx_section,section in enumerate(df_folder.secao.unique()):
        
        if(str(section).strip() != '' and str(section).strip() != '--'):
            #Used to add label options to properties file
            section_label='FOLDER_'+str(idx)+'_SECTION_'+str(idx_section)
            i18n_file('new',section_label,str(section).strip(),"","")
            tag_secao='''
                <div class="row">
                    <h5>i18n.translate("'''+section_label+'''")</h5>
                </div>
            '''
            file.write(tag_secao)
            
        df_section = df_folder.loc[data_frame['secao'] == section]
    
        #Iterate over rows
        for line in df_section.linha.unique():
            tag_init_row='''
                    <thead>
                        <tr class='row'>'''
            file.write(tag_init_row)
            df_line = df_section.loc[data_frame['linha'] == line]

            #Iterate over items
            for index, row in df_line.iterrows():
                tag_element = thead_label(row)
                
                file.write(tag_element)
            tag_end_row='''
                        </tr>
                    </thead>'''
            file.write(tag_end_row)
    
    #FIM DA LISTA THEAD DA TABLE
    
    #INICIO DA LISTA TBODY DA TABLE
    #Iterate over sections
    for idx_section,section in enumerate(df_folder.secao.unique()):
        
        if(str(section).strip() != '' and str(section).strip() != '--'):
            #Used to add label options to properties file
            section_label='FOLDER_'+str(idx)+'_SECTION_'+str(idx_section)
            i18n_file('new',section_label,str(section).strip(),"","")
            tag_secao='''
                    <div class="row">
                        <h5>i18n.translate("'''+section_label+'''")</h5>
                    </div>
            '''
            file.write(tag_secao)
            
        df_section = df_folder.loc[data_frame['secao'] == section]
    
        #Iterate over rows
        for line in df_section.linha.unique():
            tag_init_row='''
                    <tbody>
                        <tr class='row'>'''
            file.write(tag_init_row)
            df_line = df_section.loc[data_frame['linha'] == line]

            #Iterate over items
            for index, row in df_line.iterrows():
                if (row["tipo"].strip() == 'select'):
                    tag_element = type_select(row)
                elif (row["tipo"].strip() == 'zoom'):
                    tag_element = type_zoom(row)
                elif (row["tipo"].strip() == 'textarea'):
                    tag_element = type_textarea(row)
                else:
                    tag_element = type_input(row)
                

                file.write(tag_element)
            tag_end_row='''
                        </tr>
                    </tbody>'''
            file.write(tag_end_row)
      #INICIO DA LISTA TBODY DA TABLE
    tag_end_folder='''
                </table>
            </div>
        </div>'''
    file.write(tag_end_folder)

#file.write(final)
file.close()
i18n_file('create','','','','')


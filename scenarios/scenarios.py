# -*- coding: utf-8 -*-


# Errores del modelo
import random
import services.services_gen as SN
import scenarios.finder as finder

datasheet_config=""
new_index =0

def add_scenario(datasheet,IQ,selected_scenarios,service_name: SN.ServiceNAME,datasheet_two):
    datasheet_config = datasheet
  
    current_sce =0 
    if selected_scenarios != []:
        for scenario in selected_scenarios:
            if scenario=="F-O":
                      add_Falso_Opcional(datasheet_config, service_name)
            if scenario=="S-D":
                 add_Auto_Dependencia(datasheet_config,service_name)
#            if scenario=="VPV":
#                 add_Auto_Dependencia(datasheet_config,service_name)
#                 
            #INCONSISTENCIAS
            if scenario=="C-C":
                 add_constraint_contradiction(datasheet_config,service_name)
            if scenario=="A-I":
                   add_alternative_inclusion(datasheet_config,service_name)
            if scenario=="M-E":
                 add_mandatory_exclude(datasheet_config,service_name)
            if scenario=="P-E":
                 add_Auto_Dependencia(datasheet_config,service_name)
            if scenario=="T-I":
                 add_transitive_inconsistency(datasheet_config,service_name) 
                 
            #Redundancias 
            if scenario=="M-I":
                   add_mandatory_include(datasheet_config,service_name)
            if scenario=="A-E":
                add_alternative_exclude(datasheet_config,service_name)
            if scenario=="P-I":
               add_Parent_inclusion(datasheet_config,service_name)
            if scenario=="T-R":
                   add_alternative_exclude(datasheet_config,service_name)
     
            # Scope (Ss)
            
            if scenario=="F-SVP":             
                falso_Specific(datasheet_config,service_name)
            if scenario=="M-SVP":              
                mandatory_Specific(datasheet_config)
            
            # Alcances Contradictorios (C-S) R Modificar a SVP
            # Falso Global (F-GVP) R Modificar a SVP
            # =============================================================================
            #Dependencia Cruzada (CDs)
            # =============================================================================
            # Redundancia Cruzada (C-R) W -
            # Inconsistencia Cruzada (C-I)
            #         
            # 
            # =============================================================================
                    
                    
        
        

        
        
        
    
    while current_sce <IQ:
        random_select = random.randint(0, 12)
#        random_select = 3
        
        if random_select ==0:
            add_Falso_Opcional(datasheet_config, service_name)
        if random_select==1:  
            add_Auto_Dependencia(datasheet_config,service_name)
        
        #servicios muertos 
        if random_select==2:   
           add_constraint_contradiction(datasheet_config,service_name)
        if random_select==3:   
           add_alternative_inclusion(datasheet_config,service_name)
        if random_select==4:
            add_mandatory_exclude(datasheet_config,service_name)
        if random_select==5:   
            add_Parent_exclude(datasheet_config,service_name)
        if random_select==5:   
            add_transitive_inconsistency(datasheet_config,service_name) 
        #redundancias
        if random_select==7:   
            add_mandatory_include(datasheet_config,service_name)
        if random_select==8:   
            add_Parent_inclusion(datasheet_config,service_name)
        if random_select==9:   
           add_alternative_exclude(datasheet_config,service_name)
        if random_select==10:   
           add_alternative_exclude(datasheet_config,service_name)
        if random_select==11:              
            falso_Specific(datasheet_config,service_name)
        if random_select==12:              
            mandatory_Specific(datasheet_config)
           
        current_sce = current_sce +1
    return datasheet_config



def add_Falso_Opcional(datasheet_config, service_name: SN.ServiceNAME):
    AD_config =""
    name_service=""
    mandatory_name_service=""
    list_mandatory=[]
    all_services = service_name.service_in_use
    list_mandatory=finder.find_mandatory_list(datasheet_config)
    if list_mandatory!=[]:
               
        
        random_index = random.randint(0, len(list_mandatory)-1)
        mandatory_name_service=list_mandatory[random_index]
        all_services =  finder.diff(all_services,list_mandatory) 
        random_index = random.randint(0, len(all_services)-1)
        name_service=all_services[random_index]
      
        
        AD_config= {"requires": {"service": {"name": name_service}}}
        print("---------")
        print("Agregando Falso Opcionalpara: ",name_service)
        print(AD_config)
        print("---------")
        finder.add_extra_scenario(datasheet_config,mandatory_name_service,AD_config)

def add_Auto_Dependencia(datasheet_config, service_name: SN.ServiceNAME):
    parent_service = service_name.get_service_in_use()
    
    AD_config =""
    random_select = random.randint(0, 10)
    if random_select<6:
           AD_config= {"excludes": {"service": {"name": parent_service}}}
    else:
        AD_config= { "requires": {"service": {"name": parent_service}}}
    print("---------")
    print("Agregando auto dependencia para: ",parent_service)
    print(AD_config)
    print("---------")
    finder.add_extra_scenario(datasheet_config,parent_service,AD_config)

def add_Violaciones_PV():
    return ""


# Servicios Muertos

def add_constraint_contradiction(datasheet_config, service_name: SN.ServiceNAME):
    parent_service = service_name.get_service_in_use()
    AD_config =""
    name_service = service_name.get_service_name_dependency()
    AD_config= {"requires": {"service": {"name": name_service,
                                         "excludes": {"service": {"name": parent_service}}
                                         }}}
     
    print("---------")
    print("Agregando constraint contradiction para: ",parent_service)
    print(AD_config)
    print("---------")
    finder.add_extra_scenario(datasheet_config,parent_service,AD_config)

def add_alternative_inclusion(datasheet_config, service_name: SN.ServiceNAME):
    global new_index
    cant_alt_vp= str(datasheet_config).count("AlternativeVP")
    if cant_alt_vp == 0:
        print ("no existe aleatoreo")
    else:
        num_vp = random.randint(1,cant_alt_vp)
        
        new_index =num_vp
        list_services_vp = finder.find__alt_vp(datasheet_config)
        if list_services_vp!=[]:
            parent_service=list_services_vp[0]
            name_service = list_services_vp[random.randint(1,len(list_services_vp)-1)]
            AD_config= {"requires": {"service": {"name": name_service}}}
        
            print("---------")
            print("Agregando alternative inclusion para: ",parent_service)
            print(AD_config)
            print("---------")
            
            finder.add_extra_scenario(datasheet_config,parent_service,AD_config)
    

def add_mandatory_exclude(datasheet_config, service_name: SN.ServiceNAME):
    AD_config =""
    name_service=""
    mandatory_name_service=""
    list_mandatory=[]
    name_service = service_name.get_service_in_use()
    list_mandatory=finder.find_mandatory_list(datasheet_config)
    if list_mandatory!=[]:
               
        
        random_index = random.randint(0, len(list_mandatory)-1)
        mandatory_name_service=list_mandatory[random_index]
      
        
        AD_config= {"excludes": {"service": {"name": mandatory_name_service}}}
        print("---------")
        print("Agregando Mandatory Exclude para: ",name_service," con ", mandatory_name_service)
        print(AD_config)
        print("---------")
        finder.add_extra_scenario(datasheet_config,name_service,AD_config)


def add_Parent_exclude(datasheet_config, service_name: SN.ServiceNAME):
    AD_config =""
    find_service=True
    name_service=""
    parent_name_service=""
    list_parents=[]
    while find_service:
        name_service = service_name.get_service_in_use()
        list_parents=finder.find_parent_list(datasheet_config,name_service)
        
        if list_parents!=[]:
            find_service=False
    
    random_index = random.randint(0, len(list_parents)-1)
       
    parent_name_service=list_parents[random_index]
  
    
    AD_config= {"excludes": {"service": {"name": parent_name_service}}}
    print("---------")
    print("Agregando Parent Exclude para: ",name_service," con ", parent_name_service)
    print(AD_config)
    print("---------")
    finder.add_extra_scenario(datasheet_config,name_service,AD_config)
   
    

def add_transitive_inconsistency(datasheet_config, service_name: SN.ServiceNAME):
    parent_service = service_name.get_service_in_use()
    service1= service_name.get_service_in_use()
    service2 = service_name.get_service_in_use()
    AD_config =""
    
    AD_config= {"requires": {"service":{"name": service1,
                                         "requires": {"service": {"name": service2}}}  }}
    finder.add_extra_scenario(datasheet_config,parent_service,AD_config) 
    
    AD_config= {"excludes": {"service":{"name": service2  }}}
    finder.add_extra_scenario(datasheet_config,parent_service,AD_config)                                  
     
    print("---------")
    print("Agregando transitive Inconsistency para: ",parent_service)
    print(AD_config)
    print("---------")
   

# Redundancias
def add_mandatory_include(datasheet_config, service_name: SN.ServiceNAME):
    AD_config =""
    name_service=""
    mandatory_name_service=""
    list_mandatory=[]
    name_service = service_name.get_service_in_use()
    list_mandatory=finder.find_mandatory_list(datasheet_config)
    if list_mandatory!=[]:
               
        
        random_index = random.randint(0, len(list_mandatory)-1)
        mandatory_name_service=list_mandatory[random_index]
      
        
        AD_config= {"requires": {"service": {"name": mandatory_name_service}}}
        print("---------")
        print("Agregando Mandatory Includes para: ",name_service," con ", mandatory_name_service)
        print(AD_config)
        print("---------")
        finder.add_extra_scenario(datasheet_config,name_service,AD_config)



def add_Parent_inclusion(datasheet_config, service_name: SN.ServiceNAME):
    AD_config =""
    find_service=True
    name_service=""
    parent_name_service=""
    list_parents=[]
    while find_service:
        name_service = service_name.get_service_in_use()
        list_parents=finder.find_parent_list(datasheet_config,name_service)
       
        if list_parents!=[]:
            find_service=False
    
    random_index = random.randint(0, len(list_parents)-1)
       
    parent_name_service=list_parents[random_index]
  
    
    AD_config= {"requires": {"service": {"name": parent_name_service}}}
    print("---------")
    print("Agregando Parent Inclusion para: ",name_service," con ", parent_name_service)
    print(AD_config)
    print("---------")
    finder.add_extra_scenario(datasheet_config,name_service,AD_config)
   


def add_alternative_exclude(datasheet_config, service_name: SN.ServiceNAME):
    global new_index
    cant_alt_vp= str(datasheet_config).count("AlternativeVP")
    if cant_alt_vp == 0:
        print ("no existe aleatoreo")
    else:
        num_vp = random.randint(1,cant_alt_vp)
        
        new_index =num_vp
        list_services_vp = finder.find__alt_vp(datasheet_config)
        if list_services_vp!=[]:
            parent_service=list_services_vp[0]
            name_service = list_services_vp[random.randint(1,len(list_services_vp)-1)]
            AD_config= {"excludes": {"service": {"name": name_service}}}
        
            print("---------")
            print("Agregando alternative excludes para: ",parent_service)
            print(AD_config)
            print("---------")
            
            finder.add_extra_scenario(datasheet_config,parent_service,AD_config)

def add_transitive_redundancy(datasheet_config, service_name: SN.ServiceNAME):
    parent_service = service_name.get_service_in_use()
    service1= service_name.get_service_in_use()
    service2 = service_name.get_service_in_use()
    AD_config =""
    
    AD_config= {"requires": {"services":[{"name": service1,
                                         "requires": {"service": {"name": service2}}},
                                         {"name": service2}
                                            ]}}
     
    print("---------")
    print("Agregando transitive redundancy para: ",parent_service)
    print(AD_config)
    print("---------")
    finder.add_extra_scenario(datasheet_config,parent_service,AD_config)



#Scope 
def falso_Specific(datasheet_config, service_name: SN.ServiceNAME):
    parent_service = service_name.get_service_in_use()
    service1= service_name.get_service_name()
    service2= service_name.get_service_name()
    service3= service_name.get_service_name()
   
    AD_config= {"requires": {"service": {"name": service1,
                                         "GlobalVariationPoint": {
                                                 "OptionalVP": {
                                                  "service": [
                                                          {"name": service2,      
                                                           "GlobalVariationPoint": {"OptionalVP": {"service": [{"name": service3}]}}
                                                           }]
                                         }}}}}
    
    print("---------")
    print("Agregando falso_Specific ")
    print(AD_config)
    print("---------")
    finder.add_extra_scenario(datasheet_config,parent_service,AD_config)
    
  
def mandatory_Specific(datasheet_config):
    cant_vp= str(datasheet_config).count("MandatoryVP")
    if cant_vp == 0:
        print ("no es posible aplicar escenario")
    else:
        
        print(cant_vp)
        num_vp = random.randint(1,cant_vp)
        print(num_vp)
        
      
        finder.change_mand_vp(datasheet_config,num_vp)
       
        print("---------")
        print("Agregando Mandatory Specific ")
        print("---------")
        
            


def Alcances_Contradictorios(datasheet_config,service_name,dataseheet_config_two): 
    return ""
def falso_Global():
    return ""

#Dependencia Cruzada 
def redundancia_Cruzada():
    return ""
def inconsistencia_Cruzada():
    return ""


# =============================================================================
# 
# =============================================================================
#datashet = {"id": "Model_Name", 
# "service": {
#         "name": "A", 
#         "GlobalVariationPoint": {
#                 "MandatoryVP": {
#                         "service": [{
#                                 "name": "B", 
#                                 "GlobalVariationPoint": {
#                                         "OptionalVP": {
#                                                 "service": [{
#                                                         "name": "B1", "requires": {"Service": {"name": "B1"}}}]}}, 
#                                 "requires": {"service": {"name": "E"}}, 
#                                 "excludes": {"Service": {"name": "C"}}}, {"name": "C", "GlobalVariationPoint": {"VariantVP": {"service": [{"name": "C1", "requires": {"Service": {"name": "C1"}}}, {"name": "C2"}]}}, "excludes": {"service": {"name": "A"}}, "requires": {"service": {"name": "C1", "requires": {"Service": {"name": "C1"}}}}}]}}, "requires": {"service": {"name": "A"}}, "excludes": {"service": {"name": "B", "excludes": {"Service": {"name": "C"}}}}}} 
#

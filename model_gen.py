# -*- coding: utf-8 -*-
import random

import relationship.relationship as rel
import scenarios.scenarios as sce 
import services.services_gen as SN
import generator_log as GL


service_name = SN.ServiceNAME
SQ = 0
RC = 0
MP = 0
IQ = 0
currentMP = 1
currentRC = 0



def add_service(simpleService, parent_name=""):
    
    
    
    service_config= add_service_config(simpleService, parent_name)
    
    service= {"service": service_config }
    
    return service

def add_service_config(simpleService, parent_name=""):
    name= service_name.get_service_name(parent_name)
    
    #------- log -------
    gen_log =  GL.generator_log(True) 
    log= 'Addig service ' + name
    gen_log.console_log(log)
    
    #-------------------
    
    
    service_config= {"name": name}
    
    if (simpleService==False):
        vp = add_VP(name)
        service_config.update(vp)
        random_select = random.randint(1, 10)
        if  random_select<=7:
           dependency = add_dependency(name)
           service_config.update(dependency)
    return service_config

def add_service_config_dependency(simpleService):
    name= service_name.get_service_name_dependency()
    
    service_config= {"name": name}
    
    return service_config
    

def add_VP(parent_name):
    global currentMP 
   

    vp_scope= rel.get_SCOPE()
    vp_type= rel.get_VP_Type()
    
    cant_child = rel.get_cant_child(vp_type)
   
    list_service=[]
    simple_Child = False
    if currentMP<MP:
        simple_Child = False
        currentMP = currentMP + 1
    else:
        simple_Child = True
      
        
    for x in range(cant_child):
        service=add_service_config(simple_Child,parent_name)
        list_service.append(service)

    service_config = {"service":list_service}
    
    vp_type_config ={vp_type: service_config }
    
    vp = { vp_scope : vp_type_config}
    
    return vp

def add_dependency(parent_name,dependency_type=""):
#    sce_config = sce.add_constraint_contradiction(service_name,parent_name)
    
   
    global currentRC
   
    dependency_config=""
    if  currentRC < RC: 
        currentRC = currentRC +1
        service=add_service_config_dependency(True)
        if dependency_type=="":
            dependency_type= rel.get_Dependency_Type()
        dependency_config= {dependency_type:{"service":service}}

        #------- log -------
        gen_log =  GL.generator_log(True) 
        log= 'Addig dependency ' + parent_name +' '+dependency_type+' '+ str(service)
        gen_log.console_log(log)
        #-------------------



    return dependency_config
#    return sce_config
    
def add_dependency_to_service(service):
    
    dependency=""
    if "requires" in service.keys() or "excludes" in service.keys():
       if "requires" in service.keys():
           dependency=add_dependency("","excludes")    
       elif "excludes" in service.keys():
           dependency=add_dependency("","requires")    
      
    else:
         dependency=add_dependency("")
           
      
       
    service.update(dependency)
    return service
   

def add_extra_dependency(datasheet):

    s_name = service_name.get_service_in_use()
    service = datasheet.get("service") 
    find_service(service,s_name)
   
def find_service(service,name):
    data=""
    is_find = True
    name_ser= service.get("name")
    if name_ser==name:
        data=service
        add_dependency_to_service(service)
       
        
        is_find=False
    if is_find:
       for key in  service.keys():
            if key != "name": 
                config=service.get(key)
                find_service_config(config,name)
 
    return data

def find_service_config(config,name):
    
     for key in  config.keys():
            if key == "service": 
                service=config.get("service")
                find_service(service,name)
            else: 
                list_services = config.get(key).get("service")
                for service in list_services:
                   find_service(service,name)



def check_RC(datasheet,RC):
    global currentRC
 
    while currentRC < RC:
#        print("RC =",RC)
#        print("current RC =",currentRC)
        add_extra_dependency(datasheet)





def create_single_datasheet(SQ_val,RC_val,MP_val,IQ_val,selected_scenarios,ID_dat):
    

    gen_log =  GL.generator_log(True) 
    gen_log.console_log('Create a single datasheet')
    
    
    global SQ, RC, MP , IQ, service_name
    SQ = SQ_val
    RC = RC_val
    MP = MP_val
    IQ = IQ_val
    
    
    gen_log.console_log('Create a Service Name service')
    log='Adding datasheet ID: ' + ID_dat
    gen_log.console_log(log)

    
    service_name = SN.ServiceNAME(SQ)
    
    datasheet= { "id": ID_dat}
    service = add_service(False)
    
    
    datasheet.update(service) 
    check_RC(datasheet,RC)
    
    if IQ >0 or selected_scenarios!=[] : 
        datasheet=sce.add_scenario(datasheet,IQ,selected_scenarios,service_name,[])
    
    return datasheet
    
    
    
    
#    
def create_multiple_datasheet(SQ_val,RC_val,MP_val,IQ_val,selected_scenarios):
    global SQ, RC, MP , IQ, service_name
    SQ = SQ_val
    RC = RC_val
    MP = MP_val
    IQ = IQ_val
   
    service_name = SN.ServiceNAME(SQ)
    
    datasheet= { "id": "Model_Name"}
    service = add_service(False)
    
    datasheet.update(service ) 
    check_RC(datasheet)
    
    service_name = SN.ServiceNAME(SQ)
    
    datasheet2= { "id": "Model_Name"}
    service2 = add_service(False)
    
    datasheet2.update(service2 ) 
    check_RC(datasheet2)
    
    
    
    if IQ >0 or selected_scenarios!=[] : 
        datasheet=sce.add_scenario(datasheet,IQ,selected_scenarios,service_name,datasheet2)

    return datasheet
    
    



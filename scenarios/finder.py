


new_index =0


# =============================================================================
# #
# =============================================================================

def add_extra_scenario(datasheet,s_name,config_scenario):

#    s_name = service_name.get_service_in_use()
    service = datasheet.get("service") 
    find_service(service,s_name,config_scenario)
   
def find_service(service,name,config_scenario):
    data=""
    is_find = True
    name_ser= service.get("name")
    if name_ser==name:
        data=service
        add_scenario_config(service,config_scenario)
       
        
        is_find=False
    if is_find:
       for key in  service.keys():
            if key != "name": 
                config=service.get(key)
                find_service_config(config,name,config_scenario)
 
    return data

def find_service_config(config,name,config_scenario):
    
     for key in  config.keys():
            if key == "service": 
                service=config.get("service")
                find_service(service,name,config_scenario)
            else: 
                list_services = config.get(key).get("service")
                if list_services:

                    for service in list_services:
                       find_service(service,name,config_scenario)

def add_scenario_config(service,config_scenario):
    
       
    service.update(config_scenario)
    return service
   


# =============================================================================
# 
# =============================================================================

def find__alt_vp(datasheet):
    
    service = datasheet.get("service") 
    list_services = find_vp(service)
    return list_services
   
def find_vp(service):
    list_service=[]
    for key in  service.keys():
            if key != "name" and key != "requires" and key != "excludes": 
                config=service.get(key)
                list_service=find_vp_config(config)
 
    return list_service

def find_vp_config(config):
    global new_index
    list_services=[]
    
    for key in  config.keys():
        if key == "AlternativeVP": 
            if new_index==1:
                list_services=get_name_services(config.get(key).get("service"))
              
            else:
                new_index=new_index-1
                list_aux_services = config.get(key).get("service")
                for service in list_aux_services:
                      if  list_services==[]:
                          list_services=find_vp(service)
                          
        else: 
           list_aux_services = config.get(key).get("service")
           for service in list_aux_services:
               if  list_services==[]:
                   list_services=find_vp(service)
    return list_services

def get_name_services(list_services):
    list_ser=[]
    for services in list_services:
        list_ser.append(services.get("name"))
    return list_ser

# =============================================================================
# 
# =============================================================================


def find_parent_list(datasheet,name):
    
    service = datasheet.get("service") 
    list_services = find_parent(service,name)
    if list_services !=[]:
        list_services.remove(name)
    return list_services
   
def find_parent(service,name):
  
    list_service=[]
    actual_name= config=service.get("name")
    is_find= True
    if actual_name== name:
        list_service=[name]
        is_find =False
    if is_find:
        for key in service.keys():
                if key != "name" and key != "requires" and key != "excludes": 
                    config=service.get(key)
                    list_service=find_parent_vp_config(config,name)
                    if list_service!=[]:
                       list_service.append(actual_name)
 
    return list_service

def find_parent_vp_config(config,name):
    global new_index
    list_services=[]
    is_find=True
    for key in  config.keys():
        if key == "AlternativeVP": 
            list_aux_services = config.get(key).get("service")
            for service in list_aux_services:
                if is_find:
                    if  list_services==[]:
                        list_services=find_parent(service,name)
                        if list_services != []:
                            is_find=False
                          
        else: 
           list_aux_services = config.get(key).get("service")
           for service in list_aux_services:
               if is_find:
                   if  list_services==[]:
                       list_services=find_parent(service,name)
                       if list_services != []:
                                is_find=False
    return list_services

# =============================================================================
# 
# =============================================================================



def find_mandatory_list(datasheet):
    
    service = datasheet.get("service") 
    list_services = find_mand(service)
    return list_services
   
def find_mand(service):
   
    list_service=[]
    actual_name= config=service.get("name")
    for key in service.keys():
        if key != "name" and key != "requires" and key != "excludes": 
            config=service.get(key)
            list_service=list_service + find_mand_config(config)
        if key == "requires": 
            config=service.get(key).get("service")
            list_service=list_service + find_mand(config)
               
    list_service.append(actual_name)
 
    return list_service

def find_mand_config(config):
    global new_index
    list_services=[]
   
    for key in  config.keys():
        if key == "MandatoryVP": 
            list_aux_services = config.get(key).get("service")
            for service in list_aux_services:
                list_services=list_services + find_mand(service)
                       
    return list_services


# =============================================================================
# 
    
# =============================================================================
  


def diff(list1, list2): 
    c = set(list1).union(set(list2)) 
   
    d = set(list1).intersection(set(list2))

    return list(c - d)
                        

# =============================================================================
# 
# =============================================================================




def change_mand_vp(datasheet,num_vp):
    global new_index
    new_index = num_vp
    service = datasheet.get("service") 
    list_services = find_mand_vp(service)
    return list_services
   
def find_mand_vp(service):
    global new_index
  
    band = False
    for key in  service.keys():
            if key != "name" and key != "requires" and key != "excludes": 
                config=service.get(key)
                band=find_mand_scope_config(config)
                if band and new_index!=-1:
                    if  key!="SpecificVariationPoint":
                
                       vp_aux={"SpecificVariationPoint":config}
                       service.pop("GlobalVariationPoint")
                       service.update(vp_aux)
                       band =False
                       new_index = -1
                       
                       
 
    return band

def find_mand_scope_config(config):
    global new_index
    band =False
    for key in  config.keys():
        if key == "MandatoryVP": 
            if new_index==1:
                band=True
              
            else:
                new_index=new_index-1
                list_aux_services = config.get(key).get("service")
                for service in list_aux_services:
                      if  band==False:
                          band=find_mand_vp(service)
                          
        else: 
           list_aux_services = config.get(key).get("service")
           for service in list_aux_services:
               if  band==False:
                   band=find_mand_vp(service)
                   
                   
    return band

# =============================================================================
# 
# =============================================================================


    
datashet = {"id": "Model_Name", 
  "service": {
         "name": "A", 
         "GlobalVariationPoint": {
                 "MandatoryVP": {
                         "service": [{
                                 "name": "B", 
                                 "GlobalVariationPoint": {
                                         "OptionalVP": {
                                                 "service": [{
                                                         "name": "B1", "requires": {"Service": {"name": "B1"}}}]}}, 
                                 "requires": {"service": {"name": "E"}}, 
                                 "excludes": {"Service": {"name": "C"}}}, {"name": "C", "GlobalVariationPoint": {"VariantVP": {"service": [{"name": "C1", "requires": {"Service": {"name": "C1"}}}, {"name": "C2"}]}}, "excludes": {"service": {"name": "A"}}, "requires": {"service": {"name": "C1", "requires": {"Service": {"name": "C1"}}}}}]}}, "requires": {"service": {"name": "A"}}, "excludes": {"service": {"name": "B", "excludes": {"Service": {"name": "C"}}}}}} 


#change_opt_vp(datashet,2)
#
#print(datashet)
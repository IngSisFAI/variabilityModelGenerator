# -*- coding: utf-8 -*-

import random


class ServiceNAME:
    def __init__(self,SQ):      
        self.service_name_list =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.service_name_subindex =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.service_in_use=[]
        self.service_name_index = 0
        self.service_quantity = SQ
    
    def get_service_name(self,name=""):
       
        service_name=""
       
    
        if (name == "" or name == "A"  or len(name)==2 ):
         
            service_name = self.service_name_list[self.service_name_index]
            self.service_name_index = self.service_name_index + 1 
        else:
            name_index= self.service_name_list.index(name)
            service_name = name+str(self.service_name_subindex[name_index])
            self.service_name_subindex[name_index] = self.service_name_subindex[name_index] + 1
          
        
        self.service_in_use.append(service_name)
        return service_name
    
    def get_service_name_dependency(self):
        service_name=""
        
        random_select=1
        if len(self.service_in_use)>0:
               random_select = random.randint(1, 10)
               
        if  random_select<=5:
            random_index = random.randint(0, len(self.service_name_list)-1)
            service_name=self.service_name_list[random_index]
        else:
            random_index = random.randint(0, len(self.service_in_use)-1)
           
            service_name=self.service_in_use[random_index]
            
        self.service_in_use.append(service_name)
        return service_name
    
    def get_service_in_use(self,name=""):
       service_name=""
       random_index = random.randint(0, len(self.service_in_use)-1)
       
       service_name=self.service_in_use[random_index]
       return service_name

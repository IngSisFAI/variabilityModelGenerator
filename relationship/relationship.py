# -*- coding: utf-8 -*-
import random

def get_SCOPE():
    
    scope_type= "GlobalVariationPoint" 
    scope_t = random.randint(1, 10)
    if  scope_t<=5:
        scope_type= "SpecificVariationPoint" 
    return scope_type

def get_Dependency_Type():
    DP_type= "requires" 
    dp_t = random.randint(1, 10)
    if  dp_t<=5:
         DP_type= "excludes"
    return DP_type

def get_VP_Type():
    VP_type= "MandatoryVP" 
    vp_t = random.randint(1, 4)
    if  vp_t==1:
        VP_type= "AlternativeVP" 
    elif  vp_t==2:
        VP_type= "OptionalVP" 
    elif  vp_t==3:
        VP_type= "VariantVP" 
    else:
        VP_type= "MandatoryVP" 
    return VP_type

def get_cant_child(vp_type):
    cant =0
    if (vp_type == "MandatoryVP"):
        cant = random.randint(1, 2)
    elif (vp_type == "OptionalVP"):
        cant = random.randint(1, 2)
    else:
        cant = random.randint(2, 4)
    return cant 


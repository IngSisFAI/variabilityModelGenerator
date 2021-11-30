# -*- coding: utf-8 -*-

class generator_log_Meta(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class generator_log(metaclass=generator_log_Meta):
    
    def __init__(self,console):      
        self.inconsistency_log=""
        self.count =1
        self.i_count =1
        self.console= console
    
    def console_log(self,log):
        
        if self.console :
            print(self.count , " " , log)
            self.count += 1
            
    
    def add_inconsistency_log(self,log,details):
        self.console_log("Adding Inconsistency")
        self.inconsistency_log = self.inconsistency_log + str(self.i_count) + ' ' + log +'\n' + str(details) +'\n'+'\n'
        self.i_count +=1

    def print_inc(self):
        print(self.inconsistency_log)
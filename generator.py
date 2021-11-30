
import model_gen
import json
import generator_log as GL

SQ = 30
RC = 5
MP = 4
IQ = 10


selected_scenarios=[]

gen_log =  GL.generator_log(True) 
ID_dat="Model_Name"

datasheetmodel = model_gen.create_single_datasheet(SQ,RC,MP,IQ,selected_scenarios,ID_dat)


print("----------------------------------------------------------------")
# print(json.dumps(datasheetmodel))


gen_log.print_inc()

print("----------------------------------------------------------------")
print(json.dumps(datasheetmodel))
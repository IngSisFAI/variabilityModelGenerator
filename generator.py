
import model_gen
import json
import generator_log as GL

SQ = 30
RC = 5
MP = 4
IQ = 10


selected_scenarios=[]

gen_log =  GL.generator_log(True) 
ID_dat="Test_example"

datasheetmodel = model_gen.create_single_datasheet(SQ,RC,MP,IQ,selected_scenarios,ID_dat)


print("----------------------------------------------------------------")


gen_log.print_inc()

print("----------------------------------------------------------------")
print(json.dumps(datasheetmodel))

test_dir ='.//testCases//'
name_json =test_dir+ID_dat+'.json'
with open(name_json, "w") as outfile:
    json.dump(datasheetmodel, outfile)
    
    
    
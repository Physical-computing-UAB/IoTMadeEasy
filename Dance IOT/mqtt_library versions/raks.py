import json
with open(r'C:/Users/Rakshit/Downloads/my11.json','r') as f:
    data = f.read()
data = data.replace("[]","",data.count("[]"))
data = data.replace("][",",",data.count("]["))
#data = data.replace("}\",\"{","},{",data.count("\",\""))
data = data.replace("[\"{","[{",data.count("[\"{"))
data = data.replace("}\"]","}]",data.count("}\"]"))
json_data = json.loads(data)
with open(r'C:/Users/Rakshit/Downloads/my11h.json','w') as outfile:
    json.dump(json_data,outfile)
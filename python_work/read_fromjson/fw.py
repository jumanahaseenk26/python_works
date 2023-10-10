from json import load
path="C:\\Users\\hp\\Desktop\\python_works\\read_fromjson\\data.json"
with open(path) as f:
    records=load(f)
#print(records)

fw_names=[f.get("name") for f in records]
print(fw_names)
#top rated frame work
top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

# frondend farame work names
frontend_fw=[f.get("name") for f in records if f.get("side")=="frontend"]
print(frontend_fw)

#python framework names
python_fw=[f.get("name") for f in records if f.get("language")=="python"]
print(python_fw)
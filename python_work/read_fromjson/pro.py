from json import load
path="C:\\Users\\hp\\Desktop\\python_works\\read_fromjson\\countries.json"
with open(path,encoding="utf-8")as f:
    countries=load(f)
print(len(countries))
#starts_with=[c.get("name") for c in countries if c.get("name").casefold().startswith("c")]
#print(starts_with)
name_capital=[[c.get("name"),c.get("capital")] for c in countries]
#print(name_capital)
c_with_border=[c for c in countries if "borders" in c]
max_border_country=max(c_with_border,key=lambda c:len(c.get("borders")))
#print(max_border_country)
india_border=[c.get("borders") for c in countries if c.get("name")=="india"]
#print(india_border)
depended_country=[c.get("name") for c in countries if c.get("independent")==False]
#print(depended_country)
popl_filter=[c.get("name") for c in countries if c.get("population")<400000]
print(popl_filter)

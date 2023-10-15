from sample.models import frameworks
#print(frameworks)
for fw in frameworks:
    if fw.get("language")=="python":
        print(fw.get("name"))
print([fw.get("name")for fw in frameworks if fw.get("language")=="python"])
print([fw.get("name")for fw in frameworks if fw.get("side")=="server"])
print([fw.get("name")for fw in frameworks if fw.get("rating")==4])
print([fw.get("name")for fw in frameworks if fw.get("language")=="python"])
top_rating=max(frameworks,key=lambda fw:fw.get("rating"))
print(top_rating)
less_rating=min(frameworks,key=lambda fw:fw.get("rating"))
print(less_rating)
frameworks.sort(key=lambda f:f.get("rating"),reverse=True)
print(frameworks)

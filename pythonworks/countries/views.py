from json import  load

with open("countrydata.json",encoding="UTF-8")as f:
    data=load(f)
    print(len(data))

all_country_name=[c.get("name")for c in data]
print(all_country_name)

def get_country_details(name):
    return [c for c in data if c.get("name")==name][0]
def get_country_capital(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("capital")
def get_country_population(name):
    c_data=get_country_details(name)
    if cdata:
        return c_data.get("population")

def get_country_currencyname(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("currencies")[0].get("name")
def get_country_borderlist(name):
    c_data=get_country_details(name)
    borders=c_data.get("borders")
    print(borders)
    b_name=[c.get("name")for c in data if c.get("alphacode")in borders]
    return b_names

#max_population_country=max(data,key=lambda c:c.get("population"))
#print(max_population_country)
def get_maxpopulation_country():
    c_data=max(data,key=lambda c:c.get("population"))
    return c_data.get("name")
def get_counntry_languages(name):
    c_data=get_country_details(name)
    return [l.get("name")for l in c_data.get("languages")]

print(get_counntry_languages("india"))


print(get_maxpopulation_country()

print(get_country_borderlist("sri lanka"))
print(get_country_currencyname("india"))
print(get_country_population("india")

print(get_country_capi-tal("pakistan"))

details=get_country_details("india")
print(details)






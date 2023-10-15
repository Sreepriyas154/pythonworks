from products.models import bikes

#list
#detal=>retrieve
#update
#create
#remove

class  Bikes:
    def list(self,*args,**kwargs):
        return bikes
    def retrieve(self,*args,**kwargs):
        code=(kwargs.get("code"))
        bike=[b for b in bikes if b.get("code")==code]
        return bike
    def create(self,*args,**kwargs):
        bike=kwargs.get("data")
        bikes.append(bike)
        return bike
    def update(self,*args,**kwargs):
        code=kwargs.get("code")
        bike=kwargs.get("data")
        instance=[b for b in bikes if b.get("code")==code][0]
        instance.update(data)
        return  instance
    def destory(self,*args,**kwargs):
        code=kwargs.get("code")
        instance=[b for b in bikes if b.get("code")==code]
        bike.remove(instance)
        return instance


b=Bikes()
print(b.list())
print(b.retrieve(code=1001))
data={"code": 1006, "name": "hunter350",
      "colors": ["red", "grey"],
      "price": 200000,"brand": "royalenfield",
      "fuel_type": "petrol"}
print(b.create(data=data))
print(b.list())
data=  {"code": 1002, "name": "hynes",
        "colors": ["red", "blue", "black"],
        "price": 240000, "brand": "honda",
        "fuel_type": "petrol"},
b.update(code=1002,data=data)
print(b.destory(code=1002))
class Vehicle:
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        self.is_available= True

    def sell(self):
        if self.is_available:
            self.is_available= False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No está disponible")
    
    def check_available(self):
        return self.is_available
    def get_price(self):
        return self.price
    def start_engine(self):
        raise NotImplementedError("Este Método debe ser implementado por la subclase")
    def stop_engine(self):
        raise NotImplementedError("Este Método debe ser implementado por la subclase")
class Car(Vehicle):
        def start_engine(self):
            if not self.is_available:
                return f"El motor del coche {self.brand} está en marcha"
            else:
                return f"El coche {self.brand} no está disponible"
            
        def stop_engine(self):
            if self.is_available:
                return f"El motor del coche {self.brand} se ha detenido"
            else:
                return f"El coche {self.brand} no está disponible"
class Bike(Vehicle):
        def start_engine(self):
            if not self.is_available:
                return f"La bicicleta {self.brand} está en marcha"
            else:
                return f"La bicicleta {self.brand} no está disponible"
            
        def stop_engine(self):
            if self.is_available:
                return f"La bicicleta {self.brand} se ha detenido"
            else:
                return f"La bicicleta {self.brand} no está disponible"
class Truck(Vehicle):
        def start_engine(self):
            if not self.is_available:
                return f"El motor del camión {self.brand} está en marcha"
            else:
                return f"El Camión {self.brand} no está disponible"
            
        def stop_engine(self):
            if self.is_available:
                return f"El motor del camión {self.brand} se ha detenido"
            else:
                return f"El camión {self.brand} no está disponible"
class Customer:
    def __init__(self, name):
        self.name=name
        self.purchased_vehicles=[]
    def buy_vehicle(self, vehicle : Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print("Lo siento, {vehicle.brand} no está disponible")
    def inquire_vehicle(self, vehicle : Vehicle):
        if vehicle.check_available():
            availability="Disponible"
        else:
            availability="No disponible"
        print(f"El vehiculo {vehicle.brand} esta : {availability} y cuesta :{vehicle.get_price()}")
class Dealership:
    def __init__(self):
        self.inventory=[]
        self.customers=[]
    def add_vehicles(self, vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehiculo {vehicle.brand} ha sido añadido al inventario")
    def register_customer(self, customer:Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido a la lista de clientes")
    def show_available_vehicle(self):
        print("vehiculos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"el vehiculo {vehicle.brand} por {vehicle.get_price()} esta disponible para la venta")
            #else:
                #print(f"el vehiculo {vehicle.brand} NO esta disponible para la venta")
car1= Car("Toyota","Corolla",20000)
bike1= Bike("Yamaha","Teneré 7000", 7000)
truck1= Truck("Volvo","FH16",80000)

customer1=Customer("Jorge Salazar")

dealership= Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#mostrar vehiculos disponibles:
dealership.show_available_vehicle()
# un cliente va consultar un vehiculo:
customer1.inquire_vehicle(car1)
# cliente compra vehiculo:
customer1.buy_vehicle(car1)
#mostrar vehiculos disponibles:
dealership.show_available_vehicle()
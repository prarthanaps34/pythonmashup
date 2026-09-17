class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        return "Vehicle ID: {}, Base Rate: {:.2f}".format(
            self._vehicle_id, self._base_rate
        )

    def rental_charge(self):
        return 0.0


class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self.num_seats


class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5


def calculate_rental(vehicle):
    return vehicle.rental_charge()


car1 = Car("CAR001", 100.00, 4)
bike1 = Bike("BIKE001", 100.00, "Scooter")

print(car1.display_details())
print("Number of seats:", car1.num_seats)
print("Car Rental Charge:", calculate_rental(car1))

print(bike1.display_details())
print("Bike Type:", bike1.bike_type)
print("Bike Rental Charge:", calculate_rental(bike1))


    
    
    
    
        
        
        
    
           
        
     

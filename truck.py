# The truck class for creating the three truck objects.
class Truck:
    # As to prevent redundancy, I defined these attributes here rather than when creating the 3 truck objects.
    t_speed = 18                       # All trucks have a speed of 18mph.
    t_address = "4001 South 700 East"  # The hub where all trucks start from.
    t_mileage = 0                      # Trucks begin the business day with 0 mileage.

    # Initializes all the truck attributes.
    # Truck package lists and departure time are initialized when creating the truck objects later.
    def __init__(self, t_packages, t_depart_time):
        self.truck_speed = Truck.t_speed
        self.truck_packages = t_packages
        self.truck_mileage = Truck.t_mileage
        self.truck_address = Truck.t_address
        self.truck_depart_time = t_depart_time
        self.truck_time = t_depart_time

    # Used to print truck attributes for debugging or other purposes.
    def __str__(self):
        return f"Speed: {self.truck_speed} | Address: {self.truck_address} | Packages: {self.truck_packages}"\
               f" | Mileage: {self.truck_mileage} | Depart: {self.truck_depart_time}"

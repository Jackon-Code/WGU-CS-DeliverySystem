# The class for representing packages and their data.
import datetime


class Package:
    # Initializes all the package attributes.
    def __init__(self, p_id, p_address: str, p_city: str, p_state: str, p_zip: str, p_deadline_time: str,
                 p_weight, p_status: str):
        # These attribute values will be read in from the csv file.
        self.package_ID = p_id
        self.package_address = p_address
        self.package_city = p_city
        self.package_state = p_state
        self.package_zip = p_zip
        self.package_deadline_time = p_deadline_time
        self.package_weight = p_weight
        # These attribute values will be updated later.
        self.package_status = p_status
        self.package_depart_time = None
        self.package_deliver_time = None
        # Used to update and correct package 9 at 10:20 as the initial address and zip are incorrect until then.
        self.package_updated_address = "410 S State St"
        self.package_updated_zip = "84111"
        self.package_update_time = datetime.timedelta(hours=10, minutes=20)

    # Updates the status of each package by comparing the users entered time to the trucks departure times + the
    # packages time of delivery.
    def determine_status(self, entered_time):
        # Corrects package 9 at 10:20 as required.
        if self.package_ID == 9 and entered_time < self.package_update_time:
            self.package_address = "300 State St"
            self.package_zip = "84103"
        # Conditional logic for determining if the package is still at the hub, en route, or delivered.
        if entered_time >= self.package_deliver_time:
            self.package_status = "Delivered"  # Package has been delivered.
        elif (entered_time >= self.package_depart_time) and (entered_time <= self.package_deliver_time):
            self.package_status = "En route"  # Package is in the process of being delivered.
        else:
            self.package_status = "At the Hub"
            # Package is still at the hub (or on its way to the hub in the case of the 'delayed in flight' packages)

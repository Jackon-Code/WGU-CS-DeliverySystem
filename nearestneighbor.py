# File used for holding the nearest neighbor algorithm.
import datetime

from csvoperations import fetch_packages_csv, read_distance, read_address
from hashtable import CreateHashTable

# Creates the hash table, and loads the packages into it.
hashtable_packages = CreateHashTable()
fetch_packages_csv("CSVfiles/WGUPS Package File.csv", hashtable_packages)


# The function that will be used to optimize the package delivery routes using the nearest neighbor algorithm.
def nearest_package_delivery(set_truck):
    global hashtable_packages  # Access the global hashtable_packages
    # Reads in the required distance and address data for later use in the distance comparisons below.
    distance_data = read_distance()
    address_data = read_address()
    # Begins by placing all the undelivered packages into a list.
    undelivered = [hashtable_packages.hash_lookup(package_ID) for package_ID in set_truck.truck_packages]

    # Clears the trucks currently unordered package list.
    set_truck.truck_packages.clear()

    # Iterates through the list one by one to find the nearest package before adding it to the truck.
    while len(undelivered) > 0:
        # Arbitrary value set above any possible distance so the loop will iterate properly.
        subsequent_address = 30
        subsequent_package = None
        # calculates the distance between the trucks current address and the packages address and then uses
        # this comparison to append the 'nearest' package to the trucks emptied list until the undelivered
        # list is empty and the trucks package list is reordered efficiently.
        for cur_package in undelivered:
            pack_address = None
            truck_address = None
            for csv_row in address_data:
                if cur_package.package_address in csv_row[2]:
                    pack_address = int(csv_row[0])
                if set_truck.truck_address in csv_row[2]:
                    truck_address = int(csv_row[0])
            if pack_address is not None and truck_address is not None:
                distance_difference = distance_data[truck_address][pack_address]
                if distance_difference == '':
                    distance_difference = distance_data[pack_address][truck_address]
                diff_distance = float(distance_difference)

                if diff_distance <= subsequent_address:
                    subsequent_address = diff_distance
                    subsequent_package = cur_package

        # The package is removed from the undelivered package list.
        undelivered.remove(subsequent_package)

        # The closest package is then added to the package list of the truck.
        package_id = subsequent_package.package_ID
        set_truck.truck_packages.append(package_id)

        # Updates the trucks current address to the address of the latest package it will have driven to.
        set_truck.truck_address = subsequent_package.package_address

        # Updates the trucks time taken to drive to the nearest package (Takes the trucks 18mph speed into account)
        set_truck.truck_time += datetime.timedelta(hours=subsequent_address / 18)
        subsequent_package.package_deliver_time = set_truck.truck_time
        subsequent_package.package_depart_time = set_truck.truck_depart_time

        # Updates the trucks mileage driven based on the packages address.
        set_truck.truck_mileage += subsequent_address

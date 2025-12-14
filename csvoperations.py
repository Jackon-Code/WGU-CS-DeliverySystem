# File for holding csv related functions.
import csv
from packages import Package


# Simple function for reading in address data from the address csv.
def read_address():
    with open("CSVfiles/WGUPS Distance Table Addresses.csv") as addresses_csv:
        Addresses_csv = list(csv.reader(addresses_csv))
        return Addresses_csv


# Simple function for reading in distance data from the distance csv.
def read_distance():
    with open("CSVfiles/WGUPS Distance Table.csv") as distance_csv:
        dist_csv = list(csv.reader(distance_csv))
        return dist_csv


# The function that will be used to load data from the csv files and insert it all into the hash table.
def fetch_packages_csv(package_csv, package_hash_table):
    with open(package_csv) as package_data:
        for packages in csv.reader(package_data):
            (pack_id, pack_address, pack_city, pack_state, pack_zip, pack_deadline_time,
             pack_weight, pack_status
             ) = packages
            p_data = Package(
                int(pack_id), pack_address, pack_city, pack_state, pack_zip,
                pack_deadline_time, float(pack_weight), "")
            package_hash_table.insert(int(pack_id), p_data)

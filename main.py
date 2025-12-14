# Name: Jackson Hancock
# Student ID: 005494285
# To run this program: Set run configuration to "current file", and run 'main.py'.

import datetime
from matplotlib import pyplot as plt
import truck
from nearestneighbor import nearest_package_delivery, hashtable_packages
from packages import Package

# loads the trucks with their initial packages
delivery_truck1 = truck.Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
                              datetime.timedelta(hours=8))
delivery_truck2 = truck.Truck([3, 9, 12, 18, 22, 24, 26, 27, 25, 35, 36, 38, 39],
                              datetime.timedelta(hours=10, minutes=20))

delivery_truck3 = truck.Truck([2, 4, 5, 6, 7, 8, 10, 11, 17, 21, 23, 28, 32, 33, 41],
                              datetime.timedelta(hours=9, minutes=52))
delivery_truck3.truck_depart_time = (min(delivery_truck1.truck_time, delivery_truck2.truck_time) +
                                     datetime.timedelta(minutes=20))


class Main:

    print("Please provide the following values to create a new package item:")
    # Prompt the user to enter details for the new package
    new_id = int(input("Enter package ID: "))
    new_address = input("Enter package address: ")
    new_city = input("Enter package city: ")
    new_state = input("Enter package state: ")
    new_zip = input("Enter package ZIP code: ")
    new_deadline = input("Enter package deadline time (HH:MM): ")
    new_weight = float(input("Enter package weight in kilograms: "))

    # Create the new package object
    new_package = Package(new_id, new_address, new_city, new_state, new_zip, new_deadline, new_weight, "")

    # Insert the new package into the hashtable
    hashtable_packages.insert(new_id, new_package)

    # Run the nearest neighbor algorithm for the trucks to optimize routes
    nearest_package_delivery(delivery_truck1)
    nearest_package_delivery(delivery_truck2)
    nearest_package_delivery(delivery_truck3)
    print("New package added and delivery routes optimized successfully!")

    # Was used for debugging to ensure truck objects functioned correctly and stored the correct values.
    # print(f'Truck 1 |{delivery_truck1}')
    # print(f'Truck 2 |{delivery_truck2}')
    # print(f'Truck 3 |{delivery_truck3}')
    # print(f'Truck 1 |{delivery_truck1.truck_mileage}')
    # print(f'Truck 2 |{delivery_truck2.truck_mileage}')4
    # print(f'Truck 3 |{delivery_truck3.truck_mileage}')

    categories = ['Truck 1', 'Truck 2', 'Truck 3']
    values = [delivery_truck1.truck_mileage, delivery_truck2.truck_mileage, delivery_truck3.truck_mileage]

    # Opens the console interface for the user and provides the welcome message below whilst also stating the
    # determined routes total mileage (the collective mileage for all 3 trucks after all packages are delivered).
    print("---------------------------------------------------------------------------------------------------")
    print("|   Thank you for using Package Delivery CO's Routing Program!  |")
    print("|                                                                                                 |")
    # Prints the total mileage of the 3 delivery trucks by adding together the mileage of each truck.
    print(f"|              The total mileage for the determined route is: " +
          f"{delivery_truck1.truck_mileage + delivery_truck2.truck_mileage + delivery_truck3.truck_mileage} miles." +
          f"                         |")
    print("---------------------------------------------------------------------------------------------------")
    # Prompts the user to enter the word 's' if they wish to perform a package lookup.
    user_input2 = input("Would you like to view visualizations? Enter 'y' or 'n':")
    if user_input2 == 'y':
        # Creates and displays the bar graph
        plt.bar(categories, values)

        plt.xlabel('Delivery trucks')
        plt.ylabel('Truck Mileage')
        plt.title('Calculated Truck Mileage')

        plt.show()

        # Sets up the data needed for the pie chart
        labels = ['Truck 1', 'Truck 2', 'Truck 3']
        sizes = [13, 13, 15]

        # Creates and displays the pie chart
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

        plt.title('Package Distribution Among Delivery Trucks')

        plt.show()

        # Sets up the data needed for the scatter plot
        package_counts = [13, 13, 15]
        mileages = [delivery_truck1.truck_mileage, delivery_truck2.truck_mileage, delivery_truck3.truck_mileage]
        truck_numbers = ['Truck 1', 'Truck 2', 'Truck 3']

        # Creates and displays the scatter plot
        plt.scatter(package_counts, mileages)

        plt.xlabel('Number of Packages')
        plt.ylabel('Mileage')
        plt.title('Mileage vs. Number of Packages per Truck')
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))

        for i, truck in enumerate(truck_numbers):
            plt.annotate(truck, (package_counts[i], mileages[i]))

        plt.show()

    elif user_input2 == 'n':
        print("Skipping visuals")

    user_input = input("To begin a package lookup, enter 's': ")
    # Checks if the user entered the character 's', and prompt's further input if they did.
    if user_input == 's':
        specified_time = input("Enter the time that you wish to check the status of your package(s) at " +
                               "in HH:MM:SS format: ")
        (hr, min, sec) = specified_time.split(":")
        entered_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))
        specified_search = input("Enter 'i' to search for an individual package by package ID, or enter 'a' to " +
                                 "display all packages: ")
        if specified_search == "i":
            id_to_search = input("Please enter the package ID that you wish to search for: ")
            package = hashtable_packages.hash_lookup(int(id_to_search))
            package.determine_status(entered_time)
            print("------------------------------------------------------------------------------------------"
                  "---------")
            print("|                                  Package Information:                          " +
                  "                 |")
            print("------------------------------------------------------------------------------------------"
                  "---------")
            if package.package_status == "Delivered":
                print(str(f'ID: {package.package_ID} | Address: {package.package_address} | City: '
                          f'{package.package_city} | State: {package.package_state} | Zip Code: '
                          f'{package.package_zip} | Deadline: {package.package_deadline_time} | Weight: '
                          f'{package.package_weight} Kilo(\'s) | Delivery time: {package.package_deliver_time} '
                          f'| Status: {package.package_status}'))
            else:
                print(str(f'ID: {package.package_ID} | Address: {package.package_address} | City: '
                          f'{package.package_city} | State: {package.package_state} | Zip Code: '
                          f'{package.package_zip} | Deadline: {package.package_deadline_time} | Weight: '
                          f'{package.package_weight} Kilo(\'s) | Delivery time: To be determined '
                          f'| Status: {package.package_status}'))
            print("----------------------------------------------------------------")
            print(f"|         Packages delivered by truck number (ordered)         |")
            print(f"| Truck 1: {delivery_truck1.truck_packages} |")
            print(f"| Truck 2: {delivery_truck2.truck_packages}  |")
            print(f"| Truck 3: {delivery_truck3.truck_packages}  |")
            print("----------------------------------------------------------------")
        elif specified_search == "a":
            print("-----------------------------------------------------------------------------------------"
                  "----------")
            print("|                                  Package Information:                          " +
                  "                 |")
            print("-----------------------------------------------------------------------------------------"
                  "----------")
            for packageID in range(1, 42):
                package = hashtable_packages.hash_lookup(packageID)
                package.determine_status(entered_time)
                if package.package_status == "Delivered":
                    print(str(f'ID: {package.package_ID} | Address: {package.package_address} | City: '
                              f'{package.package_city} | State: {package.package_state} | Zip Code: '
                              f'{package.package_zip} | Deadline: {package.package_deadline_time} | Weight: '
                              f'{package.package_weight} Kilo(\'s) | Delivery time: {package.package_deliver_time} '
                              f'| Status: {package.package_status}'))
                else:
                    print(str(f'ID: {package.package_ID} | Address: {package.package_address} | City: '
                              f'{package.package_city} | State: {package.package_state} | Zip Code: '
                              f'{package.package_zip} | Deadline: {package.package_deadline_time} | Weight: '
                              f'{package.package_weight} Kilo(\'s) | Delivery time: To be determined '
                              f'| Status: {package.package_status}'))

            print("----------------------------------------------------------------")
            print(f"|         Packages delivered by truck number (ordered)         |")
            print(f"| Truck 1: {delivery_truck1.truck_packages} |")
            print(f"| Truck 2: {delivery_truck2.truck_packages}  |")
            print(f"| Truck 3: {delivery_truck3.truck_packages}  |")
            print("----------------------------------------------------------------")
        else:
            print("Invalid input, the program will now close.")
            exit()

    else:
        print("Invalid input, the program will now close.")
        exit()

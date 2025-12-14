# The Class for creating and handling the programs hash table.
class CreateHashTable:
    def __init__(self, starting_capacity=20, load_factor=0.7):
        # Initializes the hash table with a set starting capacity and load factor.
        self.load_factor = load_factor
        self.capacity = 0
        self.hash_list = []  # List that will represent the hash table
        for i in range(starting_capacity):
            self.hash_list.append([])

    # Used for both new package insertions, and updates for the hash table.
    def insert(self, id_key, package):
        # Checks to see if resizing is needed. Mostly useful for future scalability purposes.
        if self.capacity / len(self.hash_list) > self.load_factor:
            self.hash_resize()  # Resizes the hash table if the load factor is exceeded.
        if id_key == 9:  # Corrects the address of package 9 before its ran through the algorithm incorrectly.
            package.package_address = package.package_updated_address
            package.package_zip = package.package_updated_zip

        # Uses the hash of the key to find the bucket where the item will be stored.
        hash_bucket = hash(id_key) % len(self.hash_list)
        list_bucket = self.hash_list[hash_bucket]

        # Updates the key if its already in the bucket.
        for key_value in list_bucket:
            if key_value[0] == id_key:
                key_value[1] = package
                return True

        # Otherwise, the item will be appended to the end of the bucket list.
        key_val = [id_key, package]
        list_bucket.append(key_val)
        return True

    # Doubles the capacity of the hash table as to resize it when necessary.
    # Exists for future scalability.
    def hash_resize(self):
        resized_capacity = len(self.hash_list) * 2
        resized_list = [[] for _ in range(resized_capacity)]

        # Rehashes the existing key value pairs into the newly resized list.
        for bucket_list in self.hash_list:
            for key_value in bucket_list:
                new_bucket = hash(key_value[0]) % resized_capacity
                resized_list[new_bucket].append(key_value)
        # Updates the hash table to use the new resized list.
        self.hash_list = resized_list

    # Lookup function for the hash tables items.
    def hash_lookup(self, key):
        hash_bucket = hash(key) % len(self.hash_list)
        bucket_list = self.hash_list[hash_bucket]
        # Iterates through the buckets key value pairs to find the specified key.
        for key_pair in bucket_list:
            if key == key_pair[0]:
                return key_pair[1]
        return None

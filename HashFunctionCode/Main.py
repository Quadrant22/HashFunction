class HashTable:
    def __init__(self, size):
        # A list of empty buckets
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Sum of ASCII values and the bucket index
        return sum(ord(char) for char in key) % len(self.table)

    def insert(self, key, value):
        # Places key in a bucket
        index = self.hash_function(key)
        self.table[index].append((key, value))  

    def display(self):
        # Hash table to be displayed
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# To insert keys
hash_table = HashTable(13)  # table with 13(prime number) buckets
                            # to avoid collision
hash_table.insert("Dragon", "Blue")
hash_table.insert("Comic", "Star")
hash_table.insert("Phone", "Charge")
hash_table.display()


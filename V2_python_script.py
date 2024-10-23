# Updated Code (Simplified and Improved)

def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        ip_addresses = file.read().split()  # Read and split IP addresses into a list
    
    # Use list comprehension to filter out IPs that are in remove_list
    ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]
    
    # Write the updated list of IP addresses back to the file
    with open(import_file, "w") as file:
        file.write(" ".join(ip_addresses))  # Join IP addresses into a single string and write back

# Calling the function with specified arguments
import_file = 'allowed_list.txt'
remove_list = ["192.168.25.60", "192.168.140.81", "192.168.203.198"]

update_file(import_file, remove_list)

# Reading and printing the updated file content
with open(import_file, "r") as file:
    text = file.read()

print(text)

# Explanation:
# - The function `update_file` takes two arguments: `import_file`, which is the file containing IP addresses, and `remove_list`, which contains IPs to be removed.
# - The file is opened in read mode, and its content is read and split into individual IP addresses.
# - List comprehension is used to create a new list that excludes any IPs found in `remove_list`.
# - The updated list of IP addresses is joined back into a single string and written back to the file.

def update_file(import_file, remove_list):
    # Open the file in read mode and read its content
    with open(import_file, "r") as file:
        ip_addresses = file.read()  # Read the content of the file containing IP addresses
    
    # Split the file content into individual IP addresses based on whitespace
    ip_addresses = ip_addresses.split()  # Split the content into individual IP addresses
    
    # Use list comprehension to filter out the IP addresses that need to be removed
    ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]  # Create a new list excluding IPs in remove_list
    
    # Join the updated list of IP addresses into a single string with spaces between each IP address
    ip_addresses = " ".join(ip_addresses)  # Join the IP addresses back into a single string
    
    # Open the file in write mode and write the updated content back to the file
    with open(import_file, "w") as file:
        file.write(ip_addresses)  # Write the updated list back to the file

# Explanation:
# - The function `update_file` takes in two arguments: `import_file`, which is the file containing IP addresses, and `remove_list`, which contains IP addresses to be removed.
# - The file is opened in read mode, and its content is read into the variable `ip_addresses`.
# - The `split()` method is used to break the content into a list of individual IP addresses.
# - The code uses list comprehension to create a new list of IP addresses, excluding any addresses found in the `remove_list`.
# - The list of IP addresses is joined back into a single string, with each IP separated by a space.
# - Finally, the file is opened in write mode, and the updated list of IP addresses is written back to the file.

def update_file(import_file, remove_list):
    # Open the file in read mode and read its content
    with open(import_file, "r") as file:
        ip_addresses = file.read()  # Read the content of the file containing IP addresses
    
    # Split the file content into individual IP addresses based on whitespace
    ip_addresses = ip_addresses.split()  # Split the content into individual IP addresses
    
    # Iterate through the list of IP addresses
    # Remove elements that are in the remove_list
    for element in ip_addresses:
        if element in remove_list:
            ip_addresses.remove(element)  # Remove IP addresses that match those in remove_list
    
    # Join the updated list of IP addresses into a single string with spaces between each IP address
    ip_addresses = " ".join(ip_addresses)  # Join the IP addresses back into a single string
    
    # Open the file in write mode and write the updated content back to the file
    with open(import_file, "w") as file:
        file.write(ip_addresses)  # Write the updated list back to the file

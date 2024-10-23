def update_file(import_file, remove_list):

    with open(import_file, "r") as file:
        ip_addresses = file.read()

    ip_addresses = ip_addresses.split()

    for element in ip_addresses:

        if element in remove_list:

            ip_addresses.remove(element)

    ip_addresses = " ".join(ip_addresses)

    with open(import_file, "w") as file:

        file.write(ip_addresses)

#Calling the function and placing my two arguments.

import_file = 'allowed_list.txt'
remove_list = ["192.168.25.60", "192.168.140.81", "192.168.203.198"]

update_file(import_file, remove_list)

# Reading and printing the updated file content
with open(import_file, "r") as file:

  text = file.read()

print(text)






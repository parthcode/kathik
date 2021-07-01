import os

from file_operations import get_user_name, read_user_name_from_file, write_user_name_to_file

print("Enter a operation")
operation = int(input("Enter 1 to read. | Enter 2 to write"))
name = get_user_name()
location = os.getcwd() + '/user_details.txt'

if operation == 1:
    print(read_user_name_from_file(name, location))
elif operation == 2:
    write_user_name_to_file(name, location)

def get_user_name():
    name = input("Please enter your name")
    return name


def write_user_name_to_file(name, file_location):
    meta_data = open(file_location, 'a')
    meta_data.write(name)
    meta_data.write('\n')
    meta_data.close()


def read_user_name_from_file(name, file_location):
    meta_data = open(file_location, 'r')
    data = meta_data.read()
    meta_data.close()
    if name in data:
        return True
    return False

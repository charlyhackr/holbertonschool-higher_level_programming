def search_replace(my_list, search, replace):
    return [replace if search == num else num for num in my_list]

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_lst = []
    for cont in range(list_length):
        try:
            new_lst.append(my_list_1[cont] / my_list_2[cont])
            continue
        except ZeroDivisionError:
            print("division by 0")
            new_lst.append(0)
        except TypeError:
            print("wrong type")
            new_lst.append(0)
        except IndexError:
            print("out of range")
            new_lst.append(0)
        finally:
            pass
    return (new_lst)

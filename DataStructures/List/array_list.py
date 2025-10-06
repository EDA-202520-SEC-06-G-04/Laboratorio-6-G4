def new_list():
    newlist = {
        'elements': [], 
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"] = [element] + my_list["elements"]
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    
    
    if my_list["size"] == 0:
        my_list["elements"].append(element)
    
    else:
        my_list["elements"].append(element)
    
    my_list["size"] += 1
    
    return my_list

def is_empty(my_list):
    
    size = my_list["size"]
    
    if size == 0:
        iss = True
    else:
        iss = False
    
    return iss

def size(my_list):

    size = my_list["size"]
    
    return size

def first_element(my_list):
    
    return my_list["elements"][0]

    
def last_element(my_list):
    
    return my_list["elements"][-1]

def delete_element(my_list, pos):
    
    if (pos >= 0) and (pos < (my_list["size"])):
      my_list["elements"] = my_list["elements"][:pos] + my_list["elements"][pos+1:]
      
      my_list["size"] -= 1
      
      return my_list
    
    else:
        
        return my_list["elements"][pos]
    
    
def remove_first(my_list):
    
    if my_list["size"] == 0:
        first = my_list["elements"][0] 
        
    else:
        first = my_list["elements"][0]
        my_list["elements"] = my_list["elements"][1:]
        
        my_list["size"] -= 1
        
        return first

def remove_last(my_list):
    
    if my_list["size"] == 0:
        element = my_list["elements"][0] 
        
    else:
        last = my_list["elements"][-1]
        my_list["elements"] = my_list["elements"][:-1]
        
        my_list["size"] -= 1
        
        return last

def insert_element(my_list, element, pos):
    my_list["elements"] = (my_list["elements"][:pos] + [element] + my_list["elements"][pos:])
    my_list["size"] += 1
    return my_list



def change_info(my_list, pos, new_info):

    if (pos >= 0) and (pos < (my_list["size"])):

         my_list["elements"][pos] = new_info

         return my_list
    
    else: 
        return None


def exchange(my_list, pos1, pos2):

    if ((pos1 >= 0) and (pos1 < (my_list["size"]))) and ((pos2 >= 0) and (pos2 < (my_list["size"]))):
        
        element_1 = my_list["elements"][pos1]
        element_2 = my_list["elements"][pos2]

        my_list["elements"][pos1] = element_2
        my_list["elements"][pos2] = element_1

        return my_list
    
    else:
        
        return None 

def sub_list(my_list, pos_i, num_elements):

    if (pos_i >= 0) and (pos_i < (my_list["size"])):
        
        final_list = pos_i + num_elements

        if final_list > my_list["size"]:
            final_list = my_list["size"]

        elements = my_list["elements"][pos_i: final_list]
        sublist = {"size": len(elements), "elements": elements}

        return sublist
    
    else: 
        
        return None


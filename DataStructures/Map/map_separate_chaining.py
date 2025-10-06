from random import randint
from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime):
     
    lista_elementos = al.new_list()
    
    table = {"size": al.size(),
            "elements": al.add_last(lista_elementos)
            }
    
    prime_to_use = 109345121
    
    if prime != None:
        prime_to_use = prime
    
    my_map = {"prime": prime_to_use,
              "capacity": num_elements/load_factor,
              "scale" : randint(1,prime-1),
              "shift": randint(0,prime-1),
              "table": table, 
              "current_factor": 0,
              "limit_factor": load_factor,
              "size": 0     
              }
    return my_map

def rehash(my_map):
    new_load_factor = my_map["limit_factor"]
    new_capacity = my_map["capacity"] 
    new_num_elements = new_load_factor * new_capacity
    
    new_prime = mf.next_prime(new_capacity)
    
    table = my_map["table"]
    rehash = new_map(new_num_elements,new_load_factor,new_prime)
    new_map["table"] = table
                
    return rehash     
   
def hash_value (my_map, key):    
    m =  my_map["table"]["size"]
    hash_key = hash(key)
    
    p = mf.next_prime(m)
                
    a = randint(1,(p-1))
    b = randint(0,(p-1))
    
    MAD = (abs(a * hash_key + b) % p) % m
    return MAD
        
def find_slot(my_map,key,hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail
    
def put(my_map, key, value):  
    key_hash = hash_value(key)
    slot = find_slot(my_map,key,key_hash)
    
    if slot != None:
        my_map["table"]["elements"][slot] = value
        my_map["current_factor"] += 0.09090909090909091
           
    else:
        al.insert_element(my_map["table"]["elements"],{key:value},(my_map["table"]["size"])+1)
        my_map["current_factor"] = 0.18181818181818182
            
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map) 
        
    return my_map

def is_available(my_map, pos):
    entry = al.get_element(my_map["table"], pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False


def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1
     
def contains(my_map,key):
    contains = False
    for pos in my_map:
        if my_map[key] == my_map[pos]:
            contains = True
    return contains
    
def get(my_entry):
    return me.get_key(my_entry)
    
def remove(my_map, key):
    
    for pos in my_map:
        if my_map[pos] == my_map[key]:
            my_map["elements"][key] = "__EMPTY__"
            my_map["elements"]["value"][pos] = "__EMPTY__"
            
    return my_map  

def size(my_map):
    size = my_map["table"]["size"]  
    return size
  
def is_empty(my_map):
    size = size(my_map)
    if size != 0:
        respuesta = False
    else:
        respuesta = True
    return respuesta
        
def key_set(my_map):
    resultado = {}
    lista = al.new_list()
    for pos in my_map["table"]["elements"]:
        al.add_last(my_map["table"]["elements"][pos])
    
    if len(lista) == 0:
            resultado = {"elementos": lista, size: 0}
    else:
            resultado = {"elementos": lista, size: len(lista)}
            
    return resultado
   
def value_set(my_map):
    lista = al.new_list()
    for pos in my_map["table"]:
        al.add_last(my_map["table"][pos])
        
    return lista
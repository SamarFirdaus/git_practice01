#DICTIONARY --> the most important
#' keys' can't be duplicate,duplicate values are allowed
# no index based operation
# dictionary is mutable.
#  Dictionaries are defined using curly braces {}, with colon : separating keys and values. Each key-value pair is separated by a comma.

dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
#print(type(dic))
print(dic)
#print(dir(dic))
"""

<class 'dict'>
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', 
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', 
 '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
 '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 
 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
 """
#'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
#In Python, the fromkeys() method is a class method that returns a new dictionary with keys from a sequence and values set to a specified value, or None by default if no value is provided.

"""
 the fromkeys() method is a class method that returns a new dictionary with keys from a sequence and values set to a specified value, or None
   by default if no value is provided.

Here's the syntax for the fromkeys() method:
dict.fromkeys(sequence[, value])
sequence: This is the sequence of keys for the new dictionary.
value (optional): This is the value to be set for all the keys. If not provided, the default value is None.
Here's an example of how you can use t0he fromkeys() method:
"""
dic1 = dic.fromkeys(('A', 'B', 'C','D'),20) 
#print(dic1)
#print(dic)
"""
  from key method only takes two arguments one is key and another one is it's value if we want give more than one key and 
value then you have put keys in square brackets for list and for tuple paranthesis bracket u can use, then after coma put value
 ...value is same for all keys if we dont give value then by default it takes none value
"""

print(dic.get('f'))
# it gives one value of given key in bracket, and if u give key which is not present in bracket then it returns none by default

print(dic.items()) #--> dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40), ('e', 50)])

print(dic.keys())  # --> dict_keys(['a', 'b', 'c', 'd', 'e'])
 
print(dic.values()) #--> dict_values([10, 20, 30, 40, 50])

#print(dic.pop('a'))  #--> 10
#print(dic)   #       --> {'b': 20, 'c': 30, 'd': 40, 'e': 50}

#print(dic.pop('a','b')) #--> 10
#print(dic)  #--> {'b': 20, 'c': 30, 'd': 40, 'e': 50}
# it takes onlu one argument as a key to remove the value,if u give two value then it takes first key and remove the first keys value 

#print(dic.popitem())   #--> ('e', 50)  removes last item 

print(dic.setdefault('f',120))   # -->{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 120} set only one value in the last of dictionary if value is not given by deafuit takes None
print(dic)

dic.update(dic1)
print(dic)  #---->{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 120, 'A': 20, 'B': 20, 'C': 20, 'D': 20}

dic['A'] =  90
print(dic)   # --> {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 120, 'A': 90, 'B': 20, 'C': 20, 'D': 20}

print(dic['B'])  #--> 20

print(dic.get('b')) #--> 20

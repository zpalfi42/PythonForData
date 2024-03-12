"""_summary_

Raises:
    an: _description_
"""
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

'''
Python lists!
Lists allow duplicated values and its order can be changed
List items are indexed starting by 0
To change a list itme we only need to access with the index the item we want
to change
and change it.

Python tuples!
Tuples allow duplicated values but its order and values are unchangeable
Tuple items are indexed starting by 0
One way to change tuple items is to transform the tuple into a list change the
item and
transform it back again into a tuple.
Another way to change a tuple item is slicing (the way I did it).

Python sets!
Sets does not allow duplicated items and their items order and values are
unchangeble
Set items are not indexed
The only way to change a set item is to remove it and add another one.
To remove a set item we can either use remove() or discard() (or if the item
is at the end
of the set pop()).
The difference between remove and discard is that remove method will raise an
error if the
specified item does not exist.

Python dictionaries!
Dictionaries are used to store values in pairs (key:value)
Dictionaries doesnt allow duplicates and its items are ordered and changeable.
To change the value of a pair we can eater access with the key (dict[key]) or
use the
update() function
'''
ft_list[1] = 'World!'

ft_tuple = (ft_tuple[0], 'Spain!')

ft_set.remove("tutu!")
ft_set.add("Barcelona!")

ft_dict["Hello"] = "42Barcelona!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

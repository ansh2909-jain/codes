#Count() Method
Tuple1 = (0, 1, 2, 3, 4, 5, 3, 3, 3)                            # Creating tuples 
Tuple2 = ('anmol', 'jain', 'jain', 
		'for', 'anmol', 'jain') 

res = Tuple1.count(3)                                           # count the appearance of 3 
print('Count of 3 in Tuple1 is:', res)

res = Tuple2.count('anmol')                                    # count the appearance of python
print('Count of anmol in Tuple2 is:', res)
 
Tuple = (0, 1, (2, 3), (2, 3), 1,                               # Creating tuples
		[3, 2], 'geeks', (0,))  

res = Tuple.count((2, 3))                                       # count the appearance of (2, 3) 
print('Count of (2, 3) in Tuple is:', res) 

res = Tuple.count('geeks')                                       # count the appearance of [3, 2] 
print('Count of geeks in Tuple is:', res)

#Index() Method 
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)                             # Creating tuples

res = Tuple.index(3)                                            # getting the index of 2  
print('First occurrence of 2 is', res) 

res = Tuple.index(3, 4)                                         # getting the index of 2 after 4th index 
print('First occurrence of 2 after 4th index is:', res)
 
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2, )                             # Creating tuples
 
res = Tuple.index(4)                                            # getting the index of 4
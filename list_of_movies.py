# Make a list of your favourite Movies, the list should have minimum 8
# elements
list_movies = list(('2018','Athiran','Neela Velicham','Joseph','Mumbai Police','Moz \'N\' cat','12th Man','Masters','Dheera','Meri Aavas Suno'))
print(list_movies)
#Print a specified list after removing the 5th element.
demo1 = ['Vyshakh','Kamal','Jude Antony','Shaji Kailas','Basil Joseph']
print('Current list is :\n')
print(demo1)
demo1.remove('Basil Joseph')
print('List after removal of fifth element\n')
print(demo1)
demo1.insert(4,'Vineeth Sreenivasan')
print('After adding another element to fifth position\n')
print(demo1)
print('4th element in the list of directors is \n',demo1[3])
demo1.append('Lal Jose')
print('After adding one more element, updated list is\n',demo1)

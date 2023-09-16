numbers = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six"
}
print("the number dictionary is: ",numbers)
print("the value at the second position is: ",numbers.get(2))
print(numbers.get('3', 'Key unavailable'))
print(numbers.get(3))
print(numbers.get('four','Unavailbale key'))
print(numbers.get(10,'Unavailable key'))
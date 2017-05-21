def get_even_list(even_list):
    even_list=[ x for x in even_list if x%2==0]
    return even_list
#extract_even(range(10))

l=even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    big_list = []
    for i in list1:
        big_list.append(i)
    for i in list2:
        big_list.append(i)
    return (big_list)
    
print(merge_list(chunk_one, chunk_two))

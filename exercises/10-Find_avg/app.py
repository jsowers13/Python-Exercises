my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
def find_avg(arr):
    aux = 0
    for i in arr:
        aux = aux + i
    avg = aux / len(arr)
    print(avg)

find_avg(my_list)

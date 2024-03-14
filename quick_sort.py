# takinga a pivot and sort around it and to that again and agian (it is done on a set so there is only one posible answer)
from numpy import mean
list_to_sort = [9,8,3,17,2,1,6,20,25,30,70,15,90,5]


def quick_sort(list_sort ) -> list:
    if len(list_sort) < 2:
        return list_sort
    else:
        pivot_value : int = int(mean(list_sort))
        counter = 0
        item_pos = 0
        for item in list_sort:
            if item > pivot_value:
                pass
            else:
                if counter != item_pos:
                    list_sort[counter], list_sort[item_pos] = list_sort[item_pos], list_sort[counter]
                counter += 1
            item_pos += 1

    return quick_sort(list_sort[:counter]) + quick_sort(list_sort[counter:])
        

print(quick_sort(list_to_sort))


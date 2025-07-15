import random
array = [1,2,3,4,5,6,7,8,9,10]
destination = []

def scramble(array:list):
    for i in range(len(array)):
        secondElement = random.choice(array)
        secondIndx = array.index(secondElement)
        array[secondIndx] = array[i]
        array[i] = secondElement
    return array
    

def split(array:list, destination:list, first_index,last_index): 
    mid = (int)((first_index + last_index)/2)
    if(len(array)<= 2):
        if(array[0]>array[1]):
            destination.append(array[1])
            destination.append(array[0])
        else:
            destination.append(array[0])
            destination.append(array[1])
    else:
        left = array[first_index:mid]
        right = array[mid:last_index]
        split(left,first_index,mid)
        split(right,mid,last_index)

    

def binary_search(array, low_index:int, high_index:int, target:int):
    middle = (int)((array[low_index] + array[high_index])/2)

    if(middle == target):
        return middle
    elif(middle > target):
        return binary_search(array,low_index,middle,target)
    else:
        return binary_search(array,middle,high_index,target)
# print(binary_search(array,0,9,2))
print(scramble(array))
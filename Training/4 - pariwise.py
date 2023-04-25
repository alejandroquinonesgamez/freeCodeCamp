#Copiar el array
#Recorrer el array
#if(value[i] <= arg)
#   check = subarray[i+1:].find(arg - value[i])
#   if(check > -1)
#       result += i + check+i+1
#       value[i] = arg+1
#       value[check+i+1] = arg+1

def find(arr, value):
    for item in arr:
        if (item == value):
            return arr.index(item)
    return -1  


def pairwise(arr, arg):
    arrCopy = arr.copy()
    result = 0
    for value in arrCopy:
        if (value <= arg):
            index = arrCopy.index(value)
            check = find(arrCopy[index+1:], arg - value)
            index2 = index+1+check
            if (check > -1):
                result += index + index2
            arrCopy[index] = arg+1
            arrCopy[index2] = arg+1
    print(result)        
    return result

pairwise([1, 1, 1], 2)
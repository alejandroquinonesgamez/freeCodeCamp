def sym(*args):
    numbersList = list(args)
    result = []
    for set in numbersList:
        for number in set:
            result.append(number)
    numbersList = result
    numbersList.sort()
    result = []
    print(numbersList)
    for number in numbersList:
        if ((numbersList.count(number) < len(list(args))) & (result.count(number) == 0)):
            result.append(number)
    print(result)
    return result
    
        
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
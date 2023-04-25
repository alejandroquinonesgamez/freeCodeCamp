def updateInventory(arr1, arr2):
    inventory = {}
    arr = []
    for item in arr1:
        inventory[item[1]] = item[0]
    for item in arr2:
        if (item[1] in inventory):
            inventory[item[1]] += item[0]
        else:
            inventory[item[1]] = item[0]
    for item in inventory.keys():
        arr.append(item)
    arr.sort()
    print(arr)
    arr1 = []
    for item in arr:
        arr1.append([inventory[item], item])
    print(arr1)
    return arr1
  
updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]])
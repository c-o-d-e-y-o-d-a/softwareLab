import pandas as pd
 
def sort(index,arr):
    for i in range(1,len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if index == 0:
                if int(arr[min_idx][index][1:]) > int(arr[j][index][1:]):
                    min_idx = j     
            else:
                if arr[min_idx][index] > arr[j][index]:
                    min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
            

arr = [
["P_ID", "Process", "Start Time (ms)", "Priority"],
["P1", "VSCode", 100, "MID"],
["P23" ,"Eclipse" ,234 ,"MID"],
["P93", "Chrome", 189, "high"],
["P42" ,"JDK", 9 ,"high"],
["P9", "CMD", 7, "high"],
["P87", "NotePad" ,23, "Low"]]
print("NIschal Gautam\nE22CSEU1523\nB28 G4")
print("Welcome to Array Sorter\n")
print("Please select a sorting parameter:")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
print("3. Sort by Priority")
choice = int(input("Enter your choice(1/2/3): "))
match choice:
    case 1:
        df = pd.DataFrame(sort(0,arr))
    case 2:
        df = pd.DataFrame(sort(2,arr))
    case 3:
        df = pd.DataFrame(sort(3,arr))
print("\n\n",df.to_string(index=False, header=False))
print("Thank you for using Array Sorter")
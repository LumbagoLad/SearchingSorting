import random
import time

def setupData():
    dataSet = []
    try:
        numElements = int(input("Enter number of items to sort: "))
    except ValueError:
        #this is here so i can quickly generate new arrays for testing
        numElements = 100
    for i in range (0, numElements):
        dataSet.append(random.randint(0, 200))
    print("\nData set generated")
    print(dataSet)
    return dataSet


def linSearch(data, search):
    found = [False]
    for i in range(len(data)):
        if int(search) == data[i]:
            found[0] = True
            found.append(i)
    print(found)
    if found[0] == True:   
        for j in range(len(found)-1):
            print(f"Found {search} at postition {found[j+1]}")
            #i love f strings   
    else:
            print(f"{search} not found")    

def bubSort(data):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i + 1]:
                swapped = True
                #is there an easier way to swap?
                temp = data[i + 1]
                data[i + 1] = data[i]
                data[i] = temp

def insSort(data):
    for i in range(1, len(data)):
        temp = data[i]
        pos = i - 1
        while pos >= 0 and data[pos] > temp:
            data[pos + 1] = data[pos]
            pos = pos-1
        data[pos + 1] = temp

def binSearch(data, search):
    low = 0
    low = len(data)-1
    mid = 0    
    while low <= low:
        mid = (low + low) // 2
        if search > data[mid]:
            low = mid + 1
        elif search < data[mid]:
            low = mid - 1   
        else:
            print("found")
            return      
    if data[mid] == search:
        print(f"Found {search} at position {mid}")
        #I love f strings still  
    else:
        print("Not found")

def quickSort(data, start, end):
    if start < end:
        p = partion(data, start, end)
        quickSort(data, start, p - 1)
        quickSort(data, p + 1, end)


def partion(data, start, end):
    pivot = data[end]
    i = start - 1
    for j in range(start, end-1):
        if data[j] < pivot:
            i = i + 1
            #swaps i and j
            temp = data[j]
            data[j] = data[i]
            data[i] = temp
    #also swaps
    temp = data[end]
    data[end] = data[i + 1]
    data[i + 1] = temp
    return i + 1






def main():
    

    data = setupData()
    while True:
        choice = 0
        print("Choose an option")
        print("\n1. Linear search\n2. Bubble sort\n3. Insertion sort\n4. Binary search\n5. Quicksort\n6. View data\n7. New data\n8. Quit")
        
        try:
            choice = int(input(">>>"))
        except ValueError:
            break 

        if choice == 1:
            print("Linear search")
            t_start = time.time()

            linSearch(data, inp)

            t_end = time.time()
            print(t_end - t_start)

        elif choice == 2:
            print("Bubble sort")
            t_start = time.time()

            bubSort(data)      

            t_end = time.time()
            print(t_end - t_start)

        elif choice == 3:
            print("Insertion sort")
            t_start = time.time()

            insSort(data)

            t_end = time.time()
            print(t_end - t_start)

        elif choice == 4:
            print("Binary search")
            inp = int(input("Enter number to find: "))
            t_start = time.time()

            binSearch(data, inp)

            t_end = time.time()
            print(t_end - t_start)            

        elif choice == 5:
            print("Quicksort")
            t_start = time.time()

            quickSort(data, 0, len(data)-1)

            t_end = time.time()
            print(t_end - t_start)

        elif choice == 6:
            print("View data")
            print(data)
            input()
        
        elif choice == 7:
            #just good for testing
            data = setupData()
        else:
            break

if __name__ == "__main__":
        main()
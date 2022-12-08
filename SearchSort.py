import random
import time

def setupData():
    dataSet = []
    try:
        numElements = int(input("Enter number of items to sort: "))
    except ValueError:
        numElements = 100
    for i in range (0, numElements):
        dataSet.append(random.randint(0, 200))
    print("\nData set generated")
    print(dataSet)
    return dataSet

def main():
    def linSearch(search):
        start = time.time()
        found = [False]
        for i in range(len(data)):
            if int(search) == data[i]:
                found[0] = True
                found.append(i)
        print(found)
        if found[0] == True:   
            for j in range(len(found)-1):
                print(f"Found {search} at postition {found[j+1]}")
                
        else:
                print(f"{search} not found")   
        end = time.time()
        print(end - start)    
    def bubSort():
        start = time.time()
        swapped = True
        while swapped == True:
            swapped = False
            for i in range(len(data)-1):
                if data[i] > data[i + 1]:
                    swapped = True
                    temp = data[i + 1]
                    data[i + 1] = data[i]
                    data[i] = temp
        end = time.time()
        print(end - start)
    def insSort():
        start = time.time()
        for i in range(1, len(data)):
            temp = data[i]
            pos = i - 1
            while pos >= 0 and data[pos] > temp:
                data[pos + 1] = data[pos]
                pos = pos-1
            data[pos + 1] = temp
        end = time.time()
        print(end - start)
    def binSearch(search):
        start = time.time()
        first = 0
        last = len(data)-1
        mid = (first + last) // 2
        while data[mid] != search and first < last:
            print(f"{first} {mid} {last}")
            mid = (first + last) // 2
            if search > mid:
                first = mid + 1
            else:
                last = mid
            
        if data[mid] == search:
            print("Found")
            
        else:
            print("Not found")
                
        end = time.time()
        input(end - start)


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
            linSearch(input("Enter number to find: "))
            
        elif choice == 2:
            print("Bubble sort")
            bubSort()          
                
        elif choice == 3:
            print("Insertion sort")
            insSort()
        
        elif choice == 4:
            print("Binary search")
            binSearch(int(input("Enter number to find: ")))

        elif choice == 5:
            print("Quicksort")

        elif choice == 6:
            print("View data")
            print(data)
            input()
        elif choice == 7:
            data = setupData()
        else:
            break

if __name__ == "__main__":
        main()
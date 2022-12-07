import random
import time

def setupData():
    dataSet = []
    numElements = int(input("Enter number of items to sort: "))
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
        print(data)
        end = time.time()
        print(end - start)
    def insSort():
        start = time.time()
        for i in range(len(data)):
            1

    data = setupData()
    while True:
        print("Choose an option")
        print("\n1. Linear search\n2. Bubble sort\n3. Insertion sort\n4. Binary search\n4. Binary search\n5. Quicksort\n6. View data\n7. Quit")

        choice = int(input(">>>"))
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

        elif choice == 5:
            print("Quicksort")

        elif choice == 6:
            print("View data")

        else:
            break

if __name__ == "__main__":
        main()
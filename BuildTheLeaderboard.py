def selection_sort(data):
    arr = data[:]
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i,len(arr)):
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(data):
    arr = data[:]
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j][1] > arr[j+1][1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for item in arr[:-1]:
        if item[1] <= pivot[1]:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(data):
    arr = data[:]
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i, j =0,0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def func1(choice=None):
    players = [
        ("Arjun",450),
        ("Riya"  ,  720),
        ("Kabir"  ,  310),
        ("Neha"    ,890),
        ("Aman"    ,560)
    ]

    if choice is None:
        print("Enter the number between 1-4")
        print("1. Selection Sort \n 2. Bubble Sort \n 3. Merge Sort \n 4. Quick Sort")

        choice = input("Enter the number which type of sorting you want to preform : ")

    if choice == '1':
        sorted_choice = selection_sort(players)

    elif choice == '2':
        sorted_choice = bubble_sort(players)

    elif choice == '3':
        sorted_choice = merge_sort(players)

    elif choice == '4':
        sorted_choice = quick_sort(players)

    else:
        print("wrong input Try again later!")
        return []

    for name , score in sorted_choice:
        print(f"{name} : {score}")

    return sorted_choice


if __name__ == "__main__":
    func1()

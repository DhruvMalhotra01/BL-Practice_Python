arr = [105, 118, 129, 145, 167, 189, 205, 221, 250]


def binary_search(arr, treasure_id):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == treasure_id:
            print("found!")
            return True


        elif treasure_id > arr[mid]:
            left = mid + 1
        else:
            right = mid -1
    print("not found!")
    return False


def func2():
    treasure_id = int(input("Enter treasure ID of players: "))
    return binary_search(arr, treasure_id)


if __name__ == "__main__":
    func2()

def main():
    unsorted_list = [5,3,2,4,1]
    sorted_list = insertion_sort(unsorted_list[:]) # give a shallow copy to the fucntion so that original function doesn't change
    print(f"Unsorted: {unsorted_list}")
    print(f"Sorted: {sorted_list}")

def insertion_sort(array):
    # select second number
    # pointer pointing to the elemnt on the left
    # compare and swap if value is smaller
    # repeat step 2 and step 3

    for i in range(0, len(array) - 1):
        while (i+1) != 0:

            temp = array[i]
            if array[i+1] < array[i]:
                array[i] = array[i+1]
                array[i + 1] = temp

                i -= 1

            else:
                break

    return array



if __name__ == '__main__': main()
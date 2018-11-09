# kruskal's algorithm

def main():
    array = [5,6,4,3,7]
    quick_sort(array)
    print(array)


def quick_sort(array):
    unsorted = list(array)
    print(array)
    if len(array) > 1:
        l = pivot(array)
        quick_sort(array[:l-1])
        quick_sort(array[l+1:])

    print(array)
def pivot(array):
    p = array[0] # pivot
    k = 0 # left pointer
    l = len(array) - 1 # right pointer


    while True:
        if array[k] > p or k >= len(array): # while left pointer value is smaller than pivot or left pointer has not reached the end
        # second condition is to force k to stop at the last value
            break
        else:
            k = k + 1

    while True:
        if array[l] <= p: # doesn't need the k >= 0 condition because this condition will gurantee to hold when the right pointer points towards the 0th element
            break
        else:
            l = l - 1

    while k < l:
        temp = array[k]
        array[k] = array[l]
        array[l] = temp

        while array[k] <= p:
            k = k + 1

        while array[l] > p:
            l = l - 1

    temp = array[0]
    array[0] = array[l]
    array[l] = temp

    return l



if __name__ == '__main__': main()
def leftrotation(arr, d):
    n = len(arr)
    for i in range(d):
        temp = arr[0]
        for a in range(n-1):
            arr[a] = arr[a+1]
        arr[n-1] = temp
    return print(arr)

def leftrotation2(arr, d):
    temp_array = arr[:d]
    arr = arr[d:]
    arr = arr + temp_array
    print(arr)







leftrotation2([1,2,3,4], 2)


# def leftRotate(arr, d, n):
#     for i in range(d):
#         leftRotatebyOne(arr, n)
#
#
# # Function to left Rotate arr[] of size n by 1*/
# def leftRotatebyOne(arr, n):
#     temp = arr[0]
#     for i in range(n - 1):
#         arr[i] = arr[i + 1]
#     arr[n - 1] = temp
#
#
# # utility function to print an array */
# def printArray(arr, size):
#     for i in range(size):
#         print("% d" % arr[i], end=" ")
#
#
# # Driver program to test above functions */
# arr = [1, 2, 3, 4]
# leftRotate(arr, 2, 4)
# printArray(arr, 4)
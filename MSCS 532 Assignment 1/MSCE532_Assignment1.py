def insertion_sort_descending(arr):
    # Traverse through the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be placed at the correct position
        j = i - 1
        
        # Move elements of arr[0..i-1], that are smaller than the key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at the correct position
        arr[j + 1] = key

# Example usage
array = [12, 11, 13, 5, 6]
insertion_sort_descending(array)
print("Sorted array in decreasing order:", array)

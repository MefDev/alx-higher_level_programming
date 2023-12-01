
#!/usr/bin/python3
"""Find a peak number"""
def find_peak_recursive(arr, left, right):
    mid = left + (right - left) // 2
    
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid] # find peak
    
    # If mid element is smaller than its left neighbor, search left
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak_recursive(arr, left, mid - 1)
    
    # If mid element is smaller than its right neighbor, search right
    else:
        return find_peak_recursive(arr, mid + 1, right)

def find_peak(list_of_integers):
    """Find a peak"""
    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
def Binarysearch(num,l, r, target):
    #invalid range
    if l>r:
        return -1
    
    mid = (r+l) // 2

    if num[mid] == target:
        return mid
    elif num[mid] < target:
        return Binarysearch(num,mid+1, r, target)
    elif num[mid] > target:
        return Binarysearch(num,l, mid-1, target)
    

nums = [1,3,5,7,9,11,12]
print(Binarysearch(nums, 0, len(nums)-1, 5))


def find_cruise_length(cruise_lengths, l, r, vacation_length):
    if l>r:
        return False
    mid = (r+l) // 2

    if cruise_lengths[mid] == vacation_length:
        return True
    elif cruise_lengths[mid] < vacation_length:
        return find_cruise_length(cruise_lengths,mid+1, r, vacation_length)
    elif cruise_lengths[mid] > vacation_length:
        return find_cruise_length(cruise_lengths,l, mid-1, vacation_length)

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15],0, 7, 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 0, 7, 11))

def find_cabin_index(cabins, l, r, preferred_deck):
    
    if l>r:
        return l
    mid = (r+l) // 2
    

    if cabins[mid] == preferred_deck:
        return mid
    elif cabins[mid] < preferred_deck:
        return find_cabin_index(cabins,mid+1, r, preferred_deck)
    elif cabins[mid] > preferred_deck:
        return find_cabin_index(cabins,l, mid-1, preferred_deck)
    


print(find_cabin_index([1, 3, 5, 6],0, 3,  5))
print(find_cabin_index([1, 3, 5, 6],0, 3, 2))
print(find_cabin_index([1, 3, 5, 6],0, 3, 7))


def count_checked_in_passengers(rooms, l, r):
    if l>r:
        return 0
    
    mid = (r+l) // 2

    if rooms[mid] == 1 and (mid == 0 or rooms[mid-1] == 0):
        return len(rooms) - mid
    elif rooms[mid] < 1:
        return count_checked_in_passengers(rooms,mid+1, r)
    elif rooms[mid] > 1 and rooms[mid-1] != 0:
        return count_checked_in_passengers(rooms,l, mid-1)

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1, 0, 6)) 
print(count_checked_in_passengers(rooms2, 0, 5))
print(count_checked_in_passengers(rooms3, 0, 5))


def is_profitable(excursion_counts):
    pass
    # we have to find if there is a zero, can use binary search, if there is return -1
    if Binarysearch(excursion_counts, 0, len(excursion_counts), 0) != -1:
        return -1
    # else, return min(first element, length of the list)
    else:
        return min(excursion_counts[0], len(excursion_counts))
print(is_profitable([3, 5]))
print(is_profitable([0, 0]))

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr  # Base case: arrays with 1 or no elements are already sorted

#     # Divide the array into two halves
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])

#     # Merge the sorted halves
#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = 0  # Pointer for left half
#     j = 0  # Pointer for right half

#     # Compare elements from both halves and merge them in sorted order
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     # Append any remaining elements in the left or right half
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

def find_shallowest_point(arr, l, r):
    if len(arr) == 1:
        return arr[1]
    if l == r:
        return arr[l]
    mid = (l + r) // 2
    left_min = find_shallowest_point(l, mid)
    right_min = find_shallowest_point(mid + 1, r)
    if left_min < right_min:
        return left_min
    else:
        return right_min

# def find_min(left,right):
#     minimum = 999999
#     i = 0  # Pointer for left half
#     j = 0  # Pointer for right half

#     # Compare elements from both halves and merge them in sorted order
#     while i < len(left) and j < len(right):
#         if left[i] < minimum:
#             minimum = left[i]
#         elif right[j] < minimum:
#             minimum = right[j]

# #     # Append any remaining elements in the left or right half
# #     result.extend(left[i:])
# #     result.extend(right[j:])

#     return minimum



# def find_shallowest_point2(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_min = find_shallowest_point2(arr[:mid])
#     right_min = find_shallowest_point2(arr[mid:])


#     return find_min(left_min, right_min)

print(find_shallowest_point([5, 7, 2, 8, 3],0,4))
print(find_shallowest_point([12, 15, 10, 21],0,3))



# def find_treasure(matrix, treasure):
#     if l>r:
#         return (-1, -1)
    
#     num_rows = len(matrix)
#     num_cols = len(matrix[0])
#     mid = (0+len(matrix)) // 2
#     #matrix
#     if matrix[mid] == treasure:
#         return matrix[mid][0]
#     elif matrix[mid][mid] < target:
#         return Binarysearch(num,mid+1, r, target)
#     elif matrix[mid] > treasure:
#         right = mid
#         return Binarysearch(num,mid+1, r, target)
    

# rooms = [
#     [1, 4, 7, 11],
#     [8, 9, 10, 20],
#     [11, 12, 17, 30],
#     [18, 21, 23, 40]
# ]

# print(find_treasure(rooms, 17))
# print(find_treasure(rooms, 5))
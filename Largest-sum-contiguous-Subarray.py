# Find Largest sum contiguous Subarray

# Kadane's Algorithm

# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

array = [ 4 , 2 , -3 , 1 , 6 ]
ans = []
max_sum = - 1 * max ( array )

for interval_length in range ( 1 , len ( array ) ) :
    
    for index in range ( 0 , len ( array ) - interval_length ) :
        
        temp = array [ index : index + interval_length + 1 ]
        
        if sum ( temp ) > max_sum :
            max_sum = sum ( temp ) 
            ans = temp.copy()

print ( max_sum , ans )
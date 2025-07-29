def fun2(arr):
    result = []
    for i in arr:
        if i % 2 == 0:  # Check if the number is divisible by 2
            result.append(i)  # Add the number to the result list

    # Further filter the result to include only specific numbers
    final_result = []
    for i in result:
        if i in [2, 6, 10]:  # Keep only 2, 6, and 10
            final_result.append(i)
    
    return final_result

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fun2(arr))  # Output: [2, 6, 10]
data = [40,50,60,70,80]

def add_data(value):
    """Add a data point to the global list."""
    data.append(value)

def calculate_mean():
    """Calculate the mean of the data."""
    if not data:
        return None
    return sum(data) / len(data)

def calculate_mad():
    """Calculate the Mean Absolute Deviation (MAD)."""
    if not data:
        return None
    mean = calculate_mean()
    deviations = [abs(x - mean) for x in data]
    return sum(deviations) / len(deviations)

def calculate_median():
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n//2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]
    
def calculate_variance():
    """Calculate the variance of the data."""
    if not data:
        return None
    mean = calculate_mean()
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(squared_diffs)

# Example usage:
add_data(10)
add_data(20)
add_data(30)

mean = calculate_mean()
mad = calculate_mad()

print(f"Mean: {mean}")
print(f"MAD: {mad}")
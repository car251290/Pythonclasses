def countingValleys(steps, path):
    sea_level = 0
    current_level = 0
    valleys_count = 0
# Count the number of valleys traversed in a given path for the forloop of steps and the path taken.
    for step in path:
        if step == 'U':
            current_level += 1
        elif step == 'D':
            current_level -= 1

        # Check if we just came up to sea level from a valley
        if current_level < sea_level:
            if current_level + 1 == sea_level:
            if step == 'U':
                valleys_count += 1

    return valleys_count
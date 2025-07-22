def minimumBribes(q):
    #Make a variable equal to zero to count the number of bribes
    count = 0
    for i in range(len(q)):
    #check if the queue is already on two positions than one position
        if q[i] - (i +1) >2:
            print("Too chaotic")
            return
        #check the range of the queue to see how many bribes have to been counted
        for j in range(max(q[i] -2 , 0 ), i):
            if q[j] > q[i]:
                count += 1
    print(count)
    return count
minimumBribes([2, 1, 5, 3, 4])  # Example usage

# sort a list in Python
# sorting list on Python
# number list
numList = [1, 2, 3, 4, 5]
# list of fruits

stringList = ["banana", "orange", "apple"]

# make a list of cars
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

## reverse the list for the cars
cars.sort(reverse=True)

print (cars)



# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)


# exercises with the list 
#The task is to take two lists and print the index of every value that matches using a for loop

a = [0,1,2,3,4,6,4,5,8]
b = [0,5,6,7,4,6,3,5,8]
# it will be added to a new list
newlist = []

for index in range(len(a)):
    if a[index] == b[index]: 
        newlist.append(index)

print(newlist)
       
# exercise 2

# Optimized Python program for implementation of Bubble Sort
 
#def bubbleSort(arr):
    #arr = [64, 34, 25, 12, 22, 11, 90]
   # n = len(arr)
     
    # Traverse through all array elements
   # for i in range(n):
    #    swapped = False
 
        # Last i elements are already in place
     #   for j in range(0, n - i -1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
      #      if arr[j] > arr[j+1]:
       #         arr[j], arr[j+1] = arr[j+1], arr[j]
        #        swapped = True
        #if (swapped == False):
  #          break
 #
 
# Driver code to test above
#if __name__ == "__main__":
 #   arr = [64, 34, 25, 12, 22, 11, 90]
 
  #  bubbleSort(arr)
 
    #print("Sorted array:")
   # for i in range(len(arr)):
     #   print("%d" % arr[i], end=" ")
        
        
     
# icode solution 
# for the solution of burble sort
#unordered_list = [3,4,22,8547,-12,48375,2,0,99,101,543,-123,-55,44,100,10]

# forloop in the range of the len
#for i in range(len(unordered_list)):
 #   for k in range(i):
  #      if unordered_list[i] > unordered_list[k]:
   #         temp = unordered_list[k]
    #        unordered_list[k] = unordered_list[i]
     #       unordered_list[i] = temp
      #      print(unordered_list)
       #     input("###")
#print(unordered_list)


# solution 3 for this problem will be 
#def sort():
 #   try:
  #      n = [1,8,6]
   #     l = len(n)
    #    print("Original list:", n)
     #   for i in range(l - 1):
      #      for j in range(0,l - i - 1):
       #         if n[j] > n[j + 1]:
        #            n[j], n[j + 1] = n[j + 1], n[j]
       # print("List after sorting is:", n)
    #except:
     #   print("Error in inputing values")


#sort()
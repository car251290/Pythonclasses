#def bubbleSort():
  # arr = [3,4,22,8547,-12,48375,2,0,99,101,543,-123,-55,44,100,10]
   
#def sort():
    ## sort the value in Python!!
 #   try:
  #      n = [3,4,22,8547,-12,48375,2,0,99,101,543,-123,-55,44,100,10]
   #     list = len(n)
    #    print("Original list:", n)
     #   for i in range(list - 1):
      #      for j in range(0,list - i - 1):
       #         # compare if the element has not been sorter yet
        #        if n[j] > n[j + 1]:
         #           n[j], n[j + 1] = n[j + 1], n[j]
        #print("List after sorting is:", n)
    #except:
     #   print("Error in inputing values")


#sort()

# solution 2
def bubbleSort(list):
    n = len(list)
    for i in range(n - 1):
        swap = 0
        for k in range(n -1):
            if list[k] > list[ k + 1]:
                temp = list[k]
                list[k] = list[k + 1]
                list[ k+ 1] = temp
                swap = 1
        if swap == 0:
            break
    return list

arr = [21,6,9,1,33]

result = bubbleSort(arr)

print(result)



    
from random import random

from pendulum import time
import pendulum

#Bubble Sort Algorithm
def bubbleSort(data):        
    lenght = len(data)
    for iIndex in range(lenght):            
        swapped = False
        for jIndex in range(0, lenght - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:                    
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]                    
                swapped = True
        if swapped == False:                
            break
    #print(data)
    
#Selection Sort Algorithm
def selectionSort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):                
            if data[compIndex] < data[minIndex]:                    
                minIndex = compIndex
        if minIndex != scanIndex:               
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]
            #print(data)
                
 #Insertion Sort Algorithm
def insertionSort(data):
    for scanIndex in range(1, len(data)):            
        tmp = data[scanIndex]
        minIndex = scanIndex
        while minIndex > 0 and tmp < data[minIndex - 1]:                
            data[minIndex] = data[minIndex - 1]                
            minIndex -= 1
        data[minIndex] = tmp
        #print(data)
        
        
#Quick sort        
def partition(lst, start, end):
    pos = start                           
                                          

    for i in range(start, end):          
        if lst[i] < lst[end]:             
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos] 
                                         
    return pos

def quick_sort_recursive(lst, start, end):
    if start < end:                       
        pos = partition(lst, start, end)
        quick_sort_recursive(lst, start, pos - 1)
        quick_sort_recursive(lst, pos + 1, end)
                                          
                                         
#Merge Sort Algorithm
def mergeSort(data):        
    if len(data) < 2:            
        return data
    middle = len(data)//2
    left = mergeSort(data[:middle])        
    right = mergeSort(data[middle:])
    # print("The left side is: ", left)        
    # print("The right side is: ", right)
    merged = merge(left, right)
    # print("Merged ", merged)        
    return merged    

def merge(left, right):        
    if not len(left):            
        return left
    if not len(right):            
        return right
    result = []        
    leftIndex = 0        
    rightIndex = 0        
    totalLen = len(left) + len(right)
    while (len(result) < totalLen):
        if left[leftIndex] < right[rightIndex]:                
            result.append(left[leftIndex])                
            leftIndex += 1            
        else:                
            result.append(right[rightIndex])                
            rightIndex += 1
        if leftIndex == len(left) or rightIndex == len(right):                
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
    return result


#Bucket Sort Algorithm
def bucketSort(data):        
    bucket = []
    for iIndex in range(len(data)):           
        bucket.append([])
    for jIndex in data:            
        index_bucket = int(10 * jIndex)            
        bucket[index_bucket].append(jIndex)            
        # print(bucket)
    for iIndex in range(len(data)):           
        bucket[iIndex] = sorted(bucket[iIndex])
        kIndex = 0
        for iIndex in range(len(data)):
            for jIndex in range(len(bucket[iIndex])):                    
                data[kIndex] = bucket[iIndex][jIndex]                    
                kIndex += 1
    #print(data)


#Shell Sort Algorithm
def shellSort(data, length):
    gap = length//2
    while gap > 0:            
        for iIndex in range(gap, length):
            temp = data[iIndex]
            jIndex = iIndex
            while jIndex >= gap and data[jIndex - gap] > temp:                    
                data[jIndex] = data[jIndex - gap]
                jIndex -= gap
            data[jIndex] = temp
        gap //= 2
    #print(data)
    
 #Heap Sort Algorithm
def createHeap(data, length, index):
    largest = index        
    left = 2 * index + 1        
    right = 2 * index + 2
    if left < length and data[index] < data[left]:            
        largest = left
    if right < length and data[largest] < data[right]:            
        largest = right
    if largest != index:            
        data[index], data[largest] = data[largest], data[index]            
        createHeap(data, length, largest)
        
def heapSort(data):        
    length = len(data)
    #We build max heap
    for index in range(length, 0, -1):            
        createHeap(data, length, index)
    for index in range(length -1, 0, -1):           
        data[index], data[0] = data[0], data[index]
        createHeap(data, index, 0)
    #print(data)
    
    
data_to_sort = [ random() for i in range(0, 100000)  ] 

time_start = pendulum.now()
bubbleSort(data_to_sort)
time_end = pendulum.now()
print("bubbleSort time", time_end - time_start)

time_start = pendulum.now()
selectionSort(data_to_sort)
time_end = pendulum.now()
print("selectionSort time", time_end - time_start)

time_start = pendulum.now()
insertionSort(data_to_sort)
time_end = pendulum.now()
print("insertionSort time", time_end - time_start)

time_start = pendulum.now()
mergeSort(data_to_sort)
time_end = pendulum.now()
print("mergeSort time", time_end - time_start)

time_start = pendulum.now()
bucketSort(data_to_sort)
time_end = pendulum.now()
print("bucketSort time", time_end - time_start)

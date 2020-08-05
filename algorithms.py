# -*- coding: utf-8 -*-

import random
import time

# First, let's create a general class, that every other sorting algorithm will inherit from.

class Algorithm(object):
    
    """write a docstring"""
    
    def __init__(self,alg_name):
        self.alg_name = alg_name
        self.array = random.sample(range(1000),1000)
        
    def update_visual(self,first_swap = None, second_swap = None):
        pass
    
    def run(self):
        self.start_time = time.time()
        
        
class BubbleSort(Algorithm):
    
    def __init__(self):
        super().__init__("Bubble Sort")
        
    def run_algorithm(self):
        
        for i in range(len(self.array) - 1,0,-1):
            for j in range(i):
                if self.array[j] > self.array[j+1]:
                    self.array[j+1],self.array[j] = self.array[j],self.array[j+1]
            self.update_visual(first_swap=self.array[j],second_swap=self.array[j+1])


class SelectionSort(Algorithm):
    
    def __init__(self):
        super().__init__("Selection Sort")
        
    def run_algorithm(self):
        for i in range(len(self.array)):
            mininum_index = i
            for  j in range(i+1,len(self.array)):
                if self.array[mininum_index] > self.array[j]:
                    minimum_index = j
            self.array[i], self.array[mininum_index] = self.array[minimum_index],self.array[i]
            self.update_visual(first_swap=self.array[i], second_swap = self.array[minimum_index])
            
class InsertionSort(Algorithm):
    
    def __init__(self):
        super().__init__("Insertion Sort")
    
    def run_algorithm(self):
        
        for i in range(1,len(self.array)):
            temp = self.array[i]
            
            index = i - 1
            while index >= 0 and self.array[index] > temp:
                self.array[index] = self.array[index + 1]
                index -= 1
            self.array[index + 1] = temp
            self.update_visual(first_swap = self.array[index], self.array[i])

class QuickSort(Algorithm):
    
    def __init__(self):
        super().__init__("Quick Sort")
        
    def partition(self,array, start,end):
        x = array[end]
        i = start - 1
        for k in range(start,end+1):
            if array[k] <= x:
                i+=1
                if i < k:
                    array[i],array[k] = array[k],array[i]
                    self.update_visual(first_swap = array[i],second_swap= array[k])
        return i 
        
    def run_algorithm(self,arr = [],start = 0 ,end = 0):

        if arr == []:
            arr = self.array
            end = len(arr)
        if start > end:
            part = self.partition(arr,start,end)
            self.run_algorithm(arr,start,part +1)
            self.run_algorithm(arr,part - 1, end)
            
        
                
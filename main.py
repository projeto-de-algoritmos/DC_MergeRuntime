   
import numpy as np
import random
import time
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def Merge_A(left,right,A):
    i=j=k=0
    start_time = time.time()
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            A[k]=left[i]
            i+=1

        else:
            A[k]=right[j]
            j+=1

        k+=1

    while(i < len(left)):
        A[k]=left[i]
        i+=1
        k+=1

    while(j < len(right)):
        A[k]=right[j]
        j+=1
        k+=1

    end_time = time.time() - start_time
    
    global conquer_time_a
    conquer_time_a += end_time

def Merge_B(left,right,A):
    i=j=k=0
    start_time = time.time()
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            A[k]=left[i]
            i+=1

        else:
            A[k]=right[j]
            j+=1

        k+=1

    while(i < len(left)):
        A[k]=left[i]
        i+=1
        k+=1

    while(j < len(right)):
        A[k]=right[j]
        j+=1
        k+=1

    end_time = time.time() - start_time

    global conquer_time_b
    conquer_time_b += end_time

def Merge_C(left,right,A):
    i=j=k=0
    start_time = time.time()
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            A[k]=left[i]
            i+=1

        else:
            A[k]=right[j]
            j+=1

        k+=1

    while(i < len(left)):
        A[k]=left[i]
        i+=1
        k+=1

    while(j < len(right)):
        A[k]=right[j]
        j+=1
        k+=1

    end_time = time.time() - start_time

    global conquer_time_c
    conquer_time_c += end_time

def Merge_D(left,right,A):
    i=j=k=0
    start_time = time.time()
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            A[k]=left[i]
            i+=1

        else:
            A[k]=right[j]
            j+=1

        k+=1

    while(i < len(left)):
        A[k]=left[i]
        i+=1
        k+=1

    while(j < len(right)):
        A[k]=right[j]
        j+=1
        k+=1

    end_time = time.time() - start_time

    global conquer_time_d
    conquer_time_d += end_time

def Merge_E(left,right,A):
    i=j=k=0
    start_time = time.time()
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            A[k]=left[i]
            i+=1

        else:
            A[k]=right[j]
            j+=1

        k+=1

    while(i < len(left)):
        A[k]=left[i]
        i+=1
        k+=1

    while(j < len(right)):
        A[k]=right[j]
        j+=1
        k+=1

    end_time = time.time() - start_time

    global conquer_time_e
    conquer_time_e += end_time

def MergeSort_A(A):
    start_time = time.time()
    left = []
    right = []
    n = len(A)
    if(n<2):
        return
    mid = n/2
    for i in range(int(mid)):
        left.append(A[i])
    for i in range(int(mid),n):
        right.append(A[i])
    
    end_time = time.time() - start_time

    global divide_time_a 
    divide_time_a += end_time

    MergeSort_A(left)
    MergeSort_A(right)
    Merge_A(left,right,A)

def MergeSort_B(A):
    start_time = time.time()
    left = []
    right = []
    n = len(A)
    if(n<2):
        return
    mid = n/2
    for i in range(int(mid)):
        left.append(A[i])
    for i in range(int(mid),n):
        right.append(A[i])
    
    end_time = time.time() - start_time

    global divide_time_b 
    divide_time_b += end_time
    
    MergeSort_B(left)
    MergeSort_B(right)
    Merge_B(left,right,A)

def MergeSort_C(A):
    start_time = time.time()
    left = []
    right = []
    n = len(A)
    if(n<2):
        return
    mid = n/2
    for i in range(int(mid)):
        left.append(A[i])
    for i in range(int(mid),n):
        right.append(A[i])
    
    end_time = time.time() - start_time

    global divide_time_c 
    divide_time_c += end_time
    MergeSort_C(left)
    MergeSort_C(right)
    Merge_C(left,right,A)

def MergeSort_D(A):
    start_time = time.time()
    left = []
    right = []
    n = len(A)
    if(n<2):
        return
    mid = n/2
    for i in range(int(mid)):
        left.append(A[i])
    for i in range(int(mid),n):
        right.append(A[i])
    
    end_time = time.time() - start_time

    global divide_time_d 
    divide_time_d+= end_time
    MergeSort_D(left)
    MergeSort_D(right)
    Merge_D(left,right,A)

def MergeSort_E(A):
    start_time = time.time()
    left = []
    right = []
    n = len(A)
    if(n<2):
        return
    mid = n/2
    for i in range(int(mid)):
        left.append(A[i])
    for i in range(int(mid),n):
        right.append(A[i])
    
    end_time = time.time() - start_time

    global divide_time_e 
    divide_time_e += end_time
    MergeSort_E(left)
    MergeSort_E(right)
    Merge_E(left,right,A)

    
divide_time_a = 0
conquer_time_a = 0
divide_time_b = 0 
conquer_time_b = 0
divide_time_c = 0 
conquer_time_c = 0
divide_time_d = 0 
conquer_time_d = 0
divide_time_e = 0 
conquer_time_e = 0

vector_a = random.sample(range(1,101), 100)
vector_b = random.sample(range(1,1001), 1000)
vector_c = random.sample(range(1,10001), 10000)
vector_d = random.sample(range(1,100001), 100000)
vector_e = random.sample(range(1,1000001), 1000000)


MergeSort_A(vector_a)
MergeSort_B(vector_b)
MergeSort_C(vector_c)
MergeSort_D(vector_d)
MergeSort_E(vector_e)

final_arr_1 = []
final_arr_2 = []
total_arr = []

total_arr.append(divide_time_a + conquer_time_a);
total_arr.append(divide_time_b + conquer_time_b);
total_arr.append(divide_time_c + conquer_time_c);
total_arr.append(divide_time_d + conquer_time_d);
total_arr.append(divide_time_e + conquer_time_e);

final_arr_1.append(divide_time_a)
final_arr_1.append(divide_time_b)
final_arr_1.append(divide_time_c)
final_arr_1.append(divide_time_d)
final_arr_1.append(divide_time_e)

final_arr_2.append(conquer_time_a)
final_arr_2.append(conquer_time_b)
final_arr_2.append(conquer_time_c)
final_arr_2.append(conquer_time_d)
final_arr_2.append(conquer_time_e)

print("A(100) - ","DIV: ", divide_time_a, " CONQ: ", conquer_time_a, " DIV/CONQ: ", "0")
print("B(1000) - ","DIV: ", divide_time_b, " CONQ: ", conquer_time_b, " DIV/CONQ: ", divide_time_b/conquer_time_b)
print("C(10000) - ","DIV: ", divide_time_c, " CONQ: ", conquer_time_c, " DIV/CONQ: ", divide_time_c/conquer_time_c)
print("D(100000) - ","DIV: ", divide_time_d, " CONQ: ", conquer_time_d, " DIV/CONQ: ", divide_time_d/conquer_time_d)
print("E(10000000) - ","DIV: ", divide_time_e, " CONQ: ", conquer_time_e, " DIV/CONQ: ", divide_time_e/conquer_time_e)

y = [100, 1000, 10000, 100000, 10000000]



plt.plot(final_arr_1, y, color='red')
plt.plot(final_arr_2, y, color='blue')
plt.plot(total_arr, y, color='green')

plt.title("Comparação Tempo de Divisão/Conquista no MergeSort")
red_patch = mpatches.Patch(color='red', label='Dividir')
blue_patch = mpatches.Patch(color='blue', label='Conquistar')
green_patch = mpatches.Patch(color='green', label='Total')

plt.legend(handles=[red_patch, blue_patch, green_patch])
plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho do vetor(Milhões)')
plt.grid(color='r', linestyle='-', linewidth=0.2)
plt.show()
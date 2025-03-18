# Problem - 1

def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1 

arr = [2, 4, 5, 1, 2, 3]
result = find_equilibrium_index(arr)

if result != -1:
    print(f"The equilibrium index is: {result}")
else:
    print("No equilibrium index found")

# Problem - 2

from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(set)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].add(word)
    return list(anagrams.values())

words = ['cat', 'dog', 'god']
result = group_anagrams(words)
print(result)

# Problem - 3

def binary_search(arr, target, find_first):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            if find_first:
                # Move left to find the first occurrence
                high = mid - 1
            else:
                # Move right to find the last occurrence
                low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result

def find_first_and_last(arr, key):
    first_index = binary_search(arr, key, True)
    if first_index == -1:
        return -1, -1
    last_index = binary_search(arr, key, False)
    return first_index, last_index

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
key = 5
first, last = find_first_and_last(arr, key)

print(f"First occurrence: {first}, Last occurrence: {last}")

# Problem - 4

def find_substring(s,k):
    substr_list=[]
    j=len(s)-k+1
    for i in range(j):
        substr_list.append(s[i:i+k])
    return sorted(substr_list)

s="stack"
k=3
s1=find_substring(s,k)
print(f"Smallest substring of size k is {s1[0]}")
print(f"Largest substring of size k is {s1[-1]}")
    
# Problem - 5

def sort_frequency(s):
    d={}
    ans=""
    for item in s:
        if item in d.keys():
            d[item]+=1
        else:
            d[item]=1
    s1=sorted(d.items(),key=lambda item: (item[1], item[0]))
    sorted_keys = [ item[0] for item in s1 ]
    for item in sorted_keys:
            ans+=item*d[item]
        
    return ans

s="stations"
print(sort_frequency(s))
    
# Problem - 6

def minCost(f):
    cost=0
    while(len(f)>1):
        min1=min(f)
        f.remove(min1)
  
        min2=min(f)
        f.remove(min2)
  
        f.append(min1+min2)
        cost= cost+min1+min2
    return cost

orders= [14, 25, 5, 8 ]
cst=minCost(orders)
print(cst)

# Problem - 7

def find_pairs(a,k):
    count=0
    left=0
    right=len(a)-1
    while(left<right):
        s=a[left]+a[right]
        if s==k:
            print(a[left],a[right],k)
            count+=1
            left+=1
            right-=1
        elif s>k:
            right=right-1
        else:
            left=left+1
    if count==0:
        print(-1)

a=[1, 2 ,3, 4 ,5 ,6, 7]
k=8
find_pairs(a,k)

# Problem - 8

def find_triplet(arr, x):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):  
        left, right = i + 1, n - 1 
        
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            
            if total == x: 
                return 1  
            elif total < x:
                left += 1  
            else:
                right -= 1      
    return 0 

arr = [1, 4, 45, 6, 10, 8]
x = 13
print(find_triplet(arr, x))

# Problem - 9

def hailstone_sequence_iterative(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    sequence.append(1)
    return sequence

n = 17
result_iterative = hailstone_sequence_iterative(n)
print(result_iterative)

# Problem - 10

import math

def prime(n):
    s=int(math.sqrt(n))+1
    flag=0
    if n>1:
        for i in range(2,s):
            if n%i==0:
                flag=1
                break
        if flag==0:
            return True
    else:
        return False

def find_pair(n):
    for i in range(n):
        if prime(i):
            left=n-i
            if prime(left):
                print(i,left)

n=74
find_pair(74)

# Problem - 11

def rotate(mat,n):
    for i in range(n):
        for j in range(i,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    
    for i in range(n):
        j=0
        k=n-1
        while j<k:
            temp=mat[j][i]
            mat[j][i]=mat[k][i]
            mat[k][i]=temp
            j+=1
            k-=1
    
n=3
a=[1,2,3,4,5,6,7,8,9]
mat=[[0 for j in range(n)] for i in range(n)]
k=0
for i in range(n):
    for j in range(n):
        mat[i][j]=a[k]
        k+=1
rotate(mat,n)
for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
print()

# Problem - 12

def search_in_sorted_matrix(matrix, x):
    n = len(matrix)
    i, j = 0, n - 1

    while i < n and j >= 0:
        if matrix[i][j] == x:
            print(i, j)
            return
        elif matrix[i][j] > x:
            j -= 1
        else:
            i += 1
    print("Not Found")

matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
x = 29
search_in_sorted_matrix(matrix, x)

# Problem - 13

def swap(a,n):
    i=0
    j=1
    while(i<n and j<n):
        while(i<n and a[i]%2 == 0):
            i+=2
        while(j<n and a[j]%2 == 1):
            j+=2
        if i< n and j<n:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp


a=[4,2,5,7]
n=len(a)
swap(a,n)
print(*a)

# Problem - 14

def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

arr = [0, 1, 2, 0, 1, 2]
sorted_arr = sort_array(arr)
print(sorted_arr)

# Problem - 15

def print_boundary(mat,r,c):
        for j in range(c):
            print(mat[0][j],end=" ")
        for i in range(1,r-1):
            print(mat[i][0],end=" ")
            print(mat[i][c-1],end=" ")
        for x in range(c):
            print(mat[r-1][x],end=" ")
        print()

mat= [[1,2,3,4],
	 [5,6,7,8],
	 [1,2,3,4],
	 [5,6,7,8]]
rows=len(mat)
columns=len(mat[0])
print(rows,columns)
print_boundary(mat,rows,columns)

# Problem - 16

def print_boundary_sum(mat,r,c):
    sum=0
    for i in range(r):
        for j in range(c):
            if i==0 or j==0 or i==r-1  or j==c-1:
                sum+=mat[i][j]
    print(sum)
                
mat= [[1,2,3,4],
	 [5,6,7,8],
	 [1,2,3,4],
	 [5,6,7,8]]
rows=len(mat)
columns=len(mat[0])
print(rows,columns)
print_boundary_sum(mat,rows,columns)

# Problem - 17

def swap(x):
    start = 0
    end=len(x)-1
    while(start<=end):
        if x[start]>=0:
            x[start],x[end],x[start]
            end=end-1
        else:
            start=start+1

x=[-4,8,0,-9,-11,6,5]
swap(x)
print(*x)

# Problem - 18

def max_sum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i],current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = [-2,-3,4,-1,-2,1,5,-3]
print(max_sum_subarray(arr))

# Problem - 19

def sort_array(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] == 1 and arr[high] == 0:
            arr[low], arr[high] = arr[high], arr[low]
        
        if arr[low] == 0:
            low+= 1
        if arr[high] == 1:
            high-= 1
    return arr

arr = [1, 1, 0, 0, 1, 1, 0, 1, 0]
print(sort_array(arr))

# Problem - 20

def rotate_array(arr,d):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]

arr = [1,2,3,4,5,6,7]
d=2
rotated_array = rotate_array(arr,d)
print(rotated_array)

# Problem -21

def rotate_array_clockwise(arr,d):
    n = len(arr)
    d = d % n
    return arr[-d:] + arr[:-d]

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotated_arr = rotate_array_clockwise(arr, d)
print(rotated_arr)

# Problem - 22

def subarray_with_given_sum(arr , target_sum):
    n = len(arr)
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum+= arr[end]
        while current_sum > target_sum and start<= end:
            current_sum -= arr[start]
            start +=1
        if current_sum ==target_sum:
            return start,end
    return -1

arr = [4, 8, 0, 9, 11, 6, 5]
target_sum = 22
result = subarray_with_given_sum(arr, target_sum)

if result != -1:
    print(f"Subarray found between indices: {result[0]}, {result[1]}")
else:
    print("No subarray with the given sum found")

# Problem - 23

arr = [1,2,2,3,4,1]
count = 0
n =len(arr)
for i in range(n):
    Sum = arr[i]
    if Sum % 2 == 0:
        count += 1
    for j in range(i+1,n):
        Sum += arr[j]
        if Sum %2 == 0:
            count += 1
print(count)

# Problem - 24

def majority_element(x,n):
        l=[0]*(max(x)+1)
        for i in range(n):
                l[x[i]]=l[x[i]]+1
        m=max(l)
        if m > n/2:
                return l.index(max(l))
        return -1

x=[3,1,3,3,2]
n=len(x)
ans=majority_element(x,n)
print(ans)

# Problem - 25

def peak_element(x,n):
        if x[0]>x[1]:
                print(x[0],end=" ")
        if x[n-1]>x[n-2]:
                print(x[n-1],end=" ")
        for i in range(1,n-1):
                if x[i]>x[i-1] and x[i]>x[i+1] :
                        print(x[i],end=" ")

x=[10, 20, 15, 2, 23, 90, 67]
n=len(x)
peak_element(x,n)

# Problem - 26

def leaders(x,n):
        *l,last= x
        l1=[]
        l1.append(last)
        for j in reversed(l):
                if j>=last:
                        l1.append(j)
                        last=j
        l1.reverse()
        return l1

x=[16 ,17, 4, 3 ,5, 2]
n=len(x)
l=leaders(x,n)
print(*l)

# Problem - 27

def find_first_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            first_occurrence = mid
            right = mid - 1 
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence

def find_last_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    last_occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            last_occurrence = mid
            left = mid + 1  
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return last_occurrence

def count_occurrences(arr, x):
    first = find_first_occurrence(arr, x)
    if first == -1: 
        return 0
    last = find_last_occurrence(arr, x)
    return last - first + 1

arr = [1, 1, 2, 2, 2, 2, 3]
x = 2
print(count_occurrences(arr, x))

# Problem - 28

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False  

    for start in range(2, int(n**0.5) + 1):
            for multiple in range(start * start, n + 1, start):
                sieve[multiple] = False
    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes

n = 10
primes_up_to_n = sieve_of_eratosthenes(n)
print(primes_up_to_n)

# Problem - 29

def max_ones_row(matrix, N, M):
    max_count = -1
    row_index = -1
    
    for i in range(N):
        count_ones = 0
        for j in range(M):
            if matrix[i][j] == 1:
                count_ones += 1
        if count_ones > max_count:
            max_count = count_ones
            row_index = i
    return row_index

N = 3
M = 4
Mat = [[0, 1, 1, 1],
       [0, 0, 1, 1],
       [0, 0, 1, 1]]

print(max_ones_row(Mat, N, M))

# Problem - 30

def transition(a, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if a[mid] == 1 and (mid == 0 or a[mid - 1] == 0):
        return mid
    elif a[mid] == 1:
        return transition(a, start, mid - 1)
    else:
        return transition(a, mid + 1, end)

a = [0, 0, 0, 1, 1]
index = transition(a, 0, len(a) - 1)
print(index)

# Problem - 31

import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(n, m):
    primes = []
    for i in range(n, m + 1):
        if is_prime(i):
            primes.append(i)
    return primes

n = 1
m = 10
result = primes_in_range(n, m)
print(" ".join(map(str, result)))

# Problem - 32

def convert_to_reduced_form(arr):
    sorted_arr = sorted(arr)
    rank_map = {value: index for index, value in enumerate(sorted_arr)}
    reduced_form = [rank_map[value] for value in arr]
    return reduced_form

arr = [10, 40, 20, 50]
result = convert_to_reduced_form(arr)
print(result)

# Problem - 33

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

def check_prime_from_sum_of_digits(num):
    single_digit_sum = sum_of_digits(num)
    if is_prime(single_digit_sum):
        return "Prime"
    else:
        return "Non-Prime"

num = 5601
result = check_prime_from_sum_of_digits(num)
print(result)

# Problem - 34

def find_sum(n):
    s=0
    while(n):
        s+=n%10
        n=n//10
    return s

n=5601
while(n//10):
    n=find_sum(n)
print(n)
    
# Problem - 35

def alternative_sort(arr):
    arr.sort()
    left = 0  
    right = len(arr) - 1
    result = []
    
    while left <= right:
        if left <= right:
            result.append(arr[right])
            right -= 1
        if left <= right:
            result.append(arr[left])
            left += 1
    return result

arr = [7, 1, 2, 3, 4, 5, 6]
result = alternative_sort(arr)
print(" ".join(map(str, result)))

# Problem - 36

def find_row_with_min_ones(N,M,matrix):
    min_ones = M + 1
    row_index = -1
    for i in range(N):
        ones_count = matrix[i].count(1)
        if ones_count < min_ones:
            min_ones = ones_count
            row_index = 1
    if min_ones == 0:
        return -1
    return row_index

N, M = 4, 4
matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
result = find_row_with_min_ones(N, M, matrix)
print(result)

# Problem - 37

def modify_matrix(mat,n,m):
    rows_to_update = [False] * n
    cols_to_update = [False] * m
    for i in range(n):
        for j in range(m):
            if mat [i][j] == 1:
                rows_to_update[i] = True
                cols_to_update[j] = True
    for i in range(n):
        for j in range(m):
            if rows_to_update[i] or cols_to_update[j]:
                mat[i][j] = 1
    return mat

n = 2
m = 2
mat = [
    [1, 0],
    [0, 0]
]
result = modify_matrix(mat, n, m)
for row in result:
    print(" ".join(map(str, row)))

# Problem - 38

def lcs(a):
        a.sort()
        c=1
        m=1
        for i in range(1,len(a)):
                if a[i]-a[i-1]==1:
                        c+=1
                        m=max(c,m)
                else:
                        c=1
        return m
                
a=[2, 6, 1 ,9 ,4, 5 ,3]
ans=lcs(a)
print(ans)

# Problem - 39

import math
def prime(n):
    if n>1:
        s=int(math.sqrt(n))+1
        flag=0
        for i in range(2,s):
            if n%i==0:
                flag=1
                break
        if flag==0:
            return True
        else:
            return False

def find_sum(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s

a=4
sum2=0
sum1=find_sum(a)
if prime(a):
    print("N0")
else:
    for i in range(2,a):
        while a%i==0:
            sum2=sum2+find_sum(i)
            a=a//i
    if sum1==sum2:
        print("YES")
    else:
        print("NO")
            
# Problem - 40

def first_k_missing_numbers(N, K, arr):
    present_numbers = set(arr)
    missing_numbers = []
    current_number = 1
    while len(missing_numbers) < K:
        if current_number not in present_numbers:
            missing_numbers.append(current_number)
        current_number += 1
    return missing_numbers

N = 3
K = 3
arr = [2, 3, 4]
result = first_k_missing_numbers(N, K, arr)
print(" ".join(map(str, result)))
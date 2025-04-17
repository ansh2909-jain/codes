import unittest
import math
from collections import defaultdict

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    
    def test_add_positive(self):
        self.assertEqual(add(2, 4), 6)

    def test_add_negative(self):
        self.assertEqual(add(-4, -6), -10)

    def test_add(self):
        self.assertEqual(add(0, 6), 6)
        self.assertEqual(add(0, 0), 0)

    def test_add_mix(self):
        self.assertEqual(add(-3, 9), 6)

if __name__ == '__main__':
    unittest.main()

#####

def is_sum_equal(a, b, expected_sum):
    return (a + b) == expected_sum

class TestIsSumEqual(unittest.TestCase):

    def test_correct_sum(self):
        self.assertTrue(is_sum_equal(2, 7, 9))   

    def test_incorrect_sum(self):
        self.assertFalse(is_sum_equal(2, 6, 9))   

    def test_with_zero(self):
        self.assertTrue(is_sum_equal(0, 0, 0))    
        self.assertFalse(is_sum_equal(0, 4, 7))

    def test_negative_numbers(self):
        self.assertTrue(is_sum_equal(-2, -7, -9))     
        self.assertFalse(is_sum_equal(-2, 2, -1))     

if __name__ == '__main__':
    unittest.main()

#####

def find_equilibrium_index(arr): 
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1 

class TestEquilibriumIndex(unittest.TestCase):

    def test_equilibrium_exists(self):
        self.assertEqual(find_equilibrium_index([2, 4, 5, 1, 2, 3]), 2) 

    def test_no_equilibrium(self):
        self.assertEqual(find_equilibrium_index([1, 2, 3]), -1)

    def test_equilibrium_at_start(self):
        self.assertEqual(find_equilibrium_index([0, -3, 3]), 0)

    def test_equilibrium_at_end(self):
        self.assertEqual(find_equilibrium_index([1, 2, 3, 0, 3, 2, 1]), 3)

    def test_single_element(self):
        self.assertEqual(find_equilibrium_index([10]), 0)

    def test_empty_list(self):
        self.assertEqual(find_equilibrium_index([]), -1)

if __name__ == '__main__':
    unittest.main()

#####

def group_anagrams(words):
    anagrams = defaultdict(set)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].add(word)
    return list(anagrams.values())

class TestGroupAnagrams(unittest.TestCase):

    def test_basic_anagrams(self):
        words = ['cat', 'dog', 'god']
        result = group_anagrams(words)
        expected = [{'cat'}, {'dog', 'god'}]
        self.assertCountEqual(result, expected)

    def test_with_duplicates(self):
        words = ['bat', 'tab', 'bat']
        result = group_anagrams(words)
        expected = [{'bat', 'tab'}]  
        self.assertCountEqual(result, expected)

    def test_no_anagrams(self):
        words = ['apple', 'banana', 'cherry']
        result = group_anagrams(words)
        expected = [{'apple'}, {'banana'}, {'cherry'}]
        self.assertCountEqual(result, expected)

    def test_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_single_word(self):
        self.assertEqual(group_anagrams(['hello']), [{'hello'}])

if __name__ == '__main__':
    unittest.main()

#####

def find_substring(s, k):
    substr_list = []
    j = len(s) - k + 1
    for i in range(j):
        substr_list.append(s[i:i + k])
    return sorted(substr_list)

class TestFindSubstring(unittest.TestCase):

    def test_regular_case(self):
        s = "stack"
        k = 3
        result = find_substring(s, k)
        expected = ['ack', 'sta', 'tac'] 
        self.assertEqual(result, expected)
        self.assertEqual(result[0], 'ack')  
        self.assertEqual(result[-1], 'tac') 

    def test_full_string_as_substring(self):
        s = "abc"
        k = 3
        result = find_substring(s, k)
        self.assertEqual(result, ['abc'])

    def test_single_char_substrings(self):
        s = "abc"
        k = 1
        result = find_substring(s, k)
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_k_larger_than_length(self):
        s = "abc"
        k = 4
        result = find_substring(s, k)
        self.assertEqual(result, []) 

    def test_empty_string(self):
        s = ""
        k = 2
        result = find_substring(s, k)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

#####

def minCost(f):
    cost = 0
    while len(f) > 1:
        min1 = min(f)
        f.remove(min1)
        min2 = min(f)
        f.remove(min2)
        f.append(min1 + min2)
        cost += min1 + min2
    return cost

class TestMinCost(unittest.TestCase):
    def test_min_cost(self):
        self.assertEqual(minCost([14, 25, 5, 8]), 92)

if __name__ =='__main__':
    unittest.main()

#####

def find_pairs(a, k):
    pairs = []
    left = 0
    right = len(a) - 1
    while left < right:
        s = a[left] + a[right]
        if s == k:
            pairs.append((a[left], a[right]))
            left += 1
            right -= 1
        elif s > k:
            right -= 1
        else:
            left += 1
    return pairs

class TestFindPairs(unittest.TestCase):
    def test_find_pairs(self):
        self.assertEqual(find_pairs([1, 2, 3, 4, 5, 6, 7], 8), [(1, 7), (2, 6), (3, 5)])

if __name__ =='__main__':
    unittest.main()

#####

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

class TestFindTriplet(unittest.TestCase):
    def test_triplet_found(self):
        self.assertEqual(find_triplet([1, 4, 45, 6, 10, 8], 13), 1)

    def test_triplet_not_found(self):
        self.assertEqual(find_triplet([1, 2, 3], 50), 0)

if __name__ =='__main__':
    unittest.main()

#####

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

class TestHailstone(unittest.TestCase):
    def test_hailstone(self):
        self.assertEqual(hailstone_sequence_iterative(5), [5, 16, 8, 4, 2, 1])

if __name__ =='__main__':
    unittest.main()

#####

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_pair(n):
    result = []
    for i in range(n):
        if prime(i):
            left = n - i
            if prime(left):
                result.append((i, left))
    return result


class TestFindPair(unittest.TestCase):
    def test_pair_sum(self):
        self.assertIn((3, 71), find_pair(74))

if __name__ =='__main__':
    unittest.main()

#####

def rotate(mat, n):
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        j = 0
        k = n - 1
        while j < k:
            mat[j][i], mat[k][i] = mat[k][i], mat[j][i]
            j += 1
            k -= 1


class TestRotateMatrix(unittest.TestCase):
    def test_rotation(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate(mat, 3)
        self.assertEqual(mat, [[3, 6, 9], [2, 5, 8], [1, 4, 7]])


if __name__ =='__main__':
    unittest.main()

#####

def search_in_sorted_matrix(matrix, x):
    n = len(matrix)
    i, j = 0, n - 1
    while i < n and j >= 0:
        if matrix[i][j] == x:
            return (i, j)
        elif matrix[i][j] > x:
            j -= 1
        else:
            i += 1
    return None


class TestMatrixSearch(unittest.TestCase):
    def test_matrix_search(self):
        matrix = [
            [10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50]
        ]
        self.assertEqual(search_in_sorted_matrix(matrix, 29), (2, 1))

if __name__ =='__main__':
    unittest.main()

#####

def swap(a, n):
    i = 0
    j = 1
    while i < n and j < n:
        while i < n and a[i] % 2 == 0:
            i += 2
        while j < n and a[j] % 2 == 1:
            j += 2
        if i < n and j < n:
            a[i], a[j] = a[j], a[i]


class TestSwap(unittest.TestCase):
    def test_even_odd_swap(self):
        a = [4, 2, 5, 7]
        swap(a, len(a))
        self.assertEqual(a, [4, 5, 2, 7])

if __name__ =='__main__':
    unittest.main()

#####

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


class TestSortArray(unittest.TestCase):
    def test_sort_012(self):
        self.assertEqual(sort_array([0, 1, 2, 0, 1, 2]), [0, 0, 1, 1, 2, 2])

if __name__ =='__main__':
    unittest.main()

#####

def print_boundary_sum(mat, r, c):
    total = 0
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0 or i == r - 1 or j == c - 1:
                total += mat[i][j]
    return total

class TestBoundarySum(unittest.TestCase):
    def test_boundary_sum(self):
        mat = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        result = print_boundary_sum(mat, 4, 4)
        self.assertEqual(result, 54)

if __name__ == '__main__':
    unittest.main()
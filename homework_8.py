''' Problem #1 (reduce array size to halfs)
Given an array arr.  You can choose a set of integers and 
remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least 
half of the integers of the array are removed.
'''

# Time Complexity Analysis = O(n)

class Solution(object):
    def minSetSize(self, arr):
        counting_sort = [0]*len(arr)
        count = (arr)
        for c in count.itervalues():
            counting_sort[c-1] += 1
        result, total = 0, 0
        for c in reversed(len(arr)):
            if not counting_sort[c]:
                continue
            count = min(counting_sort[c],
                        ((len(arr)+1)//2 - total - 1)//(c+1) + 1)
            result += count
            total += count*(c+1)
            if total >= (len(arr)+1)//2:
                break
        return result





'''Problem # 2 (Largest Perimeter Triangle)

Given an array A of positive lengths, return the largest 
perimeter of a triangle with non-zero area, formed from 3 
of these lengths.

If it is impossible to form any triangle 
of non-zero area, return 0.
'''

# Time Complexity = O(nlogn)


class Solution(object):
    def largestPerimeter(self, listy): 
        listy.sort()
        for i in reversed(len(listy) - 2):
            if listy[i] + listy[i+1] > listy[i+2]:
                return listy[i] + listy[i+1] + listy[i+2]
        return 0
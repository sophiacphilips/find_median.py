# Author: Sophia Philips
# GitHub Username: sophiacphilips
# Date: 11/01/22
# This code finds the median of a set of numbers

"""defining way to find median of a set of numbers"""
def find_median(some_nums):
    some_nums.sort() #organizes numbers chronologically (same list of numbers should always have same median)
    len(some_nums) #determine amount of numbers
    l=len(some_nums) #abbreviating for easier use in equations
    median=0 #in case there are zero numbers in the set
    """used to find the median of a set of numbers if there are zero, odd, or, even amount"""
    if l == 0:
        return 0
    if l % 2 == 1:
        return some_nums[l//2] #calcs for odd amount of numbers in set
    else:
        return (some_nums[l//2-1]+some_nums[l//2])/2 #calcs for even amt of numbers in set


#test
#some_nums= [13,7,-3,82,4]
#result=find_median(some_nums)
#print(result)
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#bruteforce solution
def twoSumBruteForce():
    nums=[2,3,4,1,5]
    target = 4
    for i in range (len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i]+nums[j]==target):
                return [i,j]
# using hash table to store result of calculation
def twoSumHashTable():
    nums=[2,3,4,1,5]
    target = 7
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:        # if key in dict
            return [hashmap[complement],i]
        hashmap[nums[i]] =i              


def main():
    print(twoSumHashTable())
    

if __name__ == "__main__":
    main()


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # holds found indices
        found = {}
        # Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object
        # index, var
        for index, num in enumerate(nums):
            # find the 2nd number
            remainder = target - num
            # did we find the remainder index yet?
            # if not store the index of the remainder
            if remainder not in found:
                found[num] = index
            # we know the remainder exists and this number exists
            # return a list
            # containing remainder stored in the dictionary, current index
            else:
                return [found[remainder], index]

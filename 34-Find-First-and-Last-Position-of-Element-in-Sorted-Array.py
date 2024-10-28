class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        def first_occurence(nums, low, high, target):
            first = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid]==target:
                    first = mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid -1 
                else:
                    low = mid + 1
            return first
        def last_occurence(nums, low, high, target):
            last = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid]==target:
                    last = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid -1 
                else:
                    low = mid + 1
            return last
        
        first = first_occurence(nums, low, high, target)
        last = last_occurence(nums, low, high, target)
        return [first, last]
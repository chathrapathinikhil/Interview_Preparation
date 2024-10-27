class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarymod(arr, low, high, target):
            print(low, high)
            while low <= high:    
                mid = (low + high)//2
                print(arr[mid])
                if arr[mid] == target:
                    return mid
                elif arr[mid] >= arr[low]:
                    if arr[low] <= target < arr[mid]:
                        high = mid-1
                    else:
                        low = mid + 1
                else:
                    if arr[mid] < target <= arr[high]:
                        low = mid + 1
                    else:
                        high = mid - 1           
            return -1
        num = binarymod(nums, 0, len(nums)-1, target)
        return num

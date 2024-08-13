class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if i+1<j and nums[j]==nums[j-1]:
                    continue
                l = j+1
                k = len(nums)-1
                while l<k:
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    # print(nums[i], nums[j], nums[l], nums[k])
                    if sum>target:
                        k-=1
                    elif sum<target:
                        l+=1
                    else:
                        output.append([nums[i], nums[j], nums[l], nums[k]])
                        
                        while k>l and nums[k]==nums[k-1]:
                            k-=1
                        while l<k and nums[l]==nums[l+1]:
                            l+=1
                        l+=1
                        k-=1
            
        return output

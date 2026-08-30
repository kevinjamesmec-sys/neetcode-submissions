class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            f=i+1
            b=len(nums)-1
            while f<b:
                if (-n)==nums[f]+nums[b]:
                    res.append([n,nums[f],nums[b]])
                    f+=1
                    b-=1
                    while f < b and nums[f] == nums[f - 1]:
                        f += 1

                    while f < b and nums[b] == nums[b + 1]:
                        b -= 1

                elif (-n)>nums[f]+nums[b]:
                    f+=1
                else:
                    b-=1
        return res
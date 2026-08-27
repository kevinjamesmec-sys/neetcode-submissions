class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        res=[]
        for i in range(len(nums)):
            if i!=0:
                prefix.append(nums[i]*prefix[i-1])
            else:
                prefix.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                postfix.append(nums[i]*postfix[-1])
            else:
                postfix.append(nums[i])
        postfix.reverse()
        for i in range(len(nums)):
            if i==0:
                res.append(postfix[1])
            elif i==len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        return res
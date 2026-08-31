class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        res=0
        for i in range(len(height)):
            if i!=0:
                leftmax[i]=max(leftmax[i-1],height[i])
            else:
                leftmax[i]=max(leftmax[i],height[i])
        for i in range(len(height)-1,-1,-1):
            if i!=len(height)-1:
                rightmax[i]=max(rightmax[i+1],height[i])
            else:
                rightmax[i]=max(rightmax[i],height[i])
        for i in range(len(height)):
            ht=min(leftmax[i],rightmax[i])
            tot=ht-height[i]
            if tot>=0:
                res+=tot
        return res
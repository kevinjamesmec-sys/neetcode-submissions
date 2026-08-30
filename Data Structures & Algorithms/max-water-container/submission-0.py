class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f=0
        b=len(heights)-1
        area=0
        while f<b:
            ht=min(heights[f],heights[b])
            wdt=b-f
            area=max(area,ht*wdt)
            if heights[f]<=heights[b]:
                f+=1
            else:
                b-=1
        return area
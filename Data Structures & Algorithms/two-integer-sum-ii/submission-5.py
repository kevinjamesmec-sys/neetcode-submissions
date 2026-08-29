class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        e=len(numbers)-1
        while f!=e:
            if (numbers[f]+numbers[e])<target:
                f+=1
            elif (numbers[f]+numbers[e])>target:
                e-=1
            else:
                return [f+1,e+1]
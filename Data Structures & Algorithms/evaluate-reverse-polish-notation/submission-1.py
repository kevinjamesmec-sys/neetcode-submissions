class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result=[]
        for x in tokens:
            if x=="+":
                b=result.pop()
                a=result.pop()
                res=a+b
                result.append(res)
            elif x=="-":
                b=result.pop()
                a=result.pop()
                res=a-b
                result.append(res)
            elif x=="*":
                b=result.pop()
                a=result.pop()
                res=a*b
                result.append(res)
            elif x=="/":
                b=result.pop()
                a=result.pop()
                res=int(a/b)
                result.append(res)
            else:
                result.append(int(x))
        return result[-1]
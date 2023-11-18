class Solution:
    def rec(self,i,n,s,ans,d):
        if i==n:
            ans.append(int(s,2))
            return
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if d[i]%2==1:      
            s+="0"
            self.rec(i+1,n,s,ans,d)
            s=s[0:len(s)-1]
            s+="1"
            self.rec(i+1,n,s,ans,d)
            s=s[0:len(s)-1]
        else:
            s+="1"
            self.rec(i+1,n,s,ans,d)
            s=s[0:len(s)-1]
            s+="0"
            self.rec(i+1,n,s,ans,d)
            s=s[0:len(s)-1]

                        

        


        
    def grayCode(self, n: int) -> List[int]:
        ans=[]
        flag=False
        d={}
        self.rec(0,n,"",ans,d)
        return ans
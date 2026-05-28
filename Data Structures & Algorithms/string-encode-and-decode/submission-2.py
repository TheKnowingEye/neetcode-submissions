class Solution:

    def encode(self, strs: List[str]) -> str:
        return ('').join(list(map(lambda x: str(len(x))+'#'+x, strs)))
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s): 
            j = i 
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            word = s[j+1 :j+length+1]
            ans.append(word)
            i = j+length+1
        return ans
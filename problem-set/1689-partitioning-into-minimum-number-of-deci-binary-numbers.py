class Solution:
    def minPartitions(self, n: str) -> int:
        max_num = int(n[0])
        i = 1
        while i < len(n):
          max_num = max(max_num, int(n[i]))
          i +=1
        return max_num
        
        
s = Solution()
print(s.minPartitions("32"))
print(s.minPartitions("82734"))
print(s.minPartitions("27346209830709182346"))
print(s.minPartitions("200500000000550"))

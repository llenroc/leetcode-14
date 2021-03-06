class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for k in range(len(gas)):
            if self.canCompleteCircuitFromK(gas,cost,k)==k:
                return k
        return -1
    
    def canCompleteCircuitFromK(self,gas,cost,k):
        cur_gas=0
        for i in range(k,len(gas)):
            cur_gas+=gas[i]-cost[i]
            if cur_gas<0:
                return -1
        
        for i in range(0,k):
            cur_gas+=gas[i]-cost[i]
            if cur_gas<0:
                return -1
        
        return k
        
#===============================================================================
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        k=0
        while k<len(gas):
            cur=self.canCompleteCircuitFromK(gas,cost,k)
            if cur[0]:
                return k
            else:
                if cur[1]<k:
                    return -1
                k=cur[1]+1
        return -1
        
    
    def canCompleteCircuitFromK(self,gas,cost,k):
        cur_gas=0
        for i in range(k,len(gas)):
            cur_gas+=gas[i]-cost[i]
            if cur_gas<0:
                return False,i
        
        for i in range(0,k):
            cur_gas+=gas[i]-cost[i]
            if cur_gas<0:
                return False,i
        
        return True,k
        

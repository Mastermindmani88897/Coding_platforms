import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Min-heap for available servers: stores tuples of (weight, index)
        available = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))
            
        # Min-heap for busy servers: stores tuples of (free_time, weight, index)
        busy = []
        
        ans = []
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            # Time cannot be less than the current task arrival index
            current_time = max(current_time, j)
            
            # If no servers are available, jump time to when the next server becomes free
            if not available and busy[0][0] > current_time:
                current_time = busy[0][0]
                
            # Free up servers whose tasks have finished by current_time
            while busy and busy[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
                
            # Assign the current task to the best available server
            weight, index = heapq.heappop(available)
            ans.append(index)
            
            # Push the server into the busy heap with its new free time
            heapq.heappush(busy, (current_time + task_time, weight, index))
            
        return ans
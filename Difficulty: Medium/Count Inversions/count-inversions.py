class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr, left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            inv = 0
            
            inv += merge_sort(arr, left, mid)
            inv += merge_sort(arr, mid + 1, right)
            inv += merge(arr, left, mid, right)
            
            return inv
        
        def merge(arr, left, mid, right):
            temp = []
            i = left
            j = mid + 1
            inv = 0
            
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    inv += (mid - i + 1)
                    j += 1
            
            while i <= mid:
                temp.append(arr[i])
                i += 1
            
            while j <= right:
                temp.append(arr[j])
                j += 1
            
            for k in range(len(temp)):
                arr[left + k] = temp[k]
            
            return inv
        
        return merge_sort(arr, 0, len(arr) - 1)

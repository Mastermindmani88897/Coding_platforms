class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	z=[]
    	n=[]
    	for i in range(len(arr)):
    	    if arr[i]==0:
    	        z.append(0)
    	    else:
    	        n.append(arr[i])
    	arr[:]=n+z
    	return arr
    	   
    	   
#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0  # No jumps needed for an array with 0 or 1 elements
        
        if arr[0] == 0:
            return -1  # If the first element is 0, it's impossible to move forward

        max_reach = arr[0]  # Maximum index that can be reached from the current position
        steps = arr[0]      # Number of steps remaining at current index
        jumps = 1           # Number of jumps
        
        for i in range(1, n):
            if i == n - 1:
                return jumps  # Reached the end of the array
                
            max_reach = max(max_reach, i + arr[i])  # Update the maximum reachable index
            
            steps -= 1  # One step is already taken
            
            if steps == 0:
                jumps += 1  # Need to take a jump
                if i >= max_reach:
                    return -1  # Can't move forward from the current position
                steps = max_reach - i  # Update the steps remaining
        
        return -1  # If somehow loop terminates without reaching the end
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
       int n = nums.length;
        
    //first create deque 
        Deque<Integer> dq=  new ArrayDeque<Integer>();
        
        int[] arr = new int[nums.length - k +1] ;
        int j = 0;
        
        for(int i = 0 ; i < k ;++i){
            while(!dq.isEmpty() &&  nums[i] >= nums[dq.peekLast()]){
                dq.removeLast();
            }
            
            dq.addLast(i);
        }
        
        for(int i =k ; i < nums.length ;i++){
            arr[j] = nums[dq.peek()];
            j++;
            while(!dq.isEmpty() && dq.peek() <= i-k){
                dq.removeFirst();
            }
            
            while(!dq.isEmpty() && nums[i] >= nums[dq.peekLast()]){
                dq.removeLast();
            } 
            dq.addLast(i);
        }
        
        arr[j] = nums[dq.peek()];
        return arr ;
    }
}
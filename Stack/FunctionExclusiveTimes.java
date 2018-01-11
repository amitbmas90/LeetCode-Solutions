# Tricky part is how to count time of previously stacked function. Count the time on the fly.
class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] res = new int[n];
        Stack<Integer> s = new Stack<>();
        int start_prev_func = -1;
        for (String log: logs){
            String[] parts = log.split(":");
            int fun = Integer.parseInt(parts[0]);
            int time = Integer.parseInt(parts[2]);
            if (parts[1].equals("end")){
                int f = s.pop();
                res[f] += time - start_prev_func + 1;
                start_prev_func = time + 1;
            }
            else{
                // add time to the previous function
                if (!s.empty()){
                    res[s.peek()] += time - start_prev_func;  
                }
                s.push(fun);
                start_prev_func = time;
            }
        }        
        return res;
    }
}

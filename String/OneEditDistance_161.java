// Given two strings determine if they are one edit away.
// Clarify with interviewer if two strings equal considered false.
class Solution {
    public boolean isOneEditDistance(String s, String t) {
        if (s.equals(t)) return false;
        if (s.length() == t.length()){
            return modify(s, t);
        }
        else if (s.length() + 1 == t.length()){
            return insert(s, t);
        }
        else if (t.length() + 1 == s.length()){
            return insert(t, s);
        }
        return false;
    }
    
    public boolean insert(String s, String t){
        if (s.length() == 0) return true;
        int i = 0;
        for (; i < t.length(); i++){
            if (s.charAt(0) == t.charAt(i)) break;
        }
        if (i > 1) return false;
        else if (i == 1) return s.equals(t.substring(1));
        else  return insert(s.substring(1), t.substring(1));
    }
    
    public boolean modify(String s, String t){
        boolean flag = false;
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) != t.charAt(i)){
                if (flag == true) return false;
                flag = true;
            }
        }
        return true;
    }
}

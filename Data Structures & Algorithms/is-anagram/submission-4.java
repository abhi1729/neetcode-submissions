class Solution {
    public boolean isAnagram(String s, String t) {

        Map<Character,Integer> comp = new HashMap<>();

        if (s.length() != t.length()){
            return false;
        }

        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();

        for(char c : sChar){
           
                comp.put(c, comp.getOrDefault(c,0)+1);
            
        }
        for (char t1 : tChar){
            if(comp.containsKey(t1)){
                comp.put(t1,comp.get(t1)-1);

            }
        }
        for(char c1 : sChar){
            if (comp.get(c1) != 0)
            return false;
        }

        

    return true;}
}

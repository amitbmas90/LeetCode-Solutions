class ValidWordAbbr {
    HashMap<String, List<String>> abbrevs;

    public ValidWordAbbr(String[] dictionary) {
        abbrevs = new HashMap<>();
        HashSet<String> seen = new HashSet<>();
        for (String s: dictionary){
            if (seen.contains(s)) continue;
            seen.add(s);
            String abbrev = convert(s);
            if (!abbrevs.containsKey(abbrev)){
                abbrevs.put(abbrev, new ArrayList<String>());
            }
            abbrevs.get(abbrev).add(s);
        }
    }

    private String convert(String s){
        StringBuilder sb = new StringBuilder();
        int len = 0;
        if (s.length() > 0) sb.append(s.charAt(0));
        for (int i = 1; i < s.length()-1; i++){
            len++;
        }
        if(len > 0) sb.append(Integer.toString(len));
        if(s.length() > 1) sb.append(s.charAt(s.length()-1));
        return sb.toString();
    }

    public boolean isUnique(String word) {
        String abbrev = convert(word);
        return (!abbrevs.containsKey(abbrev)) || (abbrevs.get(abbrev).size() == 1 && word.equals(abbrevs.get(abbrev).get(0)));
    }
}

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr obj = new ValidWordAbbr(dictionary);
 * boolean param_1 = obj.isUnique(word);
 */
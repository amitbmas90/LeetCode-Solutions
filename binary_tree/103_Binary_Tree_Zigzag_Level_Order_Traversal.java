class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        List<TreeNode> queue = new LinkedList<>();
        List<Integer> vals = new ArrayList<>();
        queue.add(root);
        int level = 0;
        while (!queue.isEmpty()){
            int len = queue.size();
            for (int i = 0; i < len; i++){
                TreeNode node = queue.remove(0);
                vals.add(node.val);
                if (node.left != null){
                    queue.add(node.left);
                    }
                if (node.right != null){
                    queue.add(node.right);
                }
            }

            if (level % 2 != 0){
                Collections.reverse(vals);
            }
            result.add((new ArrayList<Integer>(vals)));

            level++;
            vals.clear();
        }
        return result;
    }

}
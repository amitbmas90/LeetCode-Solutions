/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        LinkedList<TreeNode> q = new LinkedList<>();
        sb.append(root.val);
        sb.append(" ");
        q.add(root);
        while (q.size() > 0){
            TreeNode cur = q.removeFirst();
            if (cur.left != null){
                sb.append(cur.left.val);
                q.add(cur.left);
            }
            else{
                sb.append('#');
            }
            sb.append(" ");
            if (cur.right != null){
                sb.append(cur.right.val);
                q.add(cur.right);
            }
            else{
                sb.append('#');
            }
            sb.append(" ");
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == "") return null;
        // System.out.println(data);
        String[] d = data.split(" ");
        TreeNode root = new TreeNode(Integer.parseInt(d[0]));
        LinkedList<TreeNode> q = new LinkedList<>();
        q.add(root);
        int idx = 0;
        while (q.size() > 0){
            int l = q.size();
            for (int i = 0; i < l; i++){
                TreeNode cur = q.removeFirst();
                if (!d[(idx+i) * 2 + 1].equals("#")){
                    String c = d[(idx+i) * 2 + 1];
                    TreeNode left = new TreeNode(Integer.parseInt(c));
                    cur.left = left;
                    q.add(left);
                }
                if (!d[(idx+i) * 2 + 2].equals("#")){
                    String c = d[(idx+i) * 2 + 2];
                    TreeNode right = new TreeNode(Integer.parseInt(c));
                    cur.right = right;
                    q.add(right);
                }
            }
            idx += l;
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));

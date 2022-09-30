class btree{
    static class node{
        int data;
        node left,right;
        node(int data){
            this.data=data;
            this.left=null;
            this.right=null;
        }
    }

    static class tree{
        static int i=-1;
        static node buildtree(int nodes[]){
            i++;
            if(nodes[i]==-1) return null;
            node n=new node(nodes[i]);
            n.left=buildtree(nodes); 
            n.right=buildtree(nodes);
            return n;
        }


    }

static void preorder(node root){
    if(root == null)return;

    System.out.print(root.data+" ");
    preorder(root.left);
    preorder(root.right);
}


static void inorder(node root){
    if(root == null) return;
    inorder(root.left);
    System.out.print(root.data+" ");
    inorder(root.right);


}
static void postorder(node root){
    if(root == null){
        return;
    }
    postorder(root.left);
    postorder(root.right);
    System.out.print(root.data+" ");

}







    public static void main(String arg[]){
        
        int a[]={9,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        tree t=new tree();
        node n=t.buildtree(a);
        // System.out.println(n.data);
        preorder(n);
        System.out.println();
        inorder(n);
        System.out.println();
        postorder(n);
        // System.out.println();
        




    }
}









// class btree{
//     static class node{
//         int data;
//         node left,right;
//         node(int data){
//             this.data=data;
//             this.left=left;
//             this.right=right;
//         }
//     }
// static class tree{
//     static int index=-1;

//     static node builddtree(int nodes[]){
//         index++;
//         if(nodes[index] == -1)return null;
//         node n=new node(nodes[index]);
//         n.left=builddtree(nodes);
//         n.right=builddtree(nodes);
//         return n;

//     }
// }




//     public static void main(String arg[]){
//         int nodes[]={9,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        
//         // btree b=new btree();
//         tree t =new tree();
//         node n=t.builddtree(nodes);
//         System.out.println(n.data);
//     }
// }




// class btree{
//     static class node{
//     node left;
//     node right;
//     int data;
//     node(int data){
//         this.data=data;
//         this.left=null;
//         this.right=null;

//     }
//    } 

//     static class tree{
//         static int index =-1;
//         static node builddtree(int nodes[]){
//             index++;
//             if(nodes[index] == -1){
//                 return null;
//             }
//             node newnode=new node(nodes[index]);
//             newnode.left=builddtree(nodes);
//             newnode.right=builddtree(nodes);
//             return newnode;
//         }


//    }


//     public static void main(String args[]){
//         btree b=new btree();
//         int nodes[]={1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
//         tree t=new tree();
//         node root=tree.builddtree(nodes);
//         System.out.println(root.data);
//     }
// }




// class btree{
//     static class node{
//         node left;
//         node right;
//         int data;
//         node(int data){
//             this.data=data;
//             this.left=null;
//             this.right=null;
//         }
//     }
//     static class tree{
//        static int index = -1;
//         static node builddtree(int nodes[]){
//             index++;
//             if(nodes[index] == -1){ return null;}
//             node n=new node(nodes[index]);
//             n.right=builddtree(nodes);
//             n.left=builddtree(nodes);
//             return n;
            
//         }
//     }








//     public static void main(String arg[]){
//         int nodes[]={1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
//         btree b=new btree();
//         tree t=new tree();
//         node n=t.builddtree(nodes);
//         System.out.println(n.data);
//     }
// }
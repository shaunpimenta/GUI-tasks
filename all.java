class all{
    // sorting
    static void display(int arr[]){
        for(int i:arr){
            System.out.print(i+" ");
        }
        
        System.out.println();
    }
    static void selection_sort(int arr[]){
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
                if(arr[i]<arr[j]){
                    int t=arr[j];
                    arr[j]=arr[i];
                    arr[i]=t;
                }
            }
        }
        display(arr);
    }

    static void bubble_sort(int arr[]){
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length-1;j++){
                if(arr[j]>arr[j+1]){
                    int t=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
            }
        }
        display(arr);
    }

    static void divide(int arr[]){
        if(arr.length<2)return;
        int mid=arr.length/2;
        int left[]=new int[mid];
        int right[]=new int[arr.length-mid];
        for(int i=0;i<mid;i++){
            left[i]=arr[i];
        }
        for(int i=mid;i<arr.length;i++){
            right[i-mid]=arr[i];
        }

        divide(left);
        divide(right);
        conquer(arr,left,right);
        

    }
    static void conquer(int arr[],int left[],int right[]){
        int i=0,j=0,k=0;
        while(i<left.length && j<right.length){
            if(left[i]<right[j]){
                arr[k]=left[i];
                i++;
            }
            else{
                arr[k]=right[j];
                j++;
            }
            k++;
        }

        while(i<left.length){
            arr[k]=left[i];
            i++;k++;
        }
        while(j<right.length){
            arr[k]=right[j];
            j++;k++;
        }

    }

    static void insertion_sort(int arr[]){
        for(int i=1;i<arr.length;i++){
            int curr=arr[i];
            int j=i-1;
            while(j>=0 && curr<arr[j]){
                arr[j+1]=arr[j];
                j--;
            }
            arr[j+1]=curr;

        }
        display(arr);
    }

    static int binary_search(int arr[],int start,int end,int k){
        
        if(end>=start){
            int mid=(start+end)/2;
            if(arr[mid] == k){
                return mid;
            }
            if(k<arr[mid]){
            return binary_search(arr,start,mid-1,k);
            }
            // if(k>arr[mid]){
            else{
                return binary_search(arr,mid+1,arr.length,k);
            }
            // if(arr[mid] != k){
            //     return -1;
            // }
        }
     //    return binary_search(arr,mid+1,arr.length,k);
        return -1;

    }

    static int jump_search(int arr[],int x){
        int step=(int)Math.floor(Math.sqrt(arr.length));
        if(arr[step]==x){return step;}
        for(int i=0;i<arr.length-1;i=i+step){
            if(arr[i]>x && arr[i-step]>=0){
                for(int j=i;j>=0;j--){
                    if(x == arr[j]){return j;}
                }
            }
            // else{}


        }
        return -1;
    }

    // ll
        
        static nodee head1;
        static class nodee{
            int data;
            nodee next;
            nodee(int data){
                this.data=data;
            }        
        }
        static void insert(int data){
            nodee n=new nodee(data);
            if(head1 == null){
                head1=n;
                // n.next=null;
                return;
            }
            n.next=head1;
            head1 = n;

        }
        static void show(){
            nodee n=head1;
            while(n != null){
                System.out.print(n.data+" ");
                n=n.next;
            }
        }
    // cll
        static node head,tail;
        static class node{
            node next;
            int data;
            node(int data){
                this.data=data;
            }
        }

        static void add(int data){
            node n=new node(data);
            if(head == null){
                head=n;
                tail=n;
                tail.next=head;
                // n.next
            }else{
                tail.next=n;
                tail=n;
                tail.next=head;
            }
        }

        static void cc_d(){
            node n=head;
            do{
                System.out.print(n.data+" ");
                n=n.next;
            }
            while(n != head);
        }


    // tree
        static class node1{
            node1 left,right;
            int data;
            node1(int data){
                this.data=data;
                this.left=null;
                this.right=null;
            }
        }

        static class tree{
            static int i=-1;
            static node1 build_tree(int nodes[]){
                i++;
                if(nodes[i] == -1)return null;
                node1 n=new node1(nodes[i]);
                n.left=build_tree(nodes);
                n.right=build_tree(nodes);
                return n;
            }
        }

        static void preorder(node1 root){
            if(root == null) return;
            System.out.print(root.data+" ");
            preorder(root.left);
            preorder(root.right);
        }


    public static void main(String args[]){
        int arr[]={2,4,6,3,8,99,43,2,65,0,4};
        int a[]={0 ,2 ,2 ,3 ,4 ,4, 6 ,8,43,65,99};
        display(arr);
        // selection_sort(arr);
        // bubble_sort(arr);
        // divide(arr);
        // display(arr);
        insertion_sort(arr);
        // System.out.println(binary_search(a,0,a.length,999));
        System.out.println(jump_search(arr,909));

        // LL
        // insert(20);insert(11);insert(77);
        // show();

        // CLL
        add(22);add(722);add(422);add(123);
        cc_d();

        // TREE
        int nodes[]={9,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        
        tree t=new tree();
        node1 n =t.build_tree(nodes);
        System.out.println();   
        preorder(n);


    }
}
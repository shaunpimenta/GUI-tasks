class searchingg{


    static int binary_search(int arr[],int start,int end,int x){
        try{
        int m=(start+end)/2;
        if(arr[m] == x){
            return m;
        }
        else if(x>arr[m]){
            return binary_search(arr,m+1,end,x);
        }
        else if(x<arr[m]){
            return binary_search(arr,start,m-1,x);
        }
        else if(arr[m] != x){
            return -1;
        }
        }
        catch(Exception e){
            return -1;
        }
        
        return -1;
    }


    static int jump_search(int arr[],int x,int step){
        if(arr[step]==x) return step;
        for(int i=0;i<arr.length;i=i+step){
            if(arr[i]==x){
                return i;
            }
            if(i>=step && arr[i-step] > x){
                for(int j=i;j>0;j--){
                   if(arr[j]==x){
                     return j;
                    }
                }
            }
            // else return -1;
        }
        return -1;
    }
    static void dis(int arr[]){
        for(int i:arr){
            System.out.print(i+" ");
        }
    }
    static void bubble_sort(int arr[]){
        // dis(arr);
       
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length-1;j++){
                if(arr[j]>arr[j+1]){
                    int t=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
            }
        }
        dis(arr);
    }

    static void selection_sort(int arr[]){
        for(int i=0;i<arr.length;i++){
            for(int j=i;j<arr.length;j++){
                if(arr[i]>arr[j]){
                    int t=arr[i];
                    arr[i]=arr[j];
                    arr[j]=t;
                }
            }
        }
        dis(arr);

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
        // dis(arr);
        // System.out.println();
        while(i<left.length){
            arr[k]=left[i];
            i++;      
            k++;  
            }
        while(j<right.length){
            arr[k]=right[j];
            j++;        
            k++;
            }


    }


    static void merge_sort(int arr[]){
        int mid = arr.length/2;
        int left[]=new int[mid];
        int right[]=new int[arr.length-mid];
        if(arr.length<2)return;
        for(int i=0;i<mid;i++){
            left[i]=arr[i];
        } 
        for(int i=mid;i<arr.length;i++){
            right[i-mid]=arr[i];
        }
        merge_sort(left);
        merge_sort(right);
        conquer(arr,left,right);
     

    }

    static void insertion_sort(int arr[]){
        for(int i=1;i<arr.length;i++){
            //    System.out.println("...........");
            int curr=arr[i];
            int j=i-1;
            //    System.out.print(i+" "+j+" ");
            while(j>=0 && curr<arr[j]){
                arr[j+1]=arr[j];
                // System.out.println(j);
                j--;    
            }
            arr[j+1]=curr;
        }
       
    }


    public static void main(String args[]){
        int a[]={2,3,5,6,7,8,9,12,14,16,18,22,54,65,78,89,999};
        int b[]={9,4,6,3,2,7,0,1,3344,12,14,66,34,88,3,99,123,999};
        dis(b);
        // System.out.println();
        // System.out.println("binary search element at index "+binary_search(a,0,a.length,9991));
        // int jump=(int)Math.floor(Math.sqrt(a.length));
        // System.out.println("jump search element at index "+jump_search(a,0,jump));


        // bubble_sort(b);
        
        // System.out.println();
        // selection_sort(b);
        // System.out.println();
        // merge_sort(b);
        // System.out.println();
        // dis(b);

        insertion_sort(b);
        System.out.println();
        dis(b);
        

        }
    }
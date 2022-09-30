class selection_sort{
	static int count=0;
	void sort(int arr[]){
		for(int i=0;i<arr.length;i++){
			for(int j=0;j<i;j++){
			if(arr[i]<arr[j]){
				count++;
				int t=arr[j];
				arr[j]=arr[i];
				arr[i]=t;
			}
		}
		}
	}
	void print(int a[]){
		for(int i=0;i<a.length;i++){
			System.out.print(a[i]+" ");
	}
}




	public static void main(String arg[]){
		selection_sort s=new selection_sort();
		int ars[]={33,2,32,53,6,2,7,7,99,1,0};
		s.sort(ars);
		s.print(ars);
		// System.out.println(count);
	}
}
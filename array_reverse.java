class array_reverse{
	static int da[]={0,1,2,3,4,5,6,7,8,9};

	public static void main(String arg[]){
		// int n=0;
// while(n<5){
		for(int i=0;i<da.length;i++){
			for(int j=i;j<da.length;j++){
				// System.out.println(j);
				// System.out.println(da[i]+":"+da[j]);
				int t=da[j];
				da[j]=da[da.length-1];
				da[da.length-1]=t;
			}
			
		}
		// n++;
	// }

		for(int i=0;i<da.length;i++){
			System.out.println(da[i]);
		}
	}
}
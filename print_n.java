class print_n{
	int num(int n){
		if(n==0){
			return 0;
		}
		else{
			System.out.println(n);
			return num(n-1);
		}

	}

public static void main(String arg[]){
		print_n r=new print_n();
		// System.out.println(r.num(5));
		r.num(5);
	}


}
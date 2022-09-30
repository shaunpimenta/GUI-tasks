class array_deletion{
	static int daa[] ={1,2,3,4,5,6,7,8,9};
	static int cap=daa.length;

	void remove(int val){
		for(int i=0;i<cap;i++){
			if(daa[i] == val){
				System.out .println("Removing "+val+ " at index "+i);
				cap--;
				for(int j=i;j<cap;j++){
					daa[j] = daa[j+1];
				}
			}
		}
	}

	void print(){
		for(int i=0;i<cap;i++){
			System.out.println(daa[i]);
		}
	}

	public static void main(String[] args) {
	array_deletion a=new array_deletion();
	a.print();
	a.remove(4);
	a.print();



	}
}
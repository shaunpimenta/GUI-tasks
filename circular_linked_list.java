class circular_linked_list{
	node head;
	static class node{
		int data;
		node next;
		node(int d){
			data=d;
			next=null;
		}

	}


// void add(int data){
// 	head = new node(data);
// 	// head.next=head;
// }

	public static void main(String args[]){
		circular_linked_list cll=new circular_linked_list();
		cll.head=new node(1);
		node sec = new node(2);
		node third=new node(3);


		cll.head.next=sec;
		sec.next=third;
		third.next=cll.head;


		System.out.println("ll.head : "+cll.head+"\n");
		System.out.println("ll.head.next : "+cll.head.next+"\n");
// cll.add(22);
		node n=cll.head;
		// while(n!=null){
		for(int i=0;i<5;i++){
			System.out.println(n.next+" -> "+n.data+"\n");
			n= n.next;
		}
	}
}
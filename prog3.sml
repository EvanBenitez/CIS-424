(* Part 1 *)
fun delete(a::b::c::r)=b::r; (* separate out the first 3 elements from the 
				remaining elements and return the 2nd
				element and remain *)

val del_list1 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0];
delete(del_list1);

val del_list2 = [1,2,3];
delete(del_list2);

(* Part 2 *)
fun larger_in_pair([]) = nil
| larger_in_pair(L) =
  let
	val (x:real,y) = hd(L) (* get a single tuple to work with *)
  in
	if x>y then [x] @ larger_in_pair(tl(L)) (*	if x is larger, put x in list and call
							larger_in_pair on tale of list *)
						
	else [y] @ larger_in_pair(tl(L))	(*	else put y in list and call 
							larger_in_pair for tale of list *)
  end;

val lip_list1 = [(1.3,2.4),(3.4,2.2),(8.2,4.4),(2.3,3.1),(53.0,53.2),(2.0,2.1)];
larger_in_pair(lip_list1);

val lip_list2 = [(3.3,3.2),(~0.2,0.2),(~1.4,~1.3)];
larger_in_pair(lip_list2);

(* Part 3 *)
fun add2lists([],[]) = nil	(* If both list empty, return empty list *)
| add2lists(L1,[]) = L1		(* If second list is empty, return L1 *)
| add2lists([],L2) = L2		(* If first list is empyt, return L2 *)
| add2lists(L1,L2) = [hd(L1) + hd(L2)] @ add2lists(tl(L1),tl(L2));	(* add first list elements together
									   and cancat with add2lists call
									   on tales of the 2 lists *)

val add2_list1 = [1,2,3,4,5,6,7,8];
val add2_list2 = [10,20,30,40,50,60,70,80,90];
add2lists(add2_list1,add2_list2);

val empty = nil;
add2lists(empty,empty);
add2lists(empty,add2_list1);
add2lists(add2_list2,empty);

(* Part 4 *)
fun Map(F,nil) = nil				(* The Map Function *)
| Map(F,x::xr) = F(x)::Map(F,xr);

fun product(L) = Map(fn (x,y)=>x*y,L);		(* Takes an integer 2 tuple and used the Map fucntion
						   and a lambda function to a produce a list of integers
						   that are the product of the two integers *)


val product_list1 = [(1,2),(2,3),(3,4),(4,5)];
product(product_list1);

val product_list2 = [(1,~2),(2,~3),(~3,4),(4,~5)];
product(product_list2);

(* Part 5 *)
exception Emptylist;

fun Reduce(F,nil) = raise Emptylist		(* Reduce fuction *)
| Reduce(F,[a]) = a
| Reduce(F,x::xr) = F(x,Reduce(F,xr));

fun minimum(L) = Reduce(fn (x:real, y) => 	(* Returns the minimum value of the list, uses Reduce *)
			if x>y then y 
			else x, L);

val minimum_list1 = del_list1;
minimum(minimum_list1);

val minimum_list2 = [3.0,45.0,34.0,31.0,5.3,63.0,12.0,8.0,9.0];
minimum(minimum_list2);

(* Part 6 *)
fun Filter(p,nil) = nil			(* The fileter function *)
| Filter(p,x::xr) =
	if p(x) then x::Filter(p,xr)
	else Filter(p,xr);

fun between(L) = Filter(fn x =>		(* Returns reals between 3.0 and 4.0 inclusive, uses reduce *)
			if x >= 3.0 andalso x <= 4.0 then true
			else false, L);	

val between_list1 = del_list1;
minimum(between_list1);

val between_list2 = minimum_list2;
minimum(between_list2);

def rightRotate(lists, num): 
	output_list = []
	for item in range(len(lists) - num, len(lists)): 
		output_list.append(str(lists[item])) 	 
	for item in range(0, len(lists) - num): 
		output_list.append(str(lists[item])) 
	print(" ".join(output_list))
rotate_num = int(input())
list_1 = list(map(int,input().split()))

rightRotate(list_1, rotate_num)

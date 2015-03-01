main:
	- gget url
	list = []
	for childData in children
		Child child = new Child(childData)
		list.add(child.to_csv_row)

	print_to_csv(list)

	
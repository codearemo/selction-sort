def selection_sort (items):
	for step in range(len(items)):
		location_of_smallest = step
		for location in range(step, len(items)):
			if items[location_of_smallest] < items[location]:
				smallest_num = items[location_of_smallest]
			else:
				smallest_num = items[location]
				large_num = items[location_of_smallest]
				items[location_of_smallest] = smallest_num
				items[location] = large_num
	print (items)
	print('Total Number of items  ', len(items))

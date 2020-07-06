def num_to_dashes(num):
	dash = ''
	counter = 0
	while counter < num:
		dash += '-'
		counter += 1
	return dash

print(num_to_dashes(6))

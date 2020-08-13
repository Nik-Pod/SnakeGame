import random

def snake(arr):
	c = ['top', 'left', 'right', 'bottom']
	if arr[0][0] == 7 or arr[0][1] == 7 or arr[0][2] == 7:
		return 'top'
	if arr[1][0] == 7:
		return 'left'
	if arr[1][2] == 7:
		return 'right'
	if arr[2][0] == 7 or arr[2][1] == 7 or arr[2][2] == 7:
		return 'bottom'
	if arr[0][1] == 1 or arr[0][1] == 2 or arr[0][1] == 3:
		c.remove('top')
	if arr[1][0] == 1 or arr[1][0] == 2 or arr[1][0] == 3:
		c.remove('left')
	if arr[1][2] == 1 or arr[1][2] == 2 or arr[1][2] == 3:
		c.remove('right')
	if arr[2][1] == 1 or arr[2][1] == 2 or arr[2][1] == 3:
		c.remove('bottom')
	if c == []:
		c = ['top', 'left', 'right', 'bottom']
	return random.choice(c)
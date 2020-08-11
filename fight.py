import random

arr = [[1 if (i >= 0 and i <= 1) or (i >= 12 and i <= 13) or (j >= 0 and j <= 1) or (j >= 12 and j <= 13) else 0 for j in range(0, 14)] for i in range(0, 14)]

def random_apple():
	while True:
		x = random.randint(2, 11)
		y = random.randint(2, 11)
		if arr[x][y] == 0:
			arr[x][y] = 7
			break

random_apple()
random_apple()

for i in arr:
	print(i)
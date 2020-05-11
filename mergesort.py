def mergesort(list_):
	if len(list_) > 1:
		left = list_[:len(list_)//2]
		right = list_[len(list_)//2:]

		mergesort(left)
		mergesort(right)

		l = r = a = 0
		# l => left | r => right | a => array

		while l < len(left) and r < len(right):
			if left[l] < right[r]:
				list_[a] = left[l]
				l += 1
			else:
				list_[a] = right[r]
				r += 1
			a += 1

		while l < len(left):
			list_[a] = left[l]
			l += 1
			a += 1

		while r < len(right):
			list_[a] = right[r]
			r += 1
			a += 1



num = [24, 125, 151, 522, 7367, 272, 1473, 91]
mergesort(num)
print(num)

# file_path = ABSOLUTEPATH OF THE FILE
# file = open(file_path, "r")
# names = []

# for line in file:
# 	line = line.strip("\n")
# 	names.append(line)

# mergesort(names)
# file = open(file_path, "w")
# i = 1
# for line in names:
# 	if i == len(names):
# 		file.write(line)
# 	else:
# 		file.write(line + "\n")
# 		i += 1

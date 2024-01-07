
calVals = []

def replace_text_with_numbers(line: str):

	line = line.replace("twone", "twoone")

	line = line.replace("eightwo", "eighttwo")
	
	line = line.replace("eighthree", "eightthree")

	line = line.replace("oneight", "oneeight")
	line = line.replace("threeight", "threeeight")
	line = line.replace("fiveight", "fiveeight")
	line = line.replace("nineight", "nineeight")

	line = line.replace("sevenine", "sevennine")

	line = line.replace("one", "1")
	line = line.replace("two", "2")
	line = line.replace("three", "3")
	line = line.replace("four", "4")
	line = line.replace("five", "5")
	line = line.replace("six", "6")
	line = line.replace("seven", "7")
	line = line.replace("eight", "8")
	line = line.replace("nine", "9")
	return line


with open("day1_input") as f:
	for line in f.readlines():
		line_replaced = replace_text_with_numbers(line)
		print(line)
		print(line_replaced)

		digits = [x for x in list(line_replaced) if ord(x) >= 48 and ord(x) <= 57]
		calVals.append(int("".join(digits[0] + digits[-1])))
	print(calVals)

with open("day1_answer", "w") as f:
	f.write(str(sum(calVals)))

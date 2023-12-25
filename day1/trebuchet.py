# file = open("./input.txt")
# lines = file.readlines()

numbers =  {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def extract_calibration_value(line):
    _len = len(line)
    first_number = None
    second_number = None
    for i in range(_len):
        if first_number and second_number:
            return first_number, second_number

        if not first_number:
            left = line[i]
            if left.isnumeric():
                first_number = left

        if not second_number:
            right = line[_len - i - 1]
            if right.isnumeric():
                second_number = right

    return first_number, second_number

def parse_line_string_to_number(line: str):
    substrings = [(i, key) for i in range(len(line)) for key in numbers.keys() if line.startswith(key, i)]

    for i in range(len(substrings)):
        index, key =substrings[i]
        line = line[:index + i] + str(numbers[key]) + line[index + i:]

    return line

# Part 1
# calibration_values = []
# with open("./input1.txt") as f:
#     lines = f.read().splitlines()
#     for line in lines:
#         first, second = extract_calibration_value(line)
#         print(first, second)
#         calibration_values.append(int(f"{first}{second}"))
# print(sum(calibration_values))

# Part 2
calibration_values = []
with open("./input2.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        line = parse_line_string_to_number(line)
        first, second = extract_calibration_value(line)
        calibration_values.append(int(f"{first}{second}"))

print(sum(calibration_values))

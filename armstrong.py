lower = 100
upper = 2000

armstrong_numbers = [num for num in range(lower, upper + 1) if num == sum(int(digit) ** len(str(num)) for digit in str(num))]

for armstrong in armstrong_numbers:
    print(armstrong)

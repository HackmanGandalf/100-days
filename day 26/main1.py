with open("100-days-of-code/day 26/file1.txt") as data:
    file1 = data.readlines()
    newfile1 = [int(line) for line in file1]

with open("100-days-of-code/day 26/file2.txt") as data2:
    file2 = data2.readlines()
    newfile2 = [int(line) for line in file2]
# Write your code above 👆

result = [num for num in newfile1 and newfile2 if num in newfile1 and newfile2]

print(result)



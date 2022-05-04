nums_1 = [1,3,5]
nums_2 = [2,4,6, 7, 8]

working_nums = nums_1.copy()
step = 0
for index, num in enumerate(nums_1):
    while len(nums_2) and nums_2[0] < num:
        working_nums.insert(index + step, nums_2.pop(0))
        step += 1
working_nums.extend(nums_2)

print(working_nums)
if len(working_nums)%2 == 1:
    print("Медіана {}".format(round(len(working_nums)/2+0.5)))
else:
    print("Медіана {}".format((round(len(working_nums)/2) + len(working_nums)/2+1) / 2 ))
    
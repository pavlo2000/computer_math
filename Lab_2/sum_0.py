nums = [-1,0,1,2,-1,4]

result = []

for i in range(0, len(nums)):
    for a in range(1, len(nums)-1):
        for b in range(2, len(nums)-2):
            arr = sorted([nums[i], nums[a], nums[b]])
            if sum(arr) == 0 and arr not in result:
                result.append(arr)
                
print(result)
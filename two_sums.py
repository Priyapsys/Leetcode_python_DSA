nums= [2,7,15,13]
target = 17
n = len(nums)
for i in range (n):
    for j in range(i+1,n):
        if nums[i]+ nums[j] == target:
            print(i,j)
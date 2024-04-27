def PerformBubblesort(nums):
    n=len(nums)
    for fixthisindex in range(n-1,0,-1):
        for index in range(fixthisindex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
      
n=int(input())
nums=list(map(int, input().split()))
PerformBubblesort(nums)

print(*nums)

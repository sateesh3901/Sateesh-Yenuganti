def count_multiples(nums):
    mydict = {i:0 for i in range(1,10)}
    for num in nums:
        for i in range(1,10):
            if num%i == 0:
                mydict[i]+=1
    return mydict


# nums = [int(i) for i in input("enter nums: ").split()]
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(nums))
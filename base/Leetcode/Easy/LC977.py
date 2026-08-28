#  nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]


nums = [-4,-1,0,3,10]

result = []

for i in nums:
    square = i * i
    result.append(square)
    # print(square)

left =0
right =1

# for i in range(len(nums)):
#     print(result[i])  
#     if result[left] > result[right]:
#         result[left], result[right] = result[right], result[left]
#         left += 1
#         right += 1

# print("Test for loop :::::", result)
        

print("Final :::", result)
print("Final :::", sorted(result))
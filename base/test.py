# nums = [1,2,3,1]
nums  = [1,1,1,3,3,4,3,2,4,2]

seen =[]
for i in nums:
    if i not in seen:
        seen.append(i)
    else:
        print("duplicate found")
        break
        
    

print(seen)        

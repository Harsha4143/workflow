nums=[2,7,11,15]
target=9
prev_map={}

for i,n in enumerate(nums):
    diff=target-n
    if diff in prev_map:
        print([prev_map[diff],i])
    prev_map[n]=i

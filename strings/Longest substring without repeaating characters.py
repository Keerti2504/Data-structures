string=input()
seen=set()
left=0
max_length=0
for right in range(len(string)):
    while string[right]  in seen:
        seen.remove(string[left])
        left+=1
    seen.add(string[right])
    max_length=max(max_length,right-left+1)
print(max_length)

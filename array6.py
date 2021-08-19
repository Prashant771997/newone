li = [10, 20, 5, 40, 90, 56]
mx = max(li[0], li[1])
smx = min(li[0], li[1])
for i in range(2, len(li)):
    if li[i] > mx:
        smx = mx
        mx = li[i]
    elif li[i] > smx and mx != li[i]:
        smx = li[i]

    else:
        continue

print(smx)


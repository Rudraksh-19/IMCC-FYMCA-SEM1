arr = [10,3,45,6,8,23,42,56,30]
max = min = arr[0]
smax = smin= arr[0]
for num in arr:
    if num > max:
        smax = max
        max = num
    elif (num > smax and num != max):
        smax = num
    if num < min:
        smin = num
        min = num
    elif (num<smin and num != min):
        smin = num
print("maximun : ",max)
print("minimum : ",min)
print("Second max",smax)
print("Second min",smin)
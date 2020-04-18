#uses python3
x = int(input())
y = int(input())
if x > y:  
    smaller = y  
else:  
    smaller = x  
while i < smaller + 1:  
    if((x % i == 0) and (y % i == 0)):  
        hcf = i  
print(hcf)  
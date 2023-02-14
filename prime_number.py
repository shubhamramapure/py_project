# num = int(input("Enter the number : "))
# a=0
# for i in range(1, num+1):
#     if num%i == 0:
#         a +=1
# print(f"{num} is a prime number") if a==2 else print(f"{num} is not a prime number")

# # optimized code
# num = int(input("Enter the number : "))
# a=0
# for i in range(1, num//2+1):
#     if num%i == 0:
#         a +=1
# print(f"{num} is a prime number") if a==1 else print(f"{num} is not a prime number")



#### list comprehension and ternary operator
num = int(input("enter the number : "))
li = [x for x in range(1, num // 2+1) if num % x==0 ]
print(f"{num} is prime") if len(li)== 1 else print(f"{num} is not prime")

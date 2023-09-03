# class Divide :
#     def divide_by_two (self,num) :
#         num=int(num)
#         if num != 2 and num % 2 == 0 :
#             return "YES"
#         else:
#             return "NO"

# def main():
#     divide=Divide()
#     number=input()
#     result = divide.divide_by_two(number)
#     print(result)



# if __name__ =="__main__":
#     main()            


# num=int(input())
# words=[]
# for i in range(num) :
#     i=input()
#     words.append(i)


# for word in  words:
#     if len(word) >= 10 :
#         print(word[0]+str(len(word)-2)+word[-1])
#     else :
#         print(word)



# m,n,a=map(int, input().split())

# length= (n + a - 1) // a
# width= (m + a - 1) // a


# total = length * width

# print(total)

problems=int(input())
result=0
for _ in range (problems):
    views = input().split()
    x,y,z=map(int, views)
    if x+y+z >= 2:
        result += 1

print(result)   


# 8/18 쪽지시험 마지막문제

# def isOdd(x):
#     return x % 2 == 1  #홀수일때만 true
# d1 = {x:x*x for x in range(11) if isOdd(x)}
# print(d1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#소수만 출력하기로 바꿔보기
# def isOdd(x):
#     count = 0
#     #for i in range(1,x+1):
#     for j in range(1,x+1):
#         for i in range(x,-1,-1):
#             if j / i == 0:
#                 count += 1
#                 if count == 2:
#                     print(j)
#                 else :
#                     print(' ') 
# isOdd(10)


#소수 찾기 _ 챗gpt
# def prime(x):
#     for i in range(x+1):
#         if i <= 1:
#             return False
#         if i <= 3:
#             return True
#         if i%2 ==0 or i%3 == 0:
#             return False
        
# print(5)
    



# #소수
# def prime(x):
#     count = 0
#     if x <= 1:
#         return False
#     if x <=3:
#         return True
#     for i in range(1, x+1):
#         if x/i == 0:
#             count += 1

#             if count == 2:
#                 return x
#             else:
#                 return 0
            
# print(prime(5))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



#모듈

#모듈을 다른곳에서 가져닸쓰는 예제
#가져다쓸땐 임포트를 써서 모듈이름을 가져옴
# as = 별명
#파일이름이 모듈이름이 된다.
# ex) 파일명이 morse.py  라면 다른 파일에서 import morse를 써야함



def age(x ,y):
    a = x / y
    return int(a)

print(age(5,2))

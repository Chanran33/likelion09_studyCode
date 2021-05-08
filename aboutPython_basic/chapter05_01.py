#파이썬 함수 및 중요성
#파이썬 함수식 및 람다(lamda)

#함수 정의 방법
#def function_name(parameter):
#   code

#예제 1 - 리턴문이 없는 경우
def first_func(name):
    print("Hello,", name)

# name = input()
# first_func(name) #함수 호출

#예제 2 - 리턴문이 있는 경우
def return_func(name):
    value = "Hello, " + str(name)
    return value

# name = input()
# print(return_func(name))

# 예제 3 
# 임의 정수나 실수를 입력받아 곱하기를 하여 
# 세 개를 동시에 리턴하는 함수를 만들어보자
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

# x, y, z = func_mul(10)

# print(x,y,z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) #튜플로 반환

# q = func_mul2(20)
# print(type(q), q)

#리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3] #리스트로 반환

# p = func_mul3(30)
# print(type(p), p)

#딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'key1':y1, 'key2':y2, 'key3':y3} #리스트로 반환

d = func_mul4(40)
print(type(d), d, d.get('v2'), d.items(), d.keys())

#중요
# *args, **kwargs 

#enumerate함수
#리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가진다.
#순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력받아
#인덱스 값을 포함하는 enumerate 객체를 리턴한다.

# *args(언팩킹)
def args_func(*args): #가변이다 : 한개의 매개변수가 들어올 수도 있고, 여러개의 매개변수가 들어올 수도 있다.
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('----')
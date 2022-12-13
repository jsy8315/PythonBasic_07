# 함수


# 기본
def add(a, b):
  return a + b


print(add(3, 7))


# 기본2-return문 없이 작동하기
def add(a, b):
  print("함수의 결과:", a + b)


add(3, 7)

# global 키워드
a = 50


def func():
  global a
  a += 1


for i in range(10):
  func()

print(a)

#람다 표현


def add(a, b):
  return a + b


# 일반적인 add() 메서드 사용
print(add(6, 9))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(8, 9))

# 람다 표현식 예시
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
  return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

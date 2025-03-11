# 첫 번째 인수로 함수, 두 번째 인수로 반복 가능한 데이터
# 그리고 반복 가능한 데이터의 요소 순서 대로 함수를 호출 했을때
# 리턴 값이 참인 것만 묶어서 리턴
# def positive(x):
#     return x > 0
#
# print(list(filter(positive, [1, -2, 5, -3, 8])))

# hex()
# 정수를 입력 받아 16진수 문자열로 변환 하여 리턴 하는 변수
# print(hex(234))
# print(hex(3))

# id()
# 객체를 입력 받아서 고유 주소값(레퍼런스)를 리턴 하는 함수
# a = 3
# print(id(3))

# map()
# map은 입력 받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴
# def two_time(x):
#     return x*2
#
# print(list(map(two_time, [1, 2, 3, 4])))

# max()
# 반복 가능한 데이터 중에서 최대값 리턴
# num_list = [1, 3, 13, 20, 18, 17, 5, 9]
# print(max(num_list))
#
# # min()
# # 반복 가능한 데이터 중에서 최솟값 리턴
# num_list = [1, 3, 13, 20, 18, 17, 5, 9]
# print(min(num_list))

# oct()
# oct()는 정수를 8진수 문자 열로 바꾸어 리턴 하는 함수
# print(oct(34))
# print(oct(12345))

# open()
# open(fileName, [mode])은 "파일 이름"과 "읽기 방법"을
# 입력 받아 파일 객체를 리턴 하는 함수
# w 쓰기 모드
# r 읽기 모드
# a 추가 모드
# b 바이너리 모드

# file = open("example.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)
# file.close()

# with open("example.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# ord() <> chr()
# ord()는 문자의 유니코드 숫자 값을 리턴 하는 함수
# print(ord("가"))
# print(ord("a"))

# pow()
# 첫 번째 인수의 두번째 인수 만큼 거듭 제곱 한 값을 리턴 하는 값
# print(pow(3,10))

# range()
# range(시작, 끝, 간격) for 문과 함께 자주 사용
# 이 함수는 입력 받은 숫자에 해당 하는 범위 값을
# 반복 가능한 객체로 만들어 리턴
# print(list(range(5,10,2)))

# round()
# 반올림
# print(round(4.4))
# print(round(8.9))
# print(round(5.1234, 2))

# sum()
# 합계
# num_list = [1234, 582, 1475, 55752]
# print(sum(num_list))

# 공식 문서도 자주 확인 해봐야 함

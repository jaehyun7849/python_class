# fruits = ["orange", "apple", "banana"] # 문자열 리스트
# numbers = [6, 3, 1, 5] #숫자 리스트
# bools = [True, False, True] #불리언 리스트
# mixed_list = ["안녕하세요", 12, True]
#
# print(fruits[2][1])
#
# numbers.sort(reverse=True) #sort()작은순 옵션 reverse= True 큰순
#
# fruits = "-".join(fruits)
# print(fruits)
#
# cart = []
# cart.append(input("추가할 상품 : a"))
# cart.append(input("추가할 상품 : b"))
# cart.append(input("추가할 상품 : c"))
#
# print(cart)

#튜플
colors = ("red", "green", "black", "yellow") #선언 즉시 변경 불가능
numbers = (1, 5, 3, 9, 1, 2)
bools = (True, False, True)
mixed_tuple = ("red", 1, True)

# a = ("first",) # 요소가 하나일 때는 마지막 쉼표!!

print(colors[1])

#colors[1] = "yellow" # 튜플은 변경 불가능
print(numbers[0:2]) # 슬라이싱 가능
print(numbers.count(1)) # 카운트 가능\
print(numbers.index(3))

a, b, c, d = colors # 언패킹
print(d)


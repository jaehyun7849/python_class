# #상속
#
# # class Parent :
# #     def introduce(self):
# #         print("저는 부모 입니다.")
#
# # class Child(Parent):
# #     def introduce(self):
# #         print("저는 자식 입니다.")
#
# # child = Child()
# # child.introduce()
# #
# # class Car:
# #     def __init__(self, model, price):
# #         self.model = model
# #         self.price = price
# #
# #     def drive(self):
# #         print(f"{self.model}가 앞으로 전진 합니다.")
# #
# # class ElecCar(Car):
# #     def __init__(self, model, price, energy_efficiency):
# #         super().__init__(model, price)
# #         self.energy_efficiency = energy_efficiency
# #
# #     def drive(self):
# #         super().drive() # 부모 클래스의 메소드를 그대로 호출 가능
# #         print(f"{self.model}이 전기로 전진 합니다.") # 메소드 오버라이딩
# #
# # ev6 = ElecCar("ev6", "5000", "60kWh")
# # ev6.drive()
#
# # 다단계 상속
# # class GrandParent:
# #     def introduce(self):
# #         print("우리는 할머니 할아버지")
# # class Parent(GrandParent):
# #     def introduce(self):
# #         super().introduce()
# #         print("우리는 엄마 아빠")
# #
# # class Child(Parent):
# #     def introduce(self):
# #         super().introduce()
# #         print("우리는 자식")
# #
# # child1 = Child()
# # child1.introduce()
#
#
# # 다중 상속
# # class Father:
# #     def drive(self):
# #         print("운전을 잘함")
# #
# # class Mother:
# #     def cook(self):
# #         print("요리를 잘함")
# #
# # class Child(Father, Mother):
# #     def study(self):
# #         print("공부를 잘함")
# #
# # child1 = Child()
# # child1.drive()
# # child1.cook()
# # child1.study()
#
# # class Animal:
# #     def breathe(self):
# #         print("숨을 쉴 수 있어요")
# #
# # class Swimmer:
# #     def swim(self):
# #         print("헤엄을 칠 수 있어요")
# #
# # class Fish(Animal, Swimmer):
# #     pass
# #
# # nimo = Fish()
# # nimo.swim()
# # nimo.breathe()
#
# # class GrandParent:
# #     def smart(self):
# #         print("똑똑해요")
# #
# # class Father(GrandParent):
# #     def doctor(self):
# #         print("나는 의사")
# #
# # class Mother:
# #     def rich(self):
# #         print("나는 부자")
# #
# # class Child(Father,Mother):
# #     pass
# #
# # child1 = Child()
# # child1.smart()
# # child1.doctor()
# # child1.rich()
#
# # 다중 상속을 썼을 때 super()를 사용 하면 문제가 생김
#
# # class A:
# #     def introduce(self):
# #         print("나는 A")
# #
# # class B:
# #     def introduce(self):
# #         print("나는 B")
# # class C:
# #     def introduce(self):
# #         print("나는 C")
# #
# # class Child(A,B,C):
# #     def introduce(self):
# #         print(Child.mro())
# #         super().introduce() # MRO 에 따라 첫 번째를 부름
# #         super(B, self).introduce()
# #         C.introduce(self)
# #
# # child = Child()
# # child.introduce()
#
# #MRO
# #=>Method Resolution Order : 메소드 결정 순서
#
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def start(self):
#         print(f"{self. brand}의 {self.model}가 출발합니다.")
#
#     def stop(self):
#         print(f"{self. brand}의 {self.model}가 정지합니다.")
#
# class ElectricCar:
#     def __init__(self, brand, model, battery_capacity):
#         self.battery_capacity = battery_capacity
#
#     def charge(self):
#         print(f"배터리를 충전합니다.")
#
# class GasolineCar:
#     def __init__(self, brand, model, fuel_tank_capacity):
#         self.fuel_tank_capacity = fuel_tank_capacity
#
#     def refuel(self):
#         print(f"연료를 주유 합니다.")
#
# class HybridCar(Car,ElectricCar,GasolineCar):
#     def __init__(self, brand, model, battery_capacity, fuel_tank_capacity):
#         Car.__init__(self,brand,model)
#         ElectricCar.__init__(self, battery_capacity)
#         GasolineCar.__init__(self, fuel_tank_capacity)
#
#     def switch_mode(self,mode):
#         if mode == "electric":
#             print(f"{self.brand}의 {self.model}가 전기 모드로 전환 됩니다.")
#         elif mode == "gasoline":
#             print(f"{self.brand}의 {self.model}가 내연 기관 모드로 전환 됩니다.")
#         else:
#             print("잘못된 모드입니다.")
#
#
# hybrid = HybridCar("Hyundai", "sonata", "60kWh", "50L")
# hybrid.switch_mode("electric")
# hybrid.stop()
# hybrid.start()
# hybrid.charge()
# hybrid.refuel()
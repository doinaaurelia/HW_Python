# import time
# from turtle import clear
# import os

# class TrafficLight:
#     def __init__(self, color = "red") -> None:
#         self.__color = color
#     def running(self):
#         count = 0
#         red_mode = "*******\n*     *\n*  \033[31m*\033[0m  *\n* \033[31m***\033[0m *\n*  \033[31m*\033[0m  *\n*     *\n\
# *******\n*     *\n*     *\n*     *\n*     *\n*     *\n*******\n*     *\n*     *\n*     *\n\
# *     *\n*     *\n*******\n"
#         yellow_mode = "*******\n*     *\n*     *\n*     *\n*     *\n*     *\n\
# *******\n*     *\n*  \033[33m*\033[0m  *\n* \033[33m***\033[0m *\n*  \033[33m*\033[0m  *\n*     *\n\
# *******\n*     *\n*     *\n*     *\n\
# *     *\n*     *\n*******\n"
#         green_mode = "*******\n*     *\n*     *\n*     *\n*     *\n*     *\n\
# *******\n*     *\n*     *\n*     *\n\
# *     *\n*     *\n*******\n*     *\n*  \033[32m*\033[0m  *\n* \033[32m***\033[0m *\n*  \033[32m*\033[0m  *\n*     *\n\
# *******\n"
#         while(count <= 5):
#             if self.__color == "red":
#                 os.system('cls||clear')
#                 print(red_mode)
#                 time.sleep(7)
#                 self.__color = "yellow"
#             elif self.__color == "yellow":
#                 os.system('cls||clear')
#                 print(yellow_mode)
#                 time.sleep(2)
#                 self.__color = "green"
#             elif self.__color == "green":
#                 os.system('cls||clear')
#                 print(green_mode)
#                 time.sleep(5)
#                 self.__color = "red"
#             count += 1

# a = TrafficLight("yellow")
# a.running()
# b = TrafficLight("green")
# b.running()
# c = TrafficLight()
# c.running()

# class Road():
#     def __init__(self, length = 0, width = 0) -> None:
#         self._length = length
#         self._width = width

#     def weight(self, weight = 25, thickness = 5):
#         return self._length * self._width * (weight/1000) * (thickness /100)

# road_m5 = Road(20, 5000)
# print(road_m5.weight(25,5))
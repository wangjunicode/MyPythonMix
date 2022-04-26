#!/usr/bin/python
# -*- coding:UTF-8 -*-
# Kyriewang Python Demo
# 开发时间: 2021/5/8 14:17


class Vehicle:
    def run(self):
        print("I'm running!")


class Car(Vehicle):
    def run(self):
        print("Car is running!")


class RaseCar(Car):
    def run(self):
        print("Race Car is running!")


v = Vehicle()
v = RaseCar()
v.run();
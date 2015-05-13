# -*- coding: utf-8 -*-

import random as sys_random

location_ = {
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
    "G": "16",
    "H": "17",
    "I": "34",
    "J": "18",
    "K": "19",
    "M": "21",
    "N": "22",
    "O": "35",
    "P": "23",
    "Q": "24",
    "T": "27",
    "U": "28",
    "V": "29",
    "W": "32",
    "X": "30",
    "Z": "33",
}

gender_ = {
    "male": "1",
    "female": "2",
}

def random(location=None, gender=None):
    if location not in list(location_.keys()):
        location = sys_random.choice(list(location_.keys()))
    gender = gender_[gender] if gender in list(gender_.keys()) else sys_random.choice(list(gender_.values()))
    third_to_ninth = [sys_random.choice(range(0, 10)) for _ in range(3, 10)]
    sum_, weight = 0, [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    for i, j in enumerate([int(location_[location][0]), int(location_[location][1]), int(gender)] + third_to_ninth):
        sum_ += weight[i] * j
        tenth = 10 - (sum_ % 10) if (sum_ % 10) > 0 else 0

    return "".join([location, gender] + [str(x) for x in third_to_ninth] + [str(tenth)])

def female():
    return random(gender="female")

def male():
    return random(gender="male")

def kaohsiung():
    return random(location="E")

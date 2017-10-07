# -*- coding: utf-8 -*-

import random as sys_random

location_map = {
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

gender_map = {
    "1": "1", # male
    "2": "2", # female
}

gender_ = {
    "male": "1",
    "female": "2",
}

location_ = {
    "taipei": "A",
    "taichung": "B",
    "keelung": "C",
    "tainan": "D",
    "kaohsiung": "E",
    "new_taipei": "F",
    "ilan": "G",
    "taoyuan": "H",
    "chiayi_city": "I",
    "hsinchu": "J",
    "miaoli": "K",
    "nantou": "M",
    "changhua": "N",
    "hsinchu_city": "O",
    "yunlin": "P",
    "chiayi": "Q",
    "pingtung": "T",
    "hualien": "U",
    "taitung": "V",
    "kinmen": "W",
    "penghu": "X",
    "lienchiang": "Z",
    # "taichung_county": "L",
    # "tainan_county": "R",
    # "kaohsiung_county": "S",
    # "yangming_moutain": 'Y",
}

def random(location=None, gender=None):
    location = location_.get(location, sys_random.choice(tuple(location_.values())))
    gender = gender_.get(gender, sys_random.choice(tuple(gender_.values())))
    third_to_ninth = [sys_random.choice(range(0, 10)) for _ in range(3, 10)]
    sum_, weight = 0, [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    for i, j in enumerate([int(location_map[location][0]), int(location_map[location][1]), int(gender)] + third_to_ninth):
        sum_ += weight[i] * j
        tenth = 10 - (sum_ % 10) if (sum_ % 10) > 0 else 0

    return "".join([location, gender] + [str(x) for x in third_to_ninth] + [str(tenth)])

def location(location):
    def _(fn):
        def __(id_=None):
            return random(location=location) if id_ is None else random(location=location, gender=id_[1])
        return __
    return _

def gender(gender):
    def _(fn):
        def __(id_=None):
            return random(gender=gender) if id_ is None else random(location=id_[0], gender=gender)
        return __
    return _


@gender("female")
def female(id_=None):
    pass

@gender("male")
def male(id_=None):
    pass

@location("taipei")
def taipei(id_=None):
    pass

@location("kaohsiung")
def kaohsiung(id_=None):
    pass

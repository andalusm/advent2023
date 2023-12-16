import numpy
import numpy as np


def get_points():
    points = 0
    for i in open("input_day4.txt"):
        cards = i.split(":")[1]
        cards_lucky, cards_hold = cards.split("|")
        cards_lucky = set(cards_lucky.split())
        cards_hold = set(cards_hold.split())
        points_upper = len(cards_hold.intersection(cards_lucky))
        if points_upper>0:
            points += 2**(points_upper - 1)
    return points


def get_scrach_cards():
    arr = np.ones(220)
    arr[0] = 1
    j = 0
    for i in open("input_day4.txt"):
        cards = i.split(":")[1]
        cards_lucky, cards_hold = cards.split("|")
        cards_lucky = set(cards_lucky.split())
        cards_hold = set(cards_hold.split())
        points_upper = len(cards_hold.intersection(cards_lucky))
        if points_upper > 0:
            arr[j+1:j+points_upper+1] += arr[j]
        j += 1
    return int(sum(arr))
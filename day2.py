import re

def find_balls_count(text):
    txt = text.replace('and', '')
    finding_balls = re.split(r"[,;:]", txt)
    finding_balls_dic = {}
    for f in finding_balls:
        fin_balls = f.split()
        finding_balls_dic[fin_balls[1]] = int(fin_balls[0])
    ids = []
    for i in open("input_day2.txt"):
        clean_ball = re.split(r"[,;:]", i)
        balls = {}
        find_all = True
        for c in clean_ball[1:]:
            ball = c.split()
            if finding_balls_dic[ball[1]] < int(ball[0]):
                find_all = False
                break
        if find_all:
            print(clean_ball[0])
            ball = int(clean_ball[0].split()[1])
            ids.append(ball)
    return sum(ids)

def find_min_balls_count():
    multi_balls = []
    for i in open("input_day2.txt"):
        balls_dic = {"red": 0, "green": 0, "blue": 0}
        clean_ball = re.split(r"[,;:]", i)
        for c in clean_ball[1:]:
            ball = c.split()
            if balls_dic[ball[1]] < int(ball[0]):
                balls_dic[ball[1]] = int(ball[0])
        multi_balls.append(balls_dic["red"]*balls_dic["green"]*balls_dic["blue"])
    return sum(multi_balls)













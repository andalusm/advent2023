def sum_digits():
    sum_d = 0
    for i in open("input_day1.txt"):
        first = -1
        last = -1
        for d in i:
            if d.isdigit():
                if first < 0:
                    first = int(d)
                last = int(d)
        if first > 0:
            sum_d += first*10 + last
    return sum_d

def sum_digits_words():
    sum_d = 0
    option = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for i in open("input_day1.txt"):
        first = -1
        last = -1
        for j,d in enumerate(i):
            if d.isdigit():
                if first < 0:
                    first = int(d)
                last = int(d)
            elif j+3 < len(i) and i[j:j+3] in option:
                n = option[i[j:j+3]]

                if first < 0:
                    first = n
                last = n
            elif j + 4 < len(i) and i[j:j + 4] in option:
                n = option[i[j:j + 4]]
                if first < 0:
                    first = n
                last = n

            elif j + 5 < len(i) and i[j:j + 5] in option:
                n = option[i[j:j + 5]]
                if first < 0:
                    first = n
                last = n

        if first > 0:
            sum_d += first*10 + last
    return sum_d
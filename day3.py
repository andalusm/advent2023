import csv


def checkAround(data, r, c, spec_symbols):
    rows = len(data)
    cols = len(data[0][0])
    if r + 1 < rows:
        if data[r + 1][0][c] in spec_symbols:
            return [r+1,c]
        if c + 1 < cols and data[r + 1][0][c + 1] in spec_symbols:
            return [r+1,c+1]
        if c - 1 >= 0 and data[r + 1][0][c - 1] in spec_symbols:
            return [r+1,c-1]
    if r - 1 >= 0:
        if data[r - 1][0][c] in spec_symbols:
            return [r-1,c]
        if c + 1 < cols and data[r - 1][0][c + 1] in spec_symbols:
            return [r-1,c+1]
        if c - 1 >= 0 and data[r - 1][0][c - 1] in spec_symbols:
            return [r-1,c-1]
    if c + 1 < cols and data[r][0][c + 1] in spec_symbols:
        return [r,c+1]
    if c - 1 >= 0 and data[r][0][c - 1] in spec_symbols:
        return [r,c-1]
    return None


def find_part_numbers():
    sum_numbers = 0
    spec_symbols = {'#', '+', '&', '@', '=', '*', '/', '%', '-', '$'}
    with open('input_day3.txt', 'r') as fd:
        reader = csv.reader(fd)
        data = list(reader)
        rows = len(data)
        cols = len(data[0][0])
        number = 0
        found_special = False
        for r in range(rows):
            for c in range(cols):
                if data[r][0][c].isdigit():
                    if checkAround(data, r, c, spec_symbols) is not None:
                        found_special = True
                    number = number * 10 + int(data[r][0][c])
                else:
                    if found_special:
                        print(number)
                        sum_numbers += number
                    found_special = False
                    number = 0
    return sum_numbers


def find_gear_numbers():
    sum_numbers = 0
    dic = {}
    with open('input_day3.txt', 'r') as fd:
        reader = csv.reader(fd)
        data = list(reader)
        rows = len(data)
        cols = len(data[0][0])
        number = 0
        found = ""
        for r in range(rows):
            for c in range(cols):
                if data[r][0][c].isdigit():
                    location = checkAround(data, r, c, {'*'})
                    if location is not None:
                        loc_key = str(location[0])+","+str(location[1])
                        found = loc_key
                    number = number * 10 + int(data[r][0][c])
                else:
                    if found != "":
                        if found in dic:
                            dic[found].append(number)
                        else:
                            dic[found] = [number]
                    found = ""
                    number = 0
    for f in dic.keys():
        if len(dic[f]) ==2:
            sum_numbers += dic[f][0] * dic[f][1]
    return sum_numbers


def find_special():
    with open('input_day3.txt', 'r') as fd:
        reader = csv.reader(fd)
        data = list(reader)
        rows = len(data)
        cols = len(data[0][0])
        dic = set([])
        for r in range(rows):
            for c in range(cols):
                if not data[r][0][c].isdigit():
                    dic.add(data[r][0][c])

    print(dic)

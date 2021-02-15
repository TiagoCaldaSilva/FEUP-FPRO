from math import factorial 


def number_of_collisions(objects):
    k = int(factorial(len(objects)) / (2*factorial(len(objects) - 2)))
    for i, v in enumerate(objects):
        for _ in objects[i + 1:]:
            if v["x1"] > _["x2"]:
                k -= 1
            elif v["x2"] < _["x1"]:
                k -= 1
            elif v["y2"] < _["y1"]:
                k -= 1
            elif v["y1"] > _["y2"]:
                k -= 1
    return k 

print(number_of_colisions([{'x1': 11, 'y1': 192, 'x2': 59, 'y2': 280}, {'x1': 546, 'y1': 564, 'x2': 629, 'y2': 580}, {'x1': 368, 'y1': 418, 'x2': 455, 'y2': 432}, {'x1': 479, 'y1': 506, 'x2': 577, 'y2': 521}, {'x1': 113, 'y1': 315, 'x2': 156, 'y2': 415}, {'x1': 513, 'y1': 40, 'x2': 537, 'y2': 119}, {'x1': 521, 'y1': 488, 'x2': 549, 'y2': 522}, {'x1': 72, 'y1': 295, 'x2': 122, 'y2': 343}, {'x1': 87, 'y1': 160, 'x2': 135, 'y2': 213}, {'x1': 495, 'y1': 304, 'x2': 524, 'y2': 339}]))

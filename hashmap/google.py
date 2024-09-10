# -> #

board = {1: [2, 3], 2: [4], 3: [], 4: [5, 6], 5: [7], 6: [], 7: []}
points = {}


def recursive(person, score):
    if len(board[person]) != 0:
        score.append(len(board[person]))
        for next in board[person]:
            recursive(next, score)


def mark_score():
    for person in board:
        score = []
        recursive(person, score)
        points.update({person: sum(score) + 1})


def add_person(boss, person):
    k = 2
    manager = False
    while not manager:
        if len(board[boss]) < k:
            board[boss].append(person)
            manager = True
        else:
            boss += 1
    mark_score()


add_person(1, 5)
print(points)

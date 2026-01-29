'''
def dfs():
    if solved:
        return True

    choose one decision point
    for each choice:
        apply choice
        if dfs():
            return True
        undo choice

    return False
'''
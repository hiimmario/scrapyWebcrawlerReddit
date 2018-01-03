def brute_force(string, length, goal):

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    if length == 1:
        for c in chars:
            if string + c == goal:
                return string + c
        return False
    else:
        for c in chars:
             s = brute_force(string + c, length - 1, goal)
             if s:
                 return s
        return False

print(brute_force('', 3, 'bob'))
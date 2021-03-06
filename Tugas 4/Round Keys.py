state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))

def add_round_key(s, k):
    Nb = len(s)
    new_state = [[None for j in range(4)] for i in range(Nb)]

    for i, word in enumerate(s):
        for j, byte in enumerate(word):
            new_state[i][j] = byte ^ k[i][j]

    return new_state


flag=add_round_key(state, round_key)

print(matrix2bytes(flag))

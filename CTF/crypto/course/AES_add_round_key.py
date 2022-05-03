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
    for i in matrix:
        print(''.join([chr(int(j)) for j in i]),end='')
def add_round_key(s, k):
    result=[]
    for index in range(len(s)):
        lst = [(s[index][i] ^ k[index][i]) for i in range(len(s))]
        result.append(lst)
    return result



# print(add_round_key(state, round_key))
matrix2bytes(add_round_key(state,round_key))


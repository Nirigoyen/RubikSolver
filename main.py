


def rotateCube(cube, direction): # 1 = derecha, 2 = izquierda, 3 = arriba, 4 = abajo
    if direction == 1:
        cube.front, cube.right, cube.left, cube.back = cube.back, cube.front, cube.right, cube.left
    elif direction == 2:
        cube.front, cube.right, cube.left, cube.back = cube.right, cube.left, cube.back, cube.front
    elif direction == 3:
        cube.front, cube.top, cube.left, cube.botton = cube.botton, cube.front, cube.top, cube.left
    elif direction == 4:
        cube.front, cube.top, cube.left, cube.botton = cube.top, cube.left, cube.botton, cube.front


def rotateRow(cube, row, direction): # 1 = derecha, 2 = izquierda
    if direction == 1:
        cube.front[row], cube.right[row], cube.left[row], cube.back[row] = cube.back[row], cube.front[row], cube.right[row], cube.left[row]
    elif direction == 2:
        cube.front[row], cube.right[row], cube.left[row], cube.back[row] = cube.right[row], cube.left[row], cube.back[row], cube.front[row]


def rotateCol(cube, col, direction): # 3 = arriba, 4 = abajo

    rotateCube(cube, 1)
    rotateCube(cube, 3)
    rotateCube(cube, 2)

    if direction == 3:
        cube.front[col], cube.top[col], cube.left[col], cube.botton[col] = cube.botton[col], cube.front[col], cube.top[col], cube.left[col]
    elif direction == 4:
        cube.front[col], cube.top[col], cube.left[col], cube.botton[col] = cube.top[col], cube.left[col], cube.botton[col], cube.front[col]

    rotateCube(cube, 1)
    rotateCube(cube, 4)
    rotateCube(cube, 2)


if __name__ == '__main__':
    class cube:
        front = [[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]

        right = [[2, 2, 2],
                 [2, 2, 2],
                 [2, 2, 2]]

        left =  [[3, 3, 3],
                 [3, 3, 3],
                 [3, 3, 3]]

        back =  [[4, 4, 4],
                 [4, 4, 4],
                 [4, 4, 4]]

        top =   [[5, 5, 5],
                 [5, 5, 5],
                 [5, 5, 5]]

        botton =[[6, 6, 6],
                 [6, 6, 6],
                 [6, 6, 6]]

        print("cara 1", front)
        print("cara 2", right)



        print("cara 1", front)
        print("cara 2", right)




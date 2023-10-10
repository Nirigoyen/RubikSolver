import random

# ROTACIONES
def rotateCube(cube, direction): # 1 = derecha, 2 = izquierda, 3 = arriba, 4 = abajo
    if direction == 1:
        cube.front, cube.right, cube.left, cube.back = cube.back, cube.front, cube.right, cube.left
    elif direction == 2:
        cube.front, cube.right, cube.left, cube.back = cube.right, cube.left, cube.back, cube.front
    elif direction == 3:
        cube.front, cube.top, cube.left, cube.bottom = cube.bottom, cube.front, cube.top, cube.left
    elif direction == 4:
        cube.front, cube.top, cube.left, cube.bottom = cube.top, cube.left, cube.bottom, cube.front

def rotateRow(cube, row, direction): # 1 = derecha, 2 = izquierda
    if direction == 1:
        cube.front[row-1], cube.right[row-1], cube.left[row-1], cube.back[row-1] = cube.back[row-1], cube.front[row-1], cube.right[row-1], cube.left[row-1]
    elif direction == 2:
        cube.front[row-1], cube.right[row-1], cube.left[row-1], cube.back[row-1] = cube.right[row-1], cube.left[row-1], cube.back[row-1], cube.front[row-1]

def rotateCol(cube, col, direction): # 3 = arriba, 4 = abajo
    for i in range(3):
        if direction == 3:
            cube.front[i][col - 1], cube.top[i][col - 1], cube.left[i][col - 1], cube.bottom[i][col - 1] = cube.bottom[i][col - 1], cube.front[i][col - 1], cube.top[i][col - 1], cube.left[i][col - 1]
        elif direction == 4:
            cube.front[i][col - 1], cube.top[i][col - 1], cube.left[i][col - 1], cube.bottom[i][col - 1] = cube.top[i][col - 1], cube.left[i][col - 1], cube.bottom[i][col - 1], cube.front[i][col - 1]

def scramble(cube):
    for i in range(random.randint(10, 30)):
        rotateCol(cube, random.randint(1, 3), random.randint(3, 4))
        rotateCube(cube, random.randint(1, 4))
        rotateRow(cube, random.randint(1, 3), random.randint(1, 2))



def printFace(face):
    print()
    for i in range (len(face[0])):
        print (face[i])

def printCube(cube):
    print("frente")
    printFace(cube.front)
    print()

    print("derecha")
    printFace(cube.right)
    print()

    print("izquierda")
    printFace(cube.left)
    print()

    print("arriba")
    printFace(cube.top)
    print()

    print("abajo")
    printFace(cube.bottom)
    print()


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

        bottom =[[6, 6, 6],
                 [6, 6, 6],
                 [6, 6, 6]]




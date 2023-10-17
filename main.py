import copy
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

def rotateFace(face):




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

def positionFaces(cube):
    copycube = [copy.deepcopy(cube.front), copy.deepcopy(cube.right), copy.deepcopy(cube.left), copy.deepcopy(cube.back), copy.deepcopy(cube.top), copy.deepcopy(cube.bottom)]

    for i in range(len(copycube)):
        if copycube[i][1][1] == 1:
            cube.front = copycube[i]
        elif copycube[i][1][1] == 2:
            cube.right = copycube[i]
        elif copycube[i][1][1] == 3:
            cube.left = copycube[i]
        elif copycube[i][1][1] == 4:
            cube.back = copycube[i]
        elif copycube[i][1][1] == 5:
            cube.top = copycube[i]
        elif copycube[i][1][1] == 6:
            cube.bottom = copycube[i]
def solve(cube):
    copyFaces = [copy.deepcopy(cube.front), copy.deepcopy(cube.right), copy.deepcopy(cube.left), copy.deepcopy(cube.back), copy.deepcopy(cube.top), copy.deepcopy(cube.bottom)]
    positionFaces(cube)





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

    print("atras")
    printFace(cube.back)
    print()

    print("arriba")
    printFace(cube.top)
    print()

    print("abajo")
    printFace(cube.bottom)
    print()


if __name__ == '__main__':
    class cube:
        front = [[1, 1, 1], # ROJO
                 [1, 1, 1],
                 [1, 1, 1]]

        right = [[2, 2, 2], # VERDE
                 [2, 2, 2],
                 [2, 2, 2]]

        left =  [[3, 3, 3], # AZUL
                 [3, 3, 3],
                 [3, 3, 3]]

        back =  [[4, 4, 4], # NARANJA
                 [4, 4, 4],
                 [4, 4, 4]]

        top =   [[5, 5, 5], # AMARILLO
                 [5, 5, 5],
                 [5, 5, 5]]

        bottom =[[6, 6, 6], # BLANCO
                 [6, 6, 6],
                 [6, 6, 6]]


    printCube(cube)

    rotateCol(cube, 1, 3)

    printCube(cube)

    #FALTA HACER QUE CUANDO SE ROTE UNA FILA O COLUMNA QUE SEA DEL BORDE, SE GIRE LA CARA TAMBIEN




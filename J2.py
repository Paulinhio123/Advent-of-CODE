if __name__ == '__main__':
    file = open("2.txt", "r")
    data = file.read().split('\n')

    h0, v0, aim = 0, 0, 0  #position horizontal/vertical/objectif de départ

    print(data)

    '''for p in data:
        k,v = p.split(' ')
        v = int(v)
        if k == "forward":
            h0 += v
        elif k == "down":
            v0 += v
        elif k == "up":
            v0 -= v'''

    print("Réponse 1: ", h0*v0)

    for i in data :
        k, v = i.split(' ')
        v = int(v)
        if k == "forward":
            h0 += v
            v0 += v * aim
        elif k == "down":
            aim += v
        elif k == "up":
            aim -= v

        print("Réponse 2: ", h0 * v0)










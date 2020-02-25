def to_bool(a):
    if a==1:
        return True
    return False

def hor(d):
    if d:
        print(" _ ")
    else:
        print("   ")

def vert(d1,d2,d3):
    word=""

    if d1:
        word="|"
    else:
        word=" "
    
    if d3:
        word+="_"
    else:
        word+=" "
    
    if d2:
        word+="|"
    else:
        word+=" "
        
    print(word)

def seven_segment(pattern):
    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))

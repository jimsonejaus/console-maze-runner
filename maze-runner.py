#=====================================================
#               Variable Declarations
#=====================================================
n = "North"
e = "East"
s = "South"
w = "West"
startp = 0
endp = 0
#=====================================================
#                Function Definitions
#=====================================================
def start_point(a,c,d):
    if c < 1 or c > (a+2)**2:
        while c < 1 or c > (a+2)**2:
            print ("Please put a starting point that is within the range.")
            c = int(input("Starting point: ")) 
    return c
def end_point(a,c,d):
    if d < 1 or d > (a+2)**2:
        while d < 1 or d > (a+2)**2:
            print ("Please put an exit location that is within the range.")
            d = int(input("Exit location: "))
    if c == d:
        print ("The starting and end points cannot be the same. Please enter valid points.")
        c = int(input("Starting Point: "))
        d = int(input("Exit Location: "))
    return d
def maze(a):
    if a == 1:
        print("+==================================+")
        print("|           |                      |")
        print("|    " + ox[0] + "      |     " + ox[1] + "           " + ox[2] + "    |")
        print("|           |                      |")
        print("|           |           -----------+")
        print("|                                  |")
        print("|    " + ox[3] + "            " + ox[4] + "           " + ox[5] + "    |")
        print("|                                  |")
        print("|           +-----------           |")
        print("|           |                      |")
        print("|    " + ox[6] + "      |     " + ox[7] + "           " + ox[8] + "    |")
        print("|           |                      |")
        print("+==================================+")   
    elif a==2:
        print("+==============================================+")
        print("|                                              |")
        print("|     "+ ox[0] +"          "+ ox[1] +"           "+ ox[2] +"           "+ ox[3] +"     |")
        print("|                                              |")
        print("|          ------------------------+           |")
        print("|                                  |           |")
        print("|     "+ ox[4] +"          "+ ox[5] +"           "+ ox[6] +"     |     "+ ox[7] +"     |")
        print("|                                  |           |")
        print("|          +-----------------------+           |")
        print("|          |           |                       |")
        print("|     "+ ox[8] +"    |     "+ ox[9] +"     |     "+ ox[10] +"           "+ ox[11] +"     |")
        print("|          |           |                       |")
        print("|                      |                       |")
        print("|                      |                       |")
        print("|     "+ ox[12] +"          "+ ox[13] +"     |     "+ ox[14] +"           "+ ox[15] +"     |")
        print("|                      |                       |")
        print("+==============================================+")
    elif a==3:
        print("+==========================================================+")
        print("|                                              |           |")
        print("|     "+ ox[0] +"          "+ ox[1] +"           "+ ox[2] +"            "+ ox[3] +"    |     "+ ox[4] +"     |")
        print("|                                              |           |")
        print("|          -------------+                      |           |")
        print("|                       |                                  |")
        print("|     "+ ox[5] +"          "+ ox[6] +"      |    "+ ox[7] +"            "+ ox[8] +"          "+ ox[9] +"     |")
        print("|                       |                                  |")
        print("+-----------------------+          |           ------------+")
        print("|                                  |                       |")
        print("|     "+ ox[10] +"          "+ ox[11] +"           "+ ox[12] +"     |      "+ ox[13] +"          "+ ox[14] +"     |")            
        print("|                                  |                       |")
        print("|          |            -----------+-----------            |")
        print("|          |                       |                       |")
        print("|     "+ ox[15] +"    |     "+ ox[16] +"           "+ ox[17] +"     |      "+ ox[18] +"          "+ ox[19] +"     |")
        print("|          |                       |                       |")
        print("|          +-----------+           |                       |")
        print("|                      |           |                       |")
        print("|     "+ ox[20] +"          "+ ox[21] +"     |     "+ ox[22] +"     |      "+ ox[23] +"          "+ ox[24] +"     |")
        print("|                      |           |                       |")
        print("+==========================================================+")
    ox[position-1] =" "
#=====================================================
#                   Program Execution
#=====================================================
print ("Welcome to the maze!")
print ("Select a level: 1, 2, or 3")
level = int(input())
while True:
    if 1 <= level <= 3: 
        startp = int(input("Starting point: "))
        endp = int(input("Exit location: "))
        startp = start_point(level,startp,endp)
        endp = end_point(level,startp,endp)
        position = startp
        if level == 1:
            ox =[" "," "," "," "," "," "," "," "," "]
            list1 = [s, e + " " + s ,w,n + " " + e + " " + s,n+ " " +e+ " " +w,s+ " " +w,n,e,n + " " + w]
            na = [0,0,0,  1,1,0,  1,0,1]
            ea = [0,1,0,  1,1,0,  0,1,0]
            sa = [1,1,0,  1,0,1,  0,0,0]
            wa = [0,0,1,  0,1,1,  0,0,1]
        elif level == 2:
            ox =[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            list1 = [e+" "+s,e+" "+w,e+" "+w,s+" "+w, n+" "+e+" "+s,e+" "+w,w,n+" "+s, n+" "+s,s,e+" "+s,n+" "+s+" "+w, n+" "+e,n+" "+w,n+" "+e,n+" "+w]
            na = [0,0,0,0,  1,0,0,1,  1,0,0,1,  1,1,1,1]
            ea = [1,1,1,0,  1,1,0,0,  0,0,1,0,  1,0,1,0]
            sa = [1,0,0,1,  1,0,0,1,  1,1,1,1,  0,0,0,0]
            wa = [0,1,1,1,  0,1,1,0,  0,0,0,1,  0,1,0,1]
        elif level == 3:
            ox =[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            list1 = [e+" "+s,e+" "+w,e+" "+s+" "+w,s+" "+w,s, n+" "+e,w,n+" "+e+" "+s,n+" "+e+" "+s+" "+w,n+" "+w, e+" "+s,e+" "+s+" "+w,n+" "+w,n+" "+e,s+" "+w, n+" "+s,n+" "+e,s+" "+w,e+" "+s,n+" "+s+" "+w, n+" "+e,w,n,n+" "+e,n+" "+w]
            na = [0,0,0,0,0,  1,0,1,1,1,  0,0,1,1,0,  1,1,0,0,1,  1,0,1,1,1]
            ea = [1,1,1,0,0,  1,0,1,1,0,  1,1,0,1,0,  0,1,0,1,0,  1,0,0,1,0]
            sa = [1,0,1,1,1,  0,0,1,1,0,  1,1,0,0,1,  1,0,1,1,1,  0,0,0,0,0]
            wa = [0,1,1,1,0,  0,1,0,1,1,  0,1,1,0,1,  0,0,1,0,1,  0,1,0,0,1]
        else:
            print ("Please input a valid level number.")
            level = int(input())
        ox[startp-1] = "O"
        ox[endp-1] = "X"
        maze(level)
        while position != endp:
            print ("Available Directions: " + str(list1[position-1]))
            move = input()
            case = move.lower() #https://www.w3schools.com/python/ref_string_lower.asp
            if case == "south" and int(sa[position-1]) == 1:
                position += (level+2)
            elif case == "north" and int(na[position-1]) == 1:
                position -= (level+2)
            elif case == "east" and int(ea[position-1]) == 1:
                position += 1
            elif case == "west" and int(wa[position-1]) == 1:
                position -= 1
            elif case == "quit":
                print ("Try again next time.")
                break
            else:
                print ("Please choose an available location.")
                continue
            ox[position-1] = "O"
            maze(level)
        if position == endp:
            print ("Found the exit")
        print ("Goodbye.")
        break
    else:
        print ("Please input a valid level number.")
        level = int(input())
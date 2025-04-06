"""
.......
[[ LE[V, P], LW [V, P], LN[V, P], LS[V, P]  ], 
[ Geolocation: #Xcoordinate, #Ycoordinate], 
[ Nodes Connected ], 
[ association of  LE, LW, LN, LS to connected nodes ]]
green = "11"
yellow = "10" 
red = "00"
red_y = "01"

sample list
[[[20,19], [35,12], [8, 33], [30, 30]], 
[0,0],
[[C, 20,19], [E, 35,12], [D, 8, 33], [B, 30, 30]]]


*distance*

L = [[[20,19], [35,12], [8, 33], [30, 30]], [0,0], [['C', 20,19], ['E', 35,12], ['D', 8, 33], ['B', 30, 30]]]
x = Node()
print(x.NConnected(L)) 
print(x.Gloc(L))
print(x.Tstate(L))
A = assign()
V =A.Cardinal(x.Tstate(L))
B = A.Prime(x.Tstate(L))
print(V, B)
"""

from math import radians, cos, sin, asin, sqrt

from ast import Compare


class Traffic_Lights:
    def __init__(s, *args, **kwargs):
        pass
    def Tstate(s, L : "list")-> list:
        TL = list()
        for i in range(4):
            St = 0.6*(L[0][i][0]) + 0.4*(L[0][i][1])
            TL.append(St)
        return TL
    def LE(s, TL : "list" ):
        if TL[0] > 20:
            return(1)
        else:
            return(0)
    def LW(s, TL : "list"):
        if TL[1] > 20:
            return(1)
        else:
            return(0)
    def LN(s, TL : "list"):
        if TL[2] > 20:
            return(1)
        else:
            return(0)
    def LS(s, TL : "list"):
        if TL[3] > 20:
            return(1)
        else:
            return(0)
        

class Node(Traffic_Lights):
    def __init__(s , *args, **kwargs):
        Traffic_Lights.__init__(s)
        #Tstate.__init__(s)
    def Gloc(s, L : "list"):
        return L[1][0], L[1][1]
    def Distance(s, L : "list", P : "list"):
        lon1 = radians(L[1][0])
        lon2 = radians(L[1][1])
        lat1 = radians(P[1][0])
        lat2 = radians(P[2][0])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return(c * r)
        

    def NConnected(s, L : "list"):
        YT = list()
        for i in range(len(L[2])):
            if type(L[2][i][2]) == str:
                YT.append(L[2][i][2])
        return len(YT)
        
class assign(Node, Traffic_Lights):
    def __init__(s, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
    
    def Cardinal(s, L : "list"):
        e = max(L)
        st = (e*3.14)/100
        return int(e)
    def Prime(s,  L : "list"):
        f = min(L)
        st = (f*3.14)/100
        return int(f)
    def CheckStateNode(s, o1 : "object", o2 : "object", o3 : "object", o4 : "object"):
        pass
    
def ALGO(L : list):
    TL = Traffic_Lights()
    S = TL.Tstate(L)
    State = [TL.LE(S), TL.LW(S), TL.LN(S), TL.LS(S)]
    if sum(State) == 4:
        y = 1
    else:
        y=0
    # Determine state based on traffic conditions
    x = 1 if max(S) > 20 else 0  # Green if heavy traffic, otherwise red/yellow
    R = {"LE":S[0], "LW": S[1], "LN": S[2], "LS": S[3]}
    print(R)
    A = assign()
    a = [A.Cardinal(S), A.Prime(S)]
    print([ State, a])
    return [x, y]
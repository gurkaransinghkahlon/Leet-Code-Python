maxChar = 26

def CustomerSimulation(self,n,seq):
    res = 0
    occupied = 0
    seen = [0]*maxChar
    for char in seq:
        index = ord(char) - ord('A')
        if seen[index] == 0:
            seen[index] = 1
            if occupied < n:
                occupied += 1
                seen[index] = 2
            else:
                res += 1
        else:
            if seen[index] == 2:
                occupied -= 1
            seen[index] = 0

        return res
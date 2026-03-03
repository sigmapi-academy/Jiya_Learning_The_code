
def simpleInterest(p=100, r=0.1, t=1):
    return p*r*t

si = simpleInterest()
print('Simple Interest:',si)

si = simpleInterest(1000)
print('Simple Interest:',si)

si = simpleInterest(1000, 0.12)
print('Simple Interest:',si)

si = simpleInterest(1000,0.12,3)
print('Simple Interest:',si)

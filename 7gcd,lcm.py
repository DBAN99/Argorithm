# 최소공배수
def gcm(a,b):

    while b > 0:
        a, b = b, a%b
    return a

#최대 공약수
def lcm(a,b):
    return a*b/gcm(a,b)

print(gcm(1,7))
print(lcm(12,15))
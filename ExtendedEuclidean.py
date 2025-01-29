def extended_euclidean(a, b):
    print(f"{'q':<10} {'r1':<10} {'r2':<10} {'r':<10} {'t1':<10} {'t2':<10} {'t':<10}")
    print("-" * 65)
    
    r1, r2 = a, b
    t1, t2 = 1, 0
    
    while r2 > 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        print(f"{q:<10} {r1:<10} {r2:<10} {r:<10} {t1:<10} {t2:<10} {t:<10}")
        r1, r2 = r2, r
        t1, t2 = t2, t
    
    print("-" * 65)
    print("GCD:", r1)
    print("Multiplicative Inverse:", t1 + b if t1 < 0 else t1)

if __name__ == "__main__":
    a = int(input("Enter first integer (a): "))
    b = int(input("Enter second integer (b): "))
    extended_euclidean(a, b)
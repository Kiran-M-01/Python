def dec_to_bin():
    n = int(input("Enter :"))
    binary = ''
    while n != 0:
        rem = n%2
        binary = str(rem) + binary
        n //= 2
    print(binary)
dec_to_bin()

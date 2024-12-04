import hashlib

def find_hash(secret, prefix):
    i = 1

    while True:
        if hashlib.md5(f"{secret}{i}".encode()).hexdigest().startswith(prefix):
            return i

        i += 1


print(f"part 1: {find_hash("yzbqklnj", "00000")}")
print(f"part 2: {find_hash("yzbqklnj", "000000")}")

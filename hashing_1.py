import hashlib

# print(hashlib.sha256('ESILVaaaaaaaaah'.encode('utf-8')).hexdigest())
# print(hashlib.sha256('ESILVaaaaaaaas4'.encode('utf-8')).hexdigest())
# print(hashlib.sha256('ESILVaaaaaabcjz'.encode('utf-8')).hexdigest())
# print(hashlib.sha256('ESILVbaaaabn556'.encode('utf-8')).hexdigest())
# print(hashlib.sha256('ESILVaaaaaacwx8'.encode('utf-8')).hexdigest())
# print(hashlib.sha256('ESILVaaabjnw013'.encode('utf-8')).hexdigest())

nonce_possible = 'abcdefghijklmnopqrstuvwxyz0123456789'

def nonce_generator(n = 0):
    if n < 10:
        for nonce in nonce_generator(n+1):
            for char in nonce_possible:
                yield nonce + char
    else:
        yield ''

def increment_nonce_counts(count):
    for i in range(len(count) - 1):
        if count[i] < count[i + 1]:
            count[i] += 1
            for j in range(i + 1, len(count)):
                count[j] = 0
            return count
    count[-1] += 1
    return count


def main():
    for nonce in nonce_generator():
        tested = "ESILV" + nonce
        result = hashlib.sha256(tested.encode('utf-8')).hexdigest()
        if result[:6] == "000000":
            print(tested + " " + result)

if __name__ == '__main__':
    main()
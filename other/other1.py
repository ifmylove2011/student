l = [x-y for x in range(1,5) for y in range(1,5) ]
print(l)
num = 0
for i in l:
    if abs(i)<2:
        num = num+1

print(num)

def bytes_int(data):
    return int().from_bytes(data, byteorder='big', signed=True)

bytes1 =bytes(b'\xff')
print(0xff)
print(bytes_int(bytes1))

data = bytes.fromhex('0101010102020202')
print(data[:4])
print(data[5:])
print(bytes_int(data))

from Crypto.Hash import SHA256


def hexdump(filename):
    byte_array = []
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if chunk:
                byte_array.append(chunk)
            else:
                break

    byte_array.reverse()
    final_hash = None

    for idx, item in enumerate(byte_array):

        hashed = SHA256.new(item)

        if idx == len(byte_array) - 1:
            final_hash = hashed.hexdigest()
        else:
            byte_array[idx + 1] += bytearray.fromhex(hashed.hexdigest())

    print bytes(final_hash)


hexdump('./6.2.birthday.mp4_download')
hexdump('./6.1.intro.mp4_download')

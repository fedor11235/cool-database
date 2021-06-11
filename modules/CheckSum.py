#CRC16
__all__ = ['calc', 'check']

def calc(data: bytes, poly=0x8408):
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)
    
    return crc & 0xFFFF

def check(packetData):
    cheksum = False
    payload = packetData[0:len(packetData)-2]

    cheksumClient = packetData[len(packetData)-2:len(packetData)]
    cheksumServer = cheksum(payload)

    cheksumClient = int.from_bytes(cheksumClient,"big")

    if cheksumClient == cheksumServer:
        cheksum = True

    return cheksum
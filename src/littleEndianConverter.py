def isValidHex(hexValue):
    return all(c.isdigit() or c.lower() in 'abcdef' for c in hexValue)

def addLeadingZero(hexValue):
    if len(hexValue) % 2 != 0:
        hexValue = '0' + hexValue
    return hexValue

def convertToBigEndian(hexValue):
    result = ""
    splitByBytes = [hexValue[i:i+2] for i in range(0, len(hexValue), 2)]
    for byte in splitByBytes:
        result = byte + result
    return result

def convertToDecimal(hexValue):
    return int(hexValue, 16)

def convertToASCII(hexValue):
    splitByBytes = [hexValue[i:i+2] for i in range(0, len(hexValue), 2)]
    result = ""
    for byte in splitByBytes:
        decimalValue = int(byte, 16)
        result = result + chr(decimalValue)
    return result

def prettifyHexString(hexValue):
    splitByBytes = [hexValue[i:i+2] for i in range(0, len(hexValue), 2)]
    result = "0x"
    i = 0
    for byte in splitByBytes:
        if i == len(splitByBytes)-1:
            result = result + byte
        else:
            result = result + byte + "_"
        i = i + 1
    return result

def main():
    print("This program takes in a little endian value and displays the big endian, decimal, and ASCII equivalent.")
    print("Note: Don't enter 0x prior to the hexadecimal string, only base16 characters")
    littleEndian = input("Input a little endian hexadecimal value: ").upper().replace(" ", "")
    if isValidHex(littleEndian) == False:
        print("Provided input is not a valid hexadecimal value")
    littleEndian = addLeadingZero(littleEndian)
    bigEndian = convertToBigEndian(littleEndian)
    decimal = convertToDecimal(bigEndian)

    print(f"Little endian: {prettifyHexString(littleEndian)}")
    print(f"Big endian: {prettifyHexString(bigEndian)}")
    print(f"Decimal: {decimal}")
    print(f"Little endian ASCII: {convertToASCII(littleEndian)}")
    print(f"Big endian ASCII: {convertToASCII(bigEndian)}")

if __name__ == "__main__":
    main()

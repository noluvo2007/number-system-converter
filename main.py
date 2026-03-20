# ================================
# Number System Converter
# With Step-by-Step Solutions
# ================================

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    print("\n--- Steps ---")
    for digit in binary:
        if digit not in ['0', '1']:
            print(" Invalid binary number!")
            return

        value = int(digit) * (2 ** power)
        print(f"({digit} × 2^{power}) = {value}")
        decimal += value
        power -= 1

    print(f"\n Answer = {decimal}")


def decimal_to_binary(decimal):
    if not decimal.isdigit():
        print("Invalid decimal number!")
        return

    num = int(decimal)
    binary = ""

    print("\n--- Steps ---")
    if num == 0:
        print("0 ÷ 2 = 0 remainder 0")
        print("\nAnswer = 0")
        return

    while num > 0:
        remainder = num % 2
        print(f"{num} ÷ 2 = {num // 2} remainder {remainder}")
        binary = str(remainder) + binary
        num = num // 2

    print(f"\n Answer = {binary}")


def octal_to_decimal(octal):
    decimal = 0
    power = len(octal) - 1

    print("\n--- Steps ---")
    for digit in octal:
        if digit not in "01234567":
            print("Invalid octal number!")
            return

        value = int(digit) * (8 ** power)
        print(f"({digit} × 8^{power}) = {value}")
        decimal += value
        power -= 1

    print(f"\nAnswer = {decimal}")


def hex_to_decimal(hex_num):
    decimal = 0
    power = len(hex_num) - 1

    print("\n--- Steps ---")
    for digit in hex_num.upper():
        if digit.isdigit():
            value_digit = int(digit)
        elif digit in "ABCDEF":
            value_digit = ord(digit) - 55
        else:
            print("Invalid hexadecimal number!")
            return

        value = value_digit * (16 ** power)
        print(f"({digit} × 16^{power}) = {value}")
        decimal += value
        power -= 1

    print(f"\nAnswer = {decimal}")


# ================================
# MAIN PROGRAM
# ================================

def main():
    while True:
        print("\n===============================")
        print("   NUMBER SYSTEM CONVERTER")
        print("===============================")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Octal to Decimal")
        print("4. Hexadecimal to Decimal")
        print("5. Exit")

        choice = input("\n Choose an option (1-5): ")

        if choice == "1":
            binary = input("Enter binary number: ")
            binary_to_decimal(binary)

        elif choice == "2":
            decimal = input("Enter decimal number: ")
            decimal_to_binary(decimal)

        elif choice == "3":
            octal = input("Enter octal number: ")
            octal_to_decimal(octal)

        elif choice == "4":
            hex_num = input("Enter hexadecimal number: ")
            hex_to_decimal(hex_num)

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()

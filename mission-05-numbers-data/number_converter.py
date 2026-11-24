#!/usr/bin/env python3
"""
Number Converter Program - Digital Detective Mission 5
Converts a positive decimal integer into binary and hexadecimal representations.
"""

def main():
    print("=" * 45)
    print("       DIGITAL DETECTIVE NUMBER CONVERTER     ")
    print("=" * 45)
    
    user_input = input("Enter a positive decimal number: ").strip()
    
    try:
        decimal_number = int(user_input)
        if decimal_number < 0:
            print("Error: Please enter a positive number.")
            return
            
        binary_result = bin(decimal_number)
        hex_result = hex(decimal_number)
        
        print("-" * 45)
        print(f"Decimal Value     : {decimal_number}")
        print(f"Binary Value      : {binary_result}")
        print(f"Hexadecimal Value : {hex_result}")
        print("-" * 45)
        print(f"Binary (formatted): {binary_result[2:]}")
        print(f"Hex (formatted)   : {hex_result[2:].upper()}")
        print("=" * 45)
        
    except ValueError:
        print("Invalid input. Please enter a valid decimal integer.")

if __name__ == "__main__":
    main()

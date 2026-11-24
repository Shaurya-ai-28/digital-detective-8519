# Mission 5 — Numbers and Data

## 1. Task / objective
Convert numbers between decimal, binary, and hexadecimal by hand, verify with Python, test `number_converter.py`, and explain text encoding.

## 2. Work completed
- Worked out 7 number conversions by hand step by step.
- Verified all answers using Python's `bin()`, `hex()`, and `int()`.
- Tested `number_converter.py` with test values (42, 128, 255).
- Looked up ASCII codes and explained why text encoding is needed.

---

### Task 5.1 — Convert Numbers by Hand

| Question | Working and answer |
| :--- | :--- |
| **Decimal 13 to binary** | 13/2=6 rem 1, 6/2=3 rem 0, 3/2=1 rem 1, 1/2=0 rem 1 -> **1101₂** |
| **Decimal 25 to binary** | 25/2=12 rem 1, 12/2=6 rem 0, 6/2=3 rem 0, 3/2=1 rem 1, 1/2=0 rem 1 -> **11001₂** |
| **Binary 1010 to decimal** | $(1\times 8) + (0\times 4) + (1\times 2) + (0\times 1) = 8 + 0 + 2 + 0$ -> **10₁₀** |
| **Binary 1101 to decimal** | $(1\times 8) + (1\times 4) + (0\times 2) + (1\times 1) = 8 + 4 + 0 + 1$ -> **13₁₀** |
| **Hexadecimal A to decimal** | $A = 10 \times 16^0$ -> **10₁₀** |
| **Hexadecimal 1F to decimal** | $(1\times 16) + (15\times 1) = 16 + 15$ -> **31₁₀** |
| **Binary 1111 to hexadecimal** | Decimal value is $8+4+2+1=15$, which is **F** in hex -> **F₁₆ (0xF)** |

---

### Task 5.2 — Verify Using Python

| Conversion | Python Expression | Output | Matches? |
| :--- | :--- | :--- | :--- |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes |
| Hexadecimal A to decimal | `int("A", 16)` | `10` | Yes |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` | Yes |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes |

---

### Task 5.3 — Build a Small Number Converter
The script `number_converter.py` takes a decimal number and converts it to binary and hex.
- `bin()`: Returns the binary representation with `0b`.
- `hex()`: Returns the hexadecimal representation with `0x`.

**Test Runs:**
- Input `42` -> Binary: `101010` (`0b101010`), Hex: `2A` (`0x2a`)
- Input `128` -> Binary: `10000000` (`0b10000000`), Hex: `80` (`0x80`)
- Input `255` -> Binary: `11111111` (`0b11111111`), Hex: `FF` (`0xff`)

---

### Task 5.4 — How is Text Stored?
- **ASCII codes:** Uppercase 'A' = **65**, Lowercase 'a' = **97**. (Verified with `ord()`).
- **Why encoding is needed:** Computers only store 0s and 1s. An encoding standard assigns a specific number to each letter so all computers read and display the same text.
- **Non-ASCII character:** Indian Rupee symbol **'₹'** (or emoji **'🚀'**), which needs UTF-8.

---

## 3. Commands / tools used
- `python3 number_converter.py`, `bin()`, `hex()`, `int()`, `ord()`

## 4. My understanding
Hexadecimal is a short way to read binary (4 bits = 1 hex digit). Characters are simply numbers mapped by tables like ASCII and UTF-8.

## 5. Difficulties faced
Handling non-numeric input gracefully.

## 6. How I resolved them
Added a `try...except ValueError` block in the script.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`
- Manual math and test outputs recorded above.

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Branch:** `main`

# Mission 4 — How Programs Run

## 1. Task / objective
Create and run a simple Python script (`hello.py`) and compare compilers and interpreters.

## 2. Work completed
- Created `hello.py` with `print("Hello from Python")`.
- Ran the script with `python3 hello.py` and verified output.
- Completed the compiler vs. interpreter comparison table.

---

### Task 4.1 — Create and Run a Python Program
Inside `mission-04-programs/hello.py`:
```python
print("Hello from Python")
```

**Running the program:**
```bash
$ python3 hello.py
Hello from Python
```

---

### Task 4.2 — Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation happens** | Translates the whole program into machine code before running. | Translates and executes line by line while running. |
| **Typical output** | Standalone executable binary (`.exe` or binary file). | Direct screen output; no separate binary file saved. |
| **One example** | C or C++ | Python or JavaScript |
| **One advantage** | Runs very fast because code is already translated. | Fast to test and edit since no build step is needed. |

**Explanation:**
A compiler translates all source code into a machine code executable before running, making it very fast at runtime. An interpreter reads and executes the code line by line while the program runs, making it easier to test changes quickly.

---

## 3. Commands / tools used
- `python3 hello.py`: Ran the script.
- `cat hello.py`: Checked file content.

## 4. My understanding
Computers only execute binary machine code. Compilers translate all code beforehand for speed, while interpreters translate on the fly for ease of development.

## 5. Difficulties faced
Wondering why Python created `.pyc` files in `__pycache__`.

## 6. How I resolved them
Python converts code into intermediate bytecode first, which the Python virtual machine then interprets.

## 7. Evidence / files
- File: `mission-04-programs/hello.py`
- Output: `Hello from Python`

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Branch:** `main`

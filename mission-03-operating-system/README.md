# Mission 3 — Understand the Operating System

## 1. Task / objective
Explore system information, running processes (PIDs), file paths, permissions (`rwx`), and explain operating system responsibilities.

## 2. Work completed
- Checked OS version, active user, and available storage via terminal.
- Viewed running processes and identified PIDs.
- Tested absolute vs relative paths and inspected file permissions.
- Filled out the OS responsibilities table.

---

### Task 3.1 — Explore Your Operating System

| Information explored | What it tells you | Observation |
| :--- | :--- | :--- |
| **Operating system / system details** | OS version, kernel, and chip type. | macOS 27.2.1, Darwin 27.2.0, 64-bit ARM (`arm64`). |
| **Current account identity** | Current logged-in user. | `shauryaagarwal` |
| **Available and used storage** | Total, used, and available disk space. | Total: 460 GB, Used: 13 GB, Available: 372 GB (4% used). |
| **System activity snapshot** | CPU and memory usage overview. | Low CPU load (~5%), ~400 background processes/threads. |

---

### Task 3.2 — Understand Processes
- **What is a process?** A program that is currently running in memory (RAM).
- **What does the PID column represent?** Process ID, a unique number assigned by the OS to identify and track each running process.
- **Two examples of running processes:**
  1. `launchd` (PID 1): The main macOS parent process that starts system services.
  2. `python3`: The process created when running a Python script.

---

### Task 3.3 — Understand Paths and Permissions

- **Absolute path:** Starts from the root directory `/`.
  - Example: `/Users/shauryaagarwal/digital-detective-8519/mission-03-operating-system/README.md`
- **Relative path:** Starts from the current working folder.
  - Example: `../mission-02-terminal/terminal-practice/practice_file.txt`

#### Permissions on `practice_file.txt` (`-rw-r--r--`)
- **r (Read):** Allowed. File contents can be read.
- **w (Write):** Allowed. File can be edited or deleted.
- **x (Execute):** Denied (`-`). File cannot be run as a program.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Allows opening and reading the file. | Viewing file contents with `cat`. |
| **w — Write** | Allows modifying or editing the file. | Appending text with `>>`. |
| **x — Execute** | Allows running the file as a program. | Running a shell script or entering a folder (`cd`). |

---

### Task 3.4 — Operating-System Responsibilities

| OS responsibility | Explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Schedules CPU time between running programs. | Running a browser while music plays in the background. |
| **Memory management** | Allocates and reclaims RAM memory. | Giving RAM to an app when opened and freeing it on quit. |
| **Device management** | Coordinates hardware with apps via drivers. | Translating trackpad gestures to cursor movement. |
| **File management** | Organizes and tracks files on storage drives. | Saving and opening files on the SSD. |
| **User interface / shell** | Provides a way for users to interact with the OS. | The graphical desktop windows and the Terminal shell. |
| **Security and permissions** | Controls file access and protects system files. | Preventing normal users from editing system files. |

---

## 3. Commands / tools used
- `sw_vers`, `uname -srm`, `whoami`, `df -h /`, `ls -l`

## 4. My understanding
The OS is the manager between computer hardware and apps. It shares CPU time, allocates memory, manages files, and enforces permissions so programs run smoothly without interfering with each other.

## 5. Difficulties faced
Understanding what the `x` (execute) permission means on a folder.

## 6. How I resolved them
On folders, `x` means traversal permission (it lets you `cd` into the folder).

## 7. Evidence / files
- System notes, process notes, permissions table, and OS duties table.

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Branch:** `main`

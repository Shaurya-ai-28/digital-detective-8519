# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
Learn basic terminal commands, practice safe file operations (`>`, `>>`, `cp`, `mv`), understand flags and pipes (`|`), and explain package managers.

## 2. Work completed
- Practiced 9 basic commands in a folder named `terminal-practice/`.
- Practiced overwrite (`>`) vs append (`>>`) and made backup files.
- Tested flags (`ls` vs `ls -lah`) and piping (`ls -lah | head -n 5`).
- Checked Homebrew package manager status.

---

### Task 2.1 — Explore Basic Terminal Operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display** (`pwd`) | Shows current folder path. | Printed current working directory. |
| **Directory listing** (`ls`) | Lists visible files and folders. | Listed files in the folder. |
| **Detailed listing** (`ls -l`) | Shows detailed file info. | Showed permissions, size, date. |
| **Change directory** (`cd`) | Moves between directories. | Changed to parent and back to practice folder. |
| **Create directory** (`mkdir`) | Makes a new folder. | Created `terminal-practice`. |
| **Create empty file** (`touch`) | Creates an empty file. | Created `practice_file.txt`. |
| **Copy file** (`cp`) | Duplicates a file. | Made copy `practice_backup.txt`. |
| **Move / rename file** (`mv`) | Renames or moves a file. | Renamed backup to `notes_backup_v1.txt`. |
| **Display file contents** (`cat`) | Prints file contents on screen. | Printed lines of the text file. |

---

### Task 2.2 — Practise File Changes Safely
1. Created `practice_file.txt`.
2. Line 1: `echo "First line of notes." > practice_file.txt`
3. Line 2: `echo "Second line of notes." >> practice_file.txt`
4. Checked with `cat practice_file.txt` (both lines present).
5. Backup: `cp practice_file.txt practice_backup.txt`, then `mv practice_backup.txt notes_backup_v1.txt`.

**Questions Answered:**
- **Replacing vs Adding:** `>` overwrites and clears previous content; `>>` appends to the end without deleting anything.
- **Copying vs Moving:** `cp` makes a duplicate file (two exist); `mv` renames or relocates the file (one exists).
- **Current directory (`pwd`):** Tells you your exact location so you don't edit or delete files in the wrong place.
- **Directory listing (`ls`):** Lets you verify that files were created, renamed, or saved correctly.

---

### Task 2.3 — Flags and Pipes
- **Flags:** `ls` shows plain names; `-l` shows details; `-a` shows hidden dotfiles; `-h` makes sizes human-readable (KB/MB).
- **Pipes:** `ls -lah | head -n 5` takes the output of `ls -lah` (left side) and passes it directly to `head -n 5` (right side), showing only the first 5 lines.

---

### Task 2.4 — Package Managers
- Running `brew --version` showed Homebrew is not installed on this computer.
- **Why package managers are useful:** They let you install, update, and remove software tools with single commands in the terminal (like `brew install python`) instead of manually downloading setup files from websites.

---

## 3. Commands / tools used
- `pwd`, `ls`, `ls -lah`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`
- Redirection: `>` (overwrite), `>>` (append)
- Pipes: `|` with `head -n 5`

## 4. My understanding
The terminal provides fast, direct control over files. Small utilities can be chained together using pipes (`|`) to filter and view data quickly.

## 5. Difficulties faced
Accidentally using `>` instead of `>>` on the second line.

## 6. How I resolved them
Re-ran the command using `>>` to append the line properly.

## 7. Evidence / files
- Practice folder: `terminal-practice/`
- Files: `practice_file.txt`, `notes_backup_v1.txt`

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Branch:** `main`

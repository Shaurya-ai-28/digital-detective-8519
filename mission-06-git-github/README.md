# Mission 6 — Git and GitHub

## 1. Task / objective
Practice version control with Git and GitHub, create an `update-about` branch, open a Pull Request, and create a Git command glossary.

## 2. Work completed
- Inspected repository status and history using `git status` and `git log`.
- Created and switched to the branch `update-about`.
- Added the `## My Learning` section to root `README.md` and committed it.
- Pushed `update-about` to GitHub and documented the Pull Request workflow.
- Wrote the 9-command Git glossary.

---

### Task 6.1 — Git Workflow

| Git operation | What it does |
| :--- | :--- |
| **Check repository status** (`git status`) | Shows modified, untracked, or staged files. |
| **Stage selected changes** (`git add <file>`) | Adds modified files to the staging area for the next commit. |
| **Create a commit** (`git commit -m "..."`) | Saves staged files permanently to history with a message. |
| **View commit history** (`git log --oneline`) | Displays past commits in chronological order. |

**Staging vs Committing:** Staging (`git add`) lets you pick which files are ready to save; committing (`git commit`) takes the permanent snapshot of those staged files.

---

### Task 6.2 — Create and Use a Branch
1. `git checkout -b update-about`
2. Added `## My Learning` to root `README.md`.
3. `git add README.md`
4. `git commit -m "Add My Learning section to root README"`
5. `git push -u origin update-about`

---

### Task 6.3 — Create a Pull Request
1. Push branch to GitHub (`git push -u origin update-about`).
2. Click **"Compare & pull request"** on GitHub.
3. Set base to `main` and compare to `update-about`.
4. Add description and click **Create Pull Request**.
5. Review the diff in the "Files changed" tab.
6. Merge the PR, then run `git pull origin main` on local laptop.

**Branch and PR purpose:** A branch lets you work on changes without touching working code. A Pull Request lets team members review and discuss code before merging it into `main`.

---

### Task 6.4 — Git Glossary

| Operation | Explanation |
| :--- | :--- |
| **git init** | Creates a new Git repository. |
| **git status** | Shows the state of working and staged files. |
| **git add** | Stages file changes for the next commit. |
| **git commit** | Saves staged changes into version history. |
| **git log** | Lists previous commit snapshots. |
| **git branch** | Lists or creates branches. |
| **git checkout / switch** | Switches to another branch. |
| **git push** | Uploads local commits to GitHub. |
| **git pull** | Downloads and merges remote changes into local branch. |

---

## 3. Commands / tools used
- `git status`, `git add`, `git commit`, `git log`, `git checkout -b`, `git push`

## 4. My understanding
Git branches let you experiment safely. Staging changes before committing ensures each commit is neat and focused.

## 5. Difficulties faced
Deciding when to branch.

## 6. How I resolved them
Always create and switch to the branch before making file edits.

## 7. Evidence / files
- Branch `update-about` pushed to GitHub.
- PR Link: https://github.com/Shaurya-ai-28/digital-detective-8519/pull/new/update-about

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Branch:** `main` (and `update-about`)

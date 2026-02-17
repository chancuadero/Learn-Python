This is Day 24 of learning Python

Topic: Git
Summary: Version control is a group of processes and systeams to manage changes to files, programs, and directories. Git is a version control system most commonly used by software developers. It is designed to manage and track changes to source code and other files during software development.

1. What is a Git repo?
   Git repo is a directory containing files and sub-directories, and Git storage (.git). The benefits of creating repos are the ability to systematically track versions, revert to previous versions, enables collaboration with colleagues, and compare versions at different points in time.
   To create a new repo, use git init name(replace with actual name of the repo).
   Different git commands: https://education.github.com/git-cheat-sheet-education.pdf
   FOR REFERENCE: https://www.w3schools.com/git/

2. Git commits have three parts:
   a. Commit
   -contains the metadata - author,log,message,commit time
   b. Tree
   -tracks the names and locations of files and directories in the repo
   -like a dictionary - mapping keys to files/directories
   c. Blob
   -Binary Large Object
   -may contain data of any kind
   -a compressed snapshot of a file's contents
3. Git hash
   Hash is a 40 character string of numbers and letters. Git produces Pseudo-random number generator (hash function). It allows data sharing between repos.
4. Git diff
   git diff = Show changes between all unstaged files and the latest commit
   git diff report.md = Show changes between an unstaged file and the latest commit
   git diff --staged = Show changes between all staged files and the latest commit
   git diff --staged report.md = Show changes between a stayed file and the latest commit
   git diff 35f4bfd 186398f = Show changes between two commits using hashes
   git diff HEAD~1 HEAD~2 = Show changes between two commits using HEAD instead of commit hashes
5. Git revert
   git revert HEAD = Revert all files from a given commit
   git revert HEAD --no-edit = Revert without opening a text editor
   git revert HEAD -n = Revert without making a new commit
   git checkout HEAD~1 -- report.md = Revert a single file from the previous commit
   git restore --staged report.md = Remove a single file from the staging area
   git restore --staged = Remove all files from the staging area

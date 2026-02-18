This is Day 25 of learning Python

Topic: Intermediate Git
Summary: Branch is an individual version of a repo. Git uses branches to systematically track multiple versions of files. In each branch, some files might be the same, others might be different, and some may not exist at all.

> Why use branches?

1. Multiple developers can work on a project simultaneously.
2. Compare the state of a repo between branches.
3. Combine contents, pushing new features to a live system.
4. Each branch should have a specific purpose.

> Identifying branches
> Note: Creating a new branch means "branching off"

1. git branch - lists all branches. \* indicates the current branch.
2. git switch main - switch back to main
3. git branch speed-test - creating a new branch called speed-test
4. git switch -c speed-test - alternatively, to create a new branch called speed-test and switch to it
5. git branch -m (new name) - rename branch to its new name
6. git branch -d (branch name) - delete a branch

> Steps in merging branches
> Example: move ai-assitant branch to main branch

1. Move to the destination branch:
   git switch main
   -git merge (source)
   -from main, to merge ai-assistant into main:
   git merge ai-assistant
   -from another branch: git merge source destination
   git merge ai-assistant main

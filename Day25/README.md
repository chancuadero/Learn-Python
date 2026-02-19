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

> Merging Conflicts

1. Conflict - inability to resolve differences in the contents of one or more files between branches. For example, if we edit the same file in two different branches, then try to merge, Git won't know which version should be kept.
2. Steps to resolve conflict:
   a. Open the file using nano (name of the file)
   b. Edit the file based on which data should only exists in it.
   c. Save the file using ctrl + O > enter > ctrl + X
   d. Merge the resolved file using git add (name of the file)
   e. Then, commit it to the destination branch using git commit -m "Resolving conflict"

> Remote Repos

1. Remote repo - is a repo stored in the cloud through an online repo hosting service such as GitHub.
2. If out computer breaks down or we lost it, we can use a different computer to access our project from the remote repo as it is backed up there.
3. To clone a remote report use git clone URL(the URL of the online hosting service)
4. git remote - list all remotes associated with the repo
5. git remote -v - to get more information about the remote(s)
6. When cloning, Git will automatically name the remote origin
7. We can add more remotes by specifying a name for Git to assign. Using git remote add command, and provide two informations - the name that we would like to assign to the remote repo, and the URL (the path to the directory). [git remote add name URL]

> Pulling from remotes

1. Fetching from a remote to a local report, we do this using git fetch, providing the name of the remote.
2. Git allows us to fetch and merge using a single command. We execute git pull followed by the remote repo's name, which will fetch the default branch from the report and merge it into the local repo's current branch.
3. We can specify which remote branch to pull from by including the branch name after the remote name. [git pull origin dev]

> Pushing to remotes

1. Push repo is where we merge our local's repo content into a remote. We can push to a remote using the git push command, supplying two arguments. First we provide the remote, followed by the local branch. [git push remote local_branch]

# Git


###### Change Committer and Author while preserving original dates during rebase

Begin a rebase at the commit you want to change then enter this for each commit:
```shell
export GIT_COMMITTER_NAME=$(git config user.name) && export GIT_COMMITTER_EMAIL=$(git config user.email) && export GIT_COMMITTER_DATE=$(git show --no-patch --format=%aD) && git commit --amend --author="$(git config user.name) <$(git config user.email)>" --no-edit && git rebase --continue  
```

## Devlopment Workflow:
=========================

<img width="975" alt="image" src="https://user-images.githubusercontent.com/35987583/190879439-2ec8099d-bca1-42c0-8166-c20f70984090.png">


```bash
Branches:
Master - Main Branch

Develop Branch - Branch of Master Branch

Feature Branch - Branch of Dev Branch. We will create branch from dev branch for feature devlopment and work on it. Once our work is completed we will merge changes to dev branch. Develop branche later will be merged to Master.
```


Choose Project:
```bash
- Select respective project. (midmarket or mid-market-ui)
- we will have master branch and develop branch for project.
- We will create branch (For feature development of bug fix) from develop branch. 
```

Go to Project Directory in Local: Check our git is up and running
```bash
> cd /Users/JBhutka/repos/mid_market
> git status
```

First create local branch: to work on feature, so we can make changes in local
```bash
> git branch branchNameBug522
> git checkout branchNameBug522 // In order to make changes to code locally
> git branch // To make sure we are on branchNameBug522
```

git status - To see untrack changes in our local branch
```bash
> git status
```
<img width="541" alt="image" src="https://user-images.githubusercontent.com/35987583/190879880-1184f531-4ebc-4189-8542-bdcb3e218f1f.png">


Copy past file and its location that you wanted to add in current branch
```bash
> git add .poetry-installer-error-7xxp41rh.log.swp
> git status // You will see the file (uncommited changes) in green that you can commit.
```
<img width="549" alt="image" src="https://user-images.githubusercontent.com/35987583/190879973-07eba49f-fecd-4d75-a989-545630b3eb14.png">


Commit this changes in you local repo. This command will only commit changes locally.
```bash
> git commit -m 'This is my first commit'
```

Now we are ready to push out commit to remote repo. With this command we have now pushed our local commit from local branch (branchNameBug522) to remote branch (branchNameBug522). we will be now able to see the changes in remote branch (same branch we were working locally). This command will also generate url to create pull request. You can now create PULL request for devloper branch.
```bash
> git push -u origin branchNameBug522
```

<img width="808" alt="image" src="https://user-images.githubusercontent.com/35987583/190880246-59345bf6-ab58-4496-b851-07afabaaca99.png">


```bash
- Create Pull request from URL. 
- Add reviewer.
- Ask reviewer to review it, they will merge our commit and PR it to developer branch
```


At Any point you can switch to other branch. (eg. developer branch)
```bash
> git checkout feature-developer
```

Once checkout alway do, git pull. To get latest all the changes from remote repo devloper branch to local
```bash
> git pull origin branchName
```

You can list out all the local and remote branch
```bash
> git branch -a
```
<img width="404" alt="image" src="https://user-images.githubusercontent.com/35987583/190880450-bcb4da28-51ec-4cbc-b079-283ca0d1f526.png">



You can delete local branch
```bash
> git branch -d branchName
```

You can delete remote branch using following command
```bash
>git push origin --delete branchName
```



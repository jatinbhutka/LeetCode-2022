
#### Undo Commit:
```
git reset --soft HEAD~1
```

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/35987583/195910100-4d2cccc6-a372-4c7a-8e01-3e4965aeb086.png">
<img width="980" alt="image" src="https://user-images.githubusercontent.com/35987583/195910186-f055847d-1481-4c25-9e54-a4b12bd867b8.png">


```
git reset --hard HEAD~1
git reset --soft HEAD~2

```
<img width="991" alt="image" src="https://user-images.githubusercontent.com/35987583/195910283-88e72acb-59be-4432-be93-2f130634d555.png">
<img width="1055" alt="image" src="https://user-images.githubusercontent.com/35987583/195910348-0d2e09b9-8285-4897-9a82-554eb2847ee2.png">


#### Branching:

```
git branch
# To see all the branches and current branch
```

```
git branch newBranch
# To create newBranch
```

#### Branch Checkout:
```
git checkout branchName
# To swtich to branchName
```

```
git checkout -b new_branch
# to create and checkout to new branch which is created
```

#### When you switch from one branch to other it will have there own changes, not reflect the changes you made on other branches.
<img width="1011" alt="image" src="https://user-images.githubusercontent.com/35987583/195917926-5a292d95-0b8e-4bd5-b644-3689f8df1c59.png">

#### Renaming Branch:
```
## From Branch you are on:
git checkout new_branch
git branch -m authentication_feature



# From Diff branch:
git branch -m old_name new_name
git branch -m new_branch authentication_feature
```
<img width="1033" alt="image" src="https://user-images.githubusercontent.com/35987583/195918371-53a5822b-f029-4576-a7cf-6a1b8780ab0d.png">
<img width="1017" alt="image" src="https://user-images.githubusercontent.com/35987583/195918505-c22aea0f-7875-45c5-a2cf-086e4ed136ba.png">


#### Using git branch to delete a branch:
```
git branch -d <branch_name>
git branch -d new_branch
```

#### Git Stash:

```
git stash
```

<img width="1042" alt="image" src="https://user-images.githubusercontent.com/35987583/195919949-8433734a-9f5f-4c14-a72a-bc6912803898.png">
<img width="998" alt="image" src="https://user-images.githubusercontent.com/35987583/195919985-9c49f8a2-52a8-41d8-a009-67c79947d0ec.png">
<img width="1002" alt="image" src="https://user-images.githubusercontent.com/35987583/195920095-df31e62b-4607-4b70-80b4-9fb1bac20b44.png">


## Any commit we make, will only be reflected in that particular banch only.

#### Git Merge:

```
# branch_to_be_merged will be merged to Master
git checkout master
git merge <branch_to_be_merged>
git merge feature_branch
```

<img width="1018" alt="image" src="https://user-images.githubusercontent.com/35987583/195921470-488c4be0-8b42-44cc-a6aa-e9ce19c827d5.png">
<img width="1007" alt="image" src="https://user-images.githubusercontent.com/35987583/195922647-b739f663-6a43-4352-a0ec-6638f767de7d.png">



### Merge Conflicts:

<img width="1042" alt="image" src="https://user-images.githubusercontent.com/35987583/195957967-95d6f0a1-183c-424c-b0c0-9567dde490bc.png">
<img width="1027" alt="image" src="https://user-images.githubusercontent.com/35987583/195958013-c0b0166b-c578-43d9-99ef-9f8998a5e606.png">

<img width="971" alt="image" src="https://user-images.githubusercontent.com/35987583/195958333-451dff77-95ca-46e0-a9d9-40dfca157a89.png">



#### Git and GitHub:

Git - Git create local repo on every contributor's computer

GitHub - Platfor that stores the whole codebase in remote repo.


#### The git remote command:
<img width="1007" alt="image" src="https://user-images.githubusercontent.com/35987583/195961062-d806661b-0ce6-4c3a-b0a6-862b6d5a6c97.png">


#### The git push command:

```
git push origin master
git push <remote_repository> <branch_name>
```

<img width="988" alt="image" src="https://user-images.githubusercontent.com/35987583/195961095-9a353a9c-11fd-4935-a991-933602c8c5d7.png">
<img width="1007" alt="image" src="https://user-images.githubusercontent.com/35987583/195961079-bb1e1e13-b2c0-4a56-aea9-f211dbff8127.png">




#### Git Fetch:

git fetch is used to download the updated changes from a remote repository. If you are working in a collaborative environment and want to see how other people might have updated the remote repository between now and the last time you viewed it, you will need to use the git fetch command.

<img width="1060" alt="image" src="https://user-images.githubusercontent.com/35987583/196024585-cd4da1f1-8787-43c3-b95e-160e3c272d4a.png">
<img width="994" alt="image" src="https://user-images.githubusercontent.com/35987583/196024600-24401137-e65d-451b-beb5-5e07615416ce.png">



#### The git pull:








#### The git rebase:
<img width="1057" alt="image" src="https://user-images.githubusercontent.com/35987583/196030557-ce365c62-d1d8-405d-a474-19465cfd3e60.png">
<img width="1006" alt="image" src="https://user-images.githubusercontent.com/35987583/196030564-f4503d75-5b38-46ca-a421-f28116adceac.png">
<img width="964" alt="image" src="https://user-images.githubusercontent.com/35987583/196030574-5791e1b4-abb2-48d5-9c40-fc4093e30592.png">
<img width="885" alt="image" src="https://user-images.githubusercontent.com/35987583/196030579-d1b03deb-8918-4ffa-8776-a1b88069771b.png">
<img width="1032" alt="image" src="https://user-images.githubusercontent.com/35987583/196030587-71fd6720-9287-495e-b97f-278084bfd877.png">
<img width="993" alt="image" src="https://user-images.githubusercontent.com/35987583/196030591-8285646b-cb37-42cb-a7f0-b8409a8277be.png">











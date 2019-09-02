# cmake-app
Simple app for cmake demo

# Manging externals as subtrees

https://medium.com/@porteneuve/mastering-git-subtrees-943d29a798ec

## Adding an external
```
git remote add <remote> <url>
git fetch --depth=1 <remote> master
git read-tree --prefix=externals/<remote> -u <remote>/master
...
git ci -m "Added external"
```

## Fetching updated content
```
git fetch --depth=<N> <remote> master
git merge -s subtree --squash --allow-unrelated-histories <remote>/master
```

## Backporting content

Commits for backport can contain modifications to external as well as main
project. subtree merge strategy for cherry-pick will discard unrelated changes.


```
git co -b <remote> <remote>/master
git cherry-pick --strategy=subtree <commit>...
git push <remote> HEAD:master
```

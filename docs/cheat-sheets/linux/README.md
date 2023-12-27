# Linux

### Disk and Files

###### Find disk usage for the current working directory
```shell
sudo du --max-depth=1 --block-size=MB ./* | sort -n
```
###### Find all hardlinks
```shell
find -type f -links +1
```

### APT

###### Fix APT when stuck on User prompt from automated process: 
```shell
sudo fuser -vki -TERM /var/lib/dpkg/lock var/lib/dpkg/lock-frontend
sudo dpkg --configure -a
```

###### Another option:
```shell
sudo fuser --vki /var/cache/debconf/config.dat
```

###### Fix broken packages 
```shell
sudo apt install -y --fix-broken
```

###### Run a shell script remotely without transferring to disk
```shell
ssh -o ConnectTimeout=10 -T node1 "VAR1=${VAR1} bash -s" < ./script.sh
```

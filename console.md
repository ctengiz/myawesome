#### Test Mail

`echo Test | mail -s Test1 xx@yy.com`

#### Rsync 

`rsync -arvzhu source_directory destination`

-a archive
-r recursive
-v verbose
-z compress
-h human readable
-u update

#### Nmap

Scan alive hosts
`nmap -sP 172.16.0.0/24`


### Tips

Temp fix for sudo graphical application error
`xhost +`

Send process to background
`python program.py > /dev/null 2>&1 & disown`

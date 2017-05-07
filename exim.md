http://bradthemad.org/tech/notes/exim_cheatsheet.php


# Bir kullanıcıdan gelen mesajları bulmak :
exiqgrep -f [luser]@domain

-i beslenirse o greplenen mesajalrın id'si gelir.

# Bulunan bir mesaj hakkında bilgi almak :

- exim -Mvh <mesaj-id>  # header
- exim -Mvb <mesaj-id>  # body
- exim -Mvl <mesaj-id>  # logs

# Bulunan mesajları silmek :

exiqgrep -i -f [luser]@domain | xargs exim -Mrm

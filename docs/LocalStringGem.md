
# To get locally string on linux

- if u dont want to install using repl and have desktop and git installed or termux is also fine,just run these in terminal

```
    sudo apt-get update
    sudo apt get-install -y\
        python3\
        wget \
        curl\
        python3-dev

    wget https://raw.githubusercontent.com/TeamZenX/Vision/blob/master/SessionStringGen.py

    python3 SessionStringGen.py
```


# For windows


- Note: You need  python installed in your computer


1st - Open terminal and type `python` there


then paste the following code


```
import requests


url = 'https://raw.githubusercontent.com/TeamZenX/Vision/master/SessionStringGen.py'
r = requests.get(url, allow_redirects=True)

open('SessionStringGen.py', 'wb').write(r.content)

#  then hit enter

```
now type

```
exit()
```


- at Last do this in your terminal
```
python SessionStringGen.py
```

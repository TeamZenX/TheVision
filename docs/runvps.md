### Host on Server/Vps/LocalDevice [For Devs]


- Create A local.env file


```
Reference here https://github.com/TeamZenX/VisionEnv

```
- Install package

```
pip3 install virtualenv
```

- Install Git

**Choose accorrding to your distro**

```
https://git-scm.com/download/linux
```

- Clone the repository

```
git clone https://yourgitusername:access_token@github.com/TeamZenX/Vision.git

```

- After Cloning cd into the directory

```
cd Vision
```


- Create Enviorment

```
virtualenv -p /usr/bin/python3 venv
```

- Activate the env

```
source venv/bin/activate
```

-  Run Bash File

```

bash configure.sh

```


- Run Client

**If a server**

```
screen python3 -m vision
```

**On Local Device**

```
 python3 -m vision
```

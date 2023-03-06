#VM ubanto 20.04 setup
> เชื่อมผ่าน SSH

## 1. ลง pip
- sudo apt update
- sudo apt install python3-pip

## 2. ลง package ที่จำเป็น
- pip install selenium
- pip install google-api-python-client
- sudo pip install --upgrade google-api-python-client
- pip3 install webdriver-manager (selenium4 update)
## 3. ลง token ของ google calendar api
- mkdir source
- cd source
- wget "https://drive.google.com/uc?export=download&id=1tEWrEkrIWmbzPnB3gHrA42xFcnFd_C5n" -O "token.pkl"
- pip3 install --upgrade requests
- cd

## 4. ลง chromium
sudo apt install --assume-yes chromium-browser
หา path chromium : which chromium-browser
-> ได้ /usr/bin/chromium-browser

## 5. ทำ debian buster
sudo nano /etc/apt/sources.list.d/debian.list
```
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
EOF
```

## 6. Add key 
- sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
- sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
- sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A
- sudo apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg
- sudo apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg
- sudo apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg

## 7. ทำ debian repo for chromium* packages only
sudo nano /etc/apt/preferences.d/chromium.pref
```
Package: *
Pin: release a=eoan
Pin-Priority: 500


Package: *
Pin: origin "deb.debian.org"
Pin-Priority: 300


Package: chromium*
Pin: origin "deb.debian.org"
Pin-Priority: 700
EOF
```

## 8. ลง Script จาก "/script" ใน "source"
- cd source
- sudo nano ...
    - sudo nano main.py
    - sudo nano privateData.py
    - sudo nano analysisData.py
    - sudo nano analysisLecture.py
    - sudo nano googleCalendarFunc.py

## 9. ตั้ง task เพื่อ เปิดและปิด VM อัตโนมัติ
follows : https://learn.microsoft.com/en-us/shows/it-ops-talk/auto-shutdown-and-auto-start-an-azure-vm

## 10. เขียน scrupt ให้รันไฟล์ main.py อัตโนมัตื
follows : https://www.youtube.com/watch?v=Gl9HS7-H0mI
sudo crontab -e
add : @reboot python3 /home/GIBBIN/source/main.py &
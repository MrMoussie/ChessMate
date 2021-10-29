***Please follow the steps in this guide to make sure that the game will work as intended!***

# GAME
This is a step-by-step instruction to install the necessary modules to run the game.

## Installation 
Use the following commands on your Raspberry Pi to install the necessary modules:
*In case a command does not work for you, try updating your Raspberry Pi first.*

Install PyGame:
```bash
sudo pip3 install pygame
```

Install PyGame_GUI:
```bash
sudo pip3 install pygame_gui
```

Install Tkinter:
```bash
sudo apt-get install python3-tk
```

Install Chess:
```bash
sudo pip3 install chess
```

Install Speech Recognition:
```bash
pip install SpeechRecognition
```
Install PyAudio:
```bash
sudo pip3 install pyaudio
```

```diff
-*In case of errors with PyAudio installation:*
```
```bash
sudo apt install portaudio19-dev python3-pyaudio
```

# SQL
This is a step-by-step instruction to install the necessary modules to run the SQL server.
## Installation 
Use the following commands on your Raspberry Pi to install the necessary modules:
*In case a command does not work for you, try updating your Raspberry Pi first.*

Install MariaDB Server:
```bash
sudo apt install mariadb-server
```

MySQL Module for Python:
```bash
sudo pip3 install mysql-connector
```

ConfigParser Module for Python:
```bash
sudo pip3 install configparser
```

## Configuration
*Optional:* Follow this [guide](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql) to make a new user in mysql with priviliges on your Raspberry Pi.

Configurate the [SQL.cfg](https://gitlab.utwente.nl/s2297205/mod05_group17/-/blob/master/src/SQL/SQL.cfg) file. 
Enter credentials for the program to access the mysql server.
*Must have permissions for creating databases and tables as well as altering permissions.*
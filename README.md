# LOGIN
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
Configurate the [SQL.cfg](https://gitlab.utwente.nl/s2297205/mod05_group17/-/blob/sql/SQL/SQL.cfg) file. 
Enter credentials for the program to access the mysql server.
*Must have permissions for creating databases and tables as well as altering permissions.*
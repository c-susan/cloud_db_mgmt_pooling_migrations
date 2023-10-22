# cloud_db_mgmt_pooling_migrations
HHA504 / Cloud Computing / Assignment 4c / Cloud DB Management


# Documentation
## 1. MySQL Cloud Instance Setups
### Google Cloud Platform (GCP) Setup
In GCP, I created a MySQL instance with the following customizations: 
+ **Database version:** MySQL 8.0 
+ **Cloud SQL edition:** Enterprise
+ **Preset:** Sandbox
+ **Machine Configuration:** Shared core; 1 vCPU, 0.614 GB
+ In **Conections**>**Authorized Networks**, added an allow all network: ```0.0.0.0/0```. 

### Azure Setup
Using the Azure MySQL service, I created a flexible MySQL server with the following customizations: 
+ Burstable compute tier with Standard_B1s (1 vCore, 1GiB memory, 400 max iops) compute size 
    + ```max_connections```: 20
    + ```connect_timeout```: 3
+ In the Networking section, added a new Firewall rule: ```0.0.0.0 - 255.255.255.255```. 

## 2. Database Schema and Data 
I created a new database the MySQL instances: 
1. In the google shell terminal, signed into MySQL with: ```mysql -u <username> -h <host IP address/servername> -p```. 
2. Created a database called 'susan': ```create database `susan`;```
3. Ran ```show databases;``` to confirm the database was created and then signed out of MySQL. 

In order to create a new tables, I did the following to create a connection to MySQL: 
1. Created a .env file to contain my database credentials that contains the following: 
```
DB_HOST=504migrations.mysql.database.azure.com
DB_DATABASE=susan
DB_USERNAME=susan
DB_PASSWORD=hhA5041314520
DB_PORT=3306
DB_CHARSET=utf8mb4


For both the azure and gcp MySQL instances, I created the same database name and the same tables in a .py file. The first is a ```doctors``` table that includes data on doctor IDs, their names, the department they work in, and their phone number. The second table is a ```patients``` table and contains patient IDs, their names, date of birth, and their primary doctor ID, which references the doctor ID in the doctors table. I populated data into the tables using another .py using sample data generated using Faker. 
    + In the doctors table, there is a column for phone number. In order to populate correct data into that column, I first had to create a function into order to put the sample data in correct format using the following code: 
```
def phone_number():
    # Generate random numbers for each part of the phone number
    p1 = str(random.randint(1, 999)).zfill(3)
    p2 = str(random.randint(0, 999)).zfill(3)
    p3 = str(random.randint(0, 9999)).zfill(4)

    format = f"{p1}-{p2}-{p3}"
    return format
``` 
    + In the patients table the ```primary_doctor_id``` is a foreign key that references the ```doctor_id``` in the doctors table. In order fo the column to populate with data from the doctors tables, I had to use the following code: ```primary_doctor_id=session.query(Doctor).order_by(func.rand()).first().doctor_id```.
 


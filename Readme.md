# Teacher Brain Fitness

[![GitHub contributors](https://img.shields.io/github/contributors/code4romania/standard-repo-template.svg?style=for-the-badge)](https://github.com/code4romania/standard-repo-template/graphs/contributors) [![GitHub last commit](https://img.shields.io/github/last-commit/code4romania/standard-repo-template.svg?style=for-the-badge)](https://github.com/code4romania/standard-repo-template/commits/master) [![License: MPL 2.0](https://img.shields.io/badge/license-MPL%202.0-brightgreen.svg?style=for-the-badge)](https://opensource.org/licenses/MPL-2.0)

Educators play a crucial role in our development as people. Thus, it is very important to understand how we can help them and how we can equip them with the instruments they need in order for them to take care of our children. Their initial formative period, as professionals, doesn't always provide them with the knowledge they need in order to manage the socio-emotional aspects of teching children and teens. 

Teacher Brain Fitness is our solution to this problem. It is an application designed to provide short lessons, on subjects that cover a wide spectrum of subjects, such as:
* identifying children who have difficulties learning
* managing difficult situations inside the classroom
* helping children with special needs integrate in the group of students

These lessons are meant to teach good practices and guide educations through situations that they might have trouble dealing with.

To find out more about this project, [check it out on Civic Labs](https://civiclabs.ro/ro/solutions/teacher-brain-fitness), the Code for Romanian research and prototyping program. 

You can find the full description of the solution [here](https://civiclabs.ro/ro/byproducts/descrierea-produsului-teacher-brain-fitness), complete with user actions and user stories.

[Contributing](#contributing) | [Built with](#built-with) | [Repos and projects](#repos-and-projects) | [Deployment](#deployment) | [Feedback](#feedback) | [License](#license) | [About Code4Ro](#about-code4ro)

## Contributing

This project is built by amazing volunteers and you can be one of them! Here's a list of ways in [which you can contribute to this project](.github/CONTRIBUTING.MD).

You can also list any pending features and planned improvements for the project here.

## Built With

### Programming languages

- Python

### Platforms

- Flask


### Package managers

### Database technology & provider

- MySQL

## Repos and projects

Mention all related repos and projects.

## Deployment

### Fork this repo

Fork this repo by clicking Fork on github.

### Clone your fork

    $ git clone https://github.com/[your-username]/brain-fitness-api.git
    $ cd brain-fitness-api

### Initialize a virtualenv

    $ pip install virtualenv
    $ virtualenv venv
    $ . venv/bin/activate

### Install dependencies

    $ pip install -r requirements.txt
    
### Create the MySQL database

Please create the database before proceeding. You will need the database credentials in the next step.

**Credentials you will need**:
- Database name
- Database username
- Database password
- Database address (if it is on your local machine with default settings, the address is `127.0.0.1:3306`) 

### Setup config.ini

Create a new file inside the `brain-fitness-api/` folder named `config.ini` and copy-paste the configuration from the `config.example.ini` file.

In the freshly created `config.ini` make sure you set the database connection string (`SQLALCHEMY_DATABASE_URI`) correctly.

If your database user is `admin`, your password is `password` and your database name is `code4_brainfitness`, the connection string will look like this:

```ini
SQLALCHEMY_DATABASE_URI = mysql+pymysql://admin:password@127.0.0.1:3306/code4_brainfitness
```

You can also adjust any constant from config.ini to match your needs. This file will not be pushed on the repo.

### Upgrading the database

    $ export FLASK_APP=run.py
    $ flask db upgrade

### Run the app

    $ python run.py

Or:

    $ flask run

By default, the app will run at `brainfitness.code4:8282`. 
Update your `/etc/hosts` to point to 127.0.0.1 for `brainfitness.code4` so that your computer can access the virtual host.

    127.0.0.1       brainfitness.code4
    

### Updating database (Adding/Editing/Removing columns)

Steps required:
- Modify model file (`app/models/[model_name].py`) and add/edit/remove the columns you want
- Generate migration script: 
```
    $ flask db migrate
```
- Run migration (upgrade)
```
    $ flask db upgrade
```

**USEFUL**: You can edit the migration script located in `migrations/versions/[version].py` and add a descriptive message for that migration.
To do this, just replace "empty message" with your message (on the first line).
 
## License 

This project is licensed under the MPL 2.0 License - see the [LICENSE](LICENSE) file for details

## About Code4Ro

Started in 2016, Code for Romania is a civic tech NGO, official member of the Code for All network. We have a community of over 500 volunteers (developers, ux/ui, communications, data scientists, graphic designers, devops, it security and more) who work pro-bono for developing digital solutions to solve social problems. #techforsocialgood. If you want to learn more details about our projects [visit our site](https://www.code4.ro/en/) or if you want to talk to one of our staff members, please e-mail us at contact@code4.ro.

Last, but not least, we rely on donations to ensure the infrastructure, logistics and management of our community that is widely spread across 11 timezones, coding for social change to make Romania and the world a better place. If you want to support us, [you can do it here](https://code4.ro/en/donate/).

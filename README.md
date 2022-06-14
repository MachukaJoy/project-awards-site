#  Awards Clone

### A clone of the website [Awwards](https://www.awwwards.com/) 

#### By **Joy Machuka**

+ [Description](#Description)
+ [How to run the code](#Setup)
+ [Live Site](#Live-Site)
+ [Technologies](#Technologies-and-Languages-Used)
+ [Authors Info](#Author)
+ [Licence](#Licence)

# Description
The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.<br>
A project can be rated based on 3 different criteria<br>
* Design
* Usability
* Content<br>
These criteria can be reviewed on a scale of 1-10 and the average score is taken.
## Live-Site
[View Site](https://machukawards.herokuapp.com/)

## BDD
* As a user, I would like to View posted projects and their details.
* As a user, I would like to Post a project to be rated/reviewed.
* As a user, I would like to Rate/ review other users' projects.
* As a user, I would like to Search for projects.
* As a user, I would like to View projects overall score.
* As a user, I would like to View my profile page.

## Setup

To get the project .......  
  
##### Fork then Clone the repository:  
 ```bash 
git clone https://github.com/MachukaJoy/project-awards-site.git 
```
##### Navigate into the folder
 ```bash 
cd project-awards-site
```
##### Create and activate virtual environment  
 ```bash 
pipenv –-three
```
##### Activate Virtual Environment
 ```bash 
pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv  install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations review
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test review
```
Open the application on your browser `127.0.0.1:8000`.


## Known Bugs
There are not any known bugs as at now. But feel free to let us know should you find any.

## Technologies-and-Languages-Used
* Python
* Visualstudio
* Django
* postgress sql

## Support and contact details
Should you have any issues or questions, ideas or concerns feel free to reach out to me. Also feel free to make contribution to the code and can contact me at machukajoy@gmail.com
## Author

- [Joy Machuka](https://github.com/MachukaJoy)
### Licence
[MIT LICENSE](https://github.com/MachukaJoy/project-awards-site/blob/main/LICENSE)<br>


** <br>
Copyright (c) {2022} [Joy Machuka ](https://github.com/MachukaJoy)
# BLOGOMATIC 

## Author
 [Alvynah Wabwoba](https://github.com/alvynah)


# Description
This is a flask web application whose actors are users and writers.Writers are allowed to post blogs, edit blogs and even delete them.Users are allowed to vote, downvote and comment on blogs. A blog owner can delete offensive comments.Users can also subscribe to the website for an alert when a new blog is posted.



## Screenshot

## Live Link
[Blogomatic](https://blogomatisized.herokuapp.com/)

## User Story

1. As a user, I would like to view the blog posts on the site
2. As a user, I would like to comment on blog posts
3. As a user, I would like to view the most recent posts
4. As a user, I would like to an email alert when a new post is made by joining a subscription.
5. As a user, I would like to see random quotes on the site 
6. As a writer, I would like to sign in to the blog.
7. As a writer, I would also like to create a blog from the application.
8. As a writer, I would like to delete comments that I find insulting or degrading.
9. As a writer, I would like to update or delete blogs I have created.

## Behaviour Driven Development (BDD)

### USERS

1. Comment

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the comment icon on the blog   | comment| The user is redirected to a page where they can comment and see other comments on that blog  | 

2. Subcribe to website 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter email in the subscription form and submit   | email| A welcoming email is sent to the subscriber and an alert email will be sent every time a new blog is posted  | 


3. Upvote Blog

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the upvote icon on the blog   | upvote| The number of likes is incremented by one on each click  |  

4. Downvote Pitch

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the downvote icon on the blog   | downvote| The number of dislikes is incremented by one on each click  |  


### WRITERS

1. Sign Up

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Select sign up from the navigation bar    | Email, Username, Password|   Writer is redirected to log in page   |  


2. Log in

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Select login from the navigation bar / actions that redirect to login    | Email, password |  Writer is authenticated and redirected to landing page|  


3. New Blog

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Writer selects new pitch from navigation bar,once they are logged in    | Title, Blog| Writer is redirected to landing page where the created blog is displayed   |  


4. Delete Comment

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the delete icon on the comment which is available only to the author of the blog  | comment|  The comment is deleted   |  

5. Edit Post

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the edit icon on the blog from the user profile   | blog| The blog is edited and posted   |  

6. Delete Post

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the delete icon on the blog from the user profile   | blog| The blog is deleted and all its properties   |  





## Setup/Installation Requirements
### Getting the code
1. clone repository
    https://github.com/alvynah/blogomatic.git
    
2. Move to the folder and install requirements
    cd blogomatic
    pip install -r requirements.txt
### Running the Application
1. Run main apllication
   * Change in manage.py create_app('development')
2. Run tests
    * Change in manage.py create_app('test')
   * python3.6 manage.py test

## Technologies Used

* Python3.6
* Flask framework
* Bootstrap
* PostgreSQL
* CSS

## Contact Information
For any further inquiries or contributions or comments, reach me at [Alvynah](juvatalvynah@gmail.com)
### License
[MIT License](https://github.com/alvynah/blogomatic/blob/master/License)

Copyright (c) 2021 **Alvynah Wabwoba**
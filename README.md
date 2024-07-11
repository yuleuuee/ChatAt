—— :: Before Running the “ChatAt” project following steps should be followed :: ——
************************************************************************************************
 
1.     Need to install python version 3 or above. This will automatically install “pip3”.
2.     Then from the terminal (if mac OS ) or command prompt (if windows OS) we need to install django , mysql-client,my-sql,mysql-connector-python,pillow,certify.
	·      pip3 install django
	·      pip3 install mysql-client
	·      pip3 install my-sql
	·      pip3 install mysql-connector-python
	·      pip3 install pillow
	·      pip3 install certify
 
3. In order to connect with the database, we first need to make migration using command lines(but first need to navigate to the project folder "chat_app" from the terminal)
	·      python3  manage.py makemigrations
	·      python3  manage.py migrate
(Remember, whenever we make any changes in the ‘models.py’ file ,we need to run the above two commands in order to save the changes in the database)
 
4.  To make an Admin user account:
	·      python3 manage.py createsuperuser
	·      Then need to enter admin username , email , and password.
	·      Then we are ready to use admin page as well
 
5. To run the project in then website  :
	·      First need to run “python3 manage.py runserver” command on terminal
 
6. To Open the Platform in Browser :
	·      Open the link provided in the commend lines or terminal that we got after running “python3 manage.py runserver”
	·      This will open the “login/signup page” of the ChatAt platform.
	( If we want to use the default Admin panel , then we can simply go to “http://127.0.0.1:8000/admin/” in the browser and then by entering the admin user’s username and password , an admin page will be visible.)
 
7. After entering the correct username and password , users can enter to the main page of the platform. Then ,from there users can navigate to different pages just from the navigation bar.

8. There are total 6 page in the platform with their own unique features :
	i) Login/Signup page 
	ii) Public page 
	iii) Profile page
	iv) Account Setting Page
	v) Chat page
	vi) Forgot password page

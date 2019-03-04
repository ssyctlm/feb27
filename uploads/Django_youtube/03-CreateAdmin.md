#  Built-in Components(APPS)

## Create a super user (Admin: http://127.0.0.1:8000/admin)

1.  To run the server in the virtual environment , using the following prompt:

   ``` cmd
   (trydjango)> python manage.py runservice ip:port # if you don't setting the ip and port , it will set default as 127.0.0.1:8000
   ```

   and enter the address in the browser, we can see the project is running. 

   In the file setting.py,  we can see there are some of built-in components(APPS) in "INSTALLED_APPS", and the first one is ` admin ` , we can rewrite the address of running project by adding ` /admin ` , we can see there is a user login window but we don't have the username and password.

   Now,  I will do the following steps to create a super user (Admin) 

2. Open another PowerShell to activate the VE again. 

3. First using ` migrate ` to initiative/ synchronize the database, It's important, I hadn't done that at the first time and then I received tons of Errors.

   ``` cmd
   (trydjango) > python manage.py migrate
   # some infomation here
   (tyrdjango) > python manage.py createsuperuser
   username:
   mail
   password
   tryagain 
   
   ## Ok, all done
   ```

   

4. So, you can login through the http://127.0.0.1/admin page and operate.
#  Set virtual environment of Python

Because a python project would relay on many libraries which would be modified in some circumstances , so that virtual environment is necessary. (Not only for python. many other programming languages has the same requires too)

The steps below is executed in prompt window. (cmd, powershell, wsl)

1.  install virtualenv

   ``` powershell
   pip install virtualenv
   
   virtualenv # to test if 'virtualenv' is installed
   ```

   Wait until the installation is done.

2. to create a virtual environment .

   1. To make a new folder by using the key word `mkdir env` , and then ` cd ` into this folder.

   2. Then to create the virtual env.

      ``` cmd
      virtualenv --no-site-packages venv  # the parameters "--no-site-packages" means other the third party library won't be duplicated in this virtualenv. That I will have a "pure" environment.
      ```
      ``` cmd
      virtualenv -p d:\d\anaconda3\python.exe .# pass the python in disk d anaconda3 to the new environment. Notice the '.' at the last of the prompt oders. it means the present folder path.
      where python # to find out the path of the python.exe
      ```

   3. To activate the environment. 

      if you are using Linux or MacOS, you can use ` source ` to get in this environment.

      ``` terminal 
      source venv/bin/activate
      ```

      if your are using Windows OS, there will be some difficulties to persecute you. I figured out this problem by reading this article [link](https://www.jianshu.com/p/2cb85ed1446b)

      you should opening the CMD.

      ``` cmd
      cd <venv>/Scripts
      activate.bat
      (trydjango) D:\Dev\trydjango\Scripts>
      ```

   4.  Actually when you get the prompt above , you are succeed. you can create applications(projects) in this environments.

3.  Don't forget to deactivate the environment after. ` deactivate`

   


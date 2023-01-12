# Contributing guide

Welcome to SpaceyaTech Team-Rio Django Community

## Community

The [Discussions](https://github.com/SpaceyaTech/Team-Rio-Django/discussions) is the primary communication forum for Team-Rio Django Community. It is a good place to start whether you have a question, are a new contributor, are a new user, or anything else. Please review our community norms before posting. The Team-Rio Django Community is also governed by a [code of conduct](https://docs.github.com/articles/github-community-guidelines)


## Ways to contribute

- Feel free to check the [issues page](https://github.com/SpaceyaTech/Team-Rio-Django/issues).
- Look up for issues you will like to tackle. You can as well create new issues.
- Comment on the issue you would like to tackle or give more insight or description. For example: ```Hello!, I would like to take up this issue```
- The maintainers will assign you to one of the issues or better yet you can assign yourself to one. 
- You can now get started ! All the best.

## How do I Contribute ?


**1. Fork the repository**
- Fork the [Team-Rio-Django](https://github.com/SpaceyaTech/Team-Rio-Django) by clicking on the fork button on the top of the page.
- This will create a copy of this repository in your account.


**2. Clone the repository**
- Now clone the repo to your machine
- Click on the clone button and then click the copy to clipboard icon.
- Open a terminal( bash on linux/mac, command prompt on windows) and run the following git command: ```git clone "url you just copied" ``` 
- For example : ``git clone https://github.com/yourusername/Team-Rio-Django `` where ```yourusername``` is your Github username

**3. Create a branch**
- Change to the repository directory on your computer (if you are not already there): ```cd django-backend```
- Now create a branch rebasing the pre-dev branch using the ``git checkout`` or ``git branch`` command: 
```bash
git checkout -b <issue-number-title> pre-dev
```
or
```bash
git branch <issue-number-title> pre-dev
git checkout <issue-number-title>
```
- For example: 
```bash
git checkout -b issue-10-create-readme-file pre-dev
```
or 
```bash
git branch issue-10-create-readme-file pre-dev
git checkout issue-10-create-readme-file
```
Read more on [git and GitHub](https://docs.github.com/en/get-started/quickstart/hello-world)
> Note the branch needs to show issue, number and title

**4. Create a Virtual Environment**
> It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is [pipenv](https://pypi.org/project/pipenv/) or venv, which is included in [Python](https://www.python.org/).

With venv, you can create a virtual environment by typing this in the command prompt, remember to navigate to where you want to create your project.

Windows:
```bash
py -m venv myproject
```
Unix/MacOS:
```bash
python -m venv myproject
```

This will setup a virtual environment. Then you have to activate the environment, by typing this command:

Windows:
```bash
myproject\Scripts\activate.bat
```
Unix/MacOS:
```bash
source myproject/bin/activate
```
Once the environment is activated, you will see this result in the command prompt:

Windows:
```bash
(myproject) C:\Users\Your Name>
```
Unix/MacOS:
```bash
(myproject) ... $
```

> ***Note***: You must activate the virtual environment every time you open the command prompt to work on your project.

### Install dependencies
Ensure you have python running on your machine.

```bash
pip install -r requirements.txt
```

### Run
Open the terminal in the main directory and run
```bash
python manage.py runserver
```

## .env
Store sensitive data in the .env file<br>

The .env file will be hidden automatically from the repo because it should contain sensitive information of the project such as the SECRET_KEY.
After cloning the repo go on and follow these steps:
<ul>
 <li>In the root directory of this Project, (<em>Inside the folder named <strong>community</strong></em>), create a file called <strong>.env</strong></li>
 <li>After creating the file, write the following lines:</li>
 
 ```bash
1. SECRET_KEY=your_secret_key
2. DEBUG=True
```
<li>This should do the trick, try running the server to check for any errors after creating your .env file</li>

 ```bash
python manage.py runserver
```
</ul>

> ***Note*** <strong>Generating Your Own SECRET_KEY</strong>
<p>To generate a new key, use the get_random_secret_key() function present in the django.core.management.utils that returns a 50 character string of random characters.
You can open the python shell by typing this command first to execute the get_random_secret_key</p>

 ```bash
python manage.py shell
```
After opening shell, execute the following code to generate your random key

 ```bash
 >>>from django.core.management.utils import get_random_secret_key
 >>>print(get_random_secret_key())
```
<p>Copy the key generated and place it in your SECRET_KEY variable in the .env file. <em><strong>There should be no whitespace around the variable</strong></em></p>

**5. Make necessary changes and commit those changes**
> Make sure to follow steps laid out on the [README](https://github.com/SpaceyaTech/Team-Rio-Django/blob/main/README.md) file to setup the development environment on your machine

> Ensure your commits are alligned with the [Commit Message Template](https://github.com/SpaceyaTech/Team-Rio-Django/wiki/Commit-Messages)
- You can now create/modify files in the code repository in reference to the issue you were assigned.
- Save the file.
- On executing the command ``git status``, you'll see there are changes.
- Add those changes to the branch you just created using the ``git add .`` command:
- ``git add <the file you created or ammended>``
- Now commit those changes using the ``git commit`` command:
- ``git commit -m "a description of the contribution made``


**6. Push changes to GitHub**
- Push your changes using the command ``git push``
```bash
git push origin <issue-number-title>
```
- (replacing < issue-title_number > with the name of the branch you created earlier.)

**7. Submit your changes for review**
- If you go to your repository on GitHub, you’ll see a Compare & pull request button. 
- Click on that button.
- Write a comment on the contributions made making sure to fill the template as provided.
- Link the issue you were working on by making sure the line `Fixes:` has the issue number after it e.g. `Fixes: #10`
- click create pull request button
- Wait for reviews then resolve any issues
- You will get a notification email once the changes have been merged

**You did it!**
- You now have what it takes to my your contributions! Clap for yourself !!👏👏👏

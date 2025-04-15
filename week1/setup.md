
## Clone the Class GitHub
You can access the class GitHub repository directly from your PyCharm.

1. Go to `File` and click on `Project from Version Control...`. 

1. Copy the class GitHub URL `https://github.com/cqx931/techBasics1` and paste it into the input field 

1. Locate the folder where you want to put it. 

1. Click `Clone`

Or you can do it directly from Terminal

`git clone https://github.com/cqx931/techBasics1`

Now you should have access to the class GitHub repository locally.

---

## Terminal

Have you ever seen a hacking scene in a film, where lines of text are streaming in a magic black window? That's where we are going to explore now.

**Terminal** is one of the coolest place to interact with your computer. It is a text-based user interface that allows you to interact with a computer by typing **commands**. 

To not overwhelm you for the first day, we will stay with the very basics.

Open the terminal window from your PyCharm. This would be the same, if you open the terminal window from your system. 


    For Windows users, your default command line would be Windows PowerShell. Please install Git Bash for the class so that we can all share the same syntax.
    If you need help with the installation process, check out this video:
    [Git Bash - Simplest command line program for Windows](https://www.youtube.com/watch?v=yoZ910JQzrg)

Try typing the following command into your terminal:

`python --version`

You shall be able to see something like `Python 3.10.9`, or the version of your default python installed on your laptop. As long as you are using python3, the exact version number doesn't matter at this point.

In case you get `command not found: python`, there might be issues with your Python installation or path configurations on your laptop.

Now let's get to know our computer a bit more inside a terminal.

Depends on where you are accessing this terminal, you might see something like the following

`(.venv) qianxunchen@Mac ~ %`

`(.venv)` means the current environment you are using. Here `.venv` is the default python environment that comes with PyCharm. A python virtual environment is a context in which you run Python code. It is a common and good practice in Python to set up a dedicated environment that is separated from your system. One of the reasons to do so is that if we mess up something, it won't influence the rest of the system. We will learn more about environment later in the class.

Here is a list of basic commands:

`cd` change the directory where you are currently locating in your system.

`cd ~` go to your home directory

`cd Desktop/techBasics1/week1` go to a particular location

`cd ../` go outside the current folder

`ls` list all the files in the current directory.

`ls -l` list all the files with more information.

`ls -A` for hidden files.

`mkdir` make a new directory 

`rmdir` remove a directory, but only if it's empty.

`touch` create a new empty file, inside the current directory.

`rm` remove a file.

`mv` move a file from one location to another location

`cp` create a copy of the file from the first location to the second location

`open` open up a directory in your finder (Not sure if this works with windows git bash)

`open .` open up the current directory


### Exercise 2
Create a folder structure for the class inside your computer with command line ONLY

---

## Git & GitHub

Git is a version control system that tracks changes in files, enabling developers to manage and collaborate on projects effectively. 

While Git is the software that tracks changes, GitHub is an online service that host Git repositories, allowing for easier collaboration and sharing of code. For example, you can still use git to version track your project without uploading it to git.


`git init` If you are starting fresh, you will first need to initialize a directory as a Git repository. Run this command inside the directory you are working on.

`git clone [url]` If you already created a repository on GitHub, or if you want to retrieve a Git repository from someone else.

`git status` show modified files in your working directory

`git add [file]` add a file to your next commit

`git add -A` add all changes to your next commit

`git commit -m "[message]"` commit your staged content

`git log` check your commit history

`git help` check all available commands

`git remote -v` check your current git remote setup

`git remote add [alias] [url]` add a git URL as an alias

`git push` Push the local commit to the remote GitHub repository. By default, it pushes to origin/main

`git pull` fetch and merge commits from remote GitHub repository

`git reset HEAD^` reset the last commit

For more, check out this [cheat sheet for the most commonly used Git commands](https://education.github.com/git-cheat-sheet-education.pdf)

\* To push directly to GitHub from command line, you will need a Personal Access Token. GitHub has disabled you can checkout [the following instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) to generate a personal access token. When the terminal asks you for password, paste this personal access token instead of your GitHub password.

### Exercise 3
- Git control the folder you created
- Make your first commit
- Connect it with your GitHub repository

---
I know this can be a lot of information for the first session, but we will repeat all these together many times in the semester.
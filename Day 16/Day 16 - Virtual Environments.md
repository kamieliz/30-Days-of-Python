# Day 16 - Virtual Environments

# Setting up Virtual Environments

- to start with a project, it would be better to have a virtual envirnonment
- virtual environments can help us create an isolated or separate environment
- helps to avoid conflicts in dependencies across projects
- to see all the packages installed on your computer:
   - `pip freeze`
- to create a virtual environment install the package on your computer
   - `pip install virtualenv`
- to create a virtual environment go to your project folder
   - `virtualenv <project name>`
- the virtual environment will be located in a folder named after project
- to activate the virtual environment
   - `source venv/bin/activate`
- in your virtual environment you will need to install packages that you need
- to return back to your local machine
   - `deactivate`
- if this is in a folder with a git project make sure to include the virtual environment folder in your .gitignore file to not push it to github


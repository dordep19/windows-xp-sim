# windows-xp-sim

Windows XP simulator including Notepad, Snake, Paint, Calculator, and third-party Python script execution. Developed for CMU 15-112 Fall 2018 Final Project.

## Development

```
cd windows-xp-sim
source env/bin/activate
```

This activates the virtual env and dependencies can now be installed local to the repository.

```
pip install -r requirements.txt
```

To run the simulator:

```
python main.py
```

## General Description

The simulation will accept user login, creating accounts for different users and saving their files on the computer running the simulation. Users will be offered access to simulations of notepad, calculator, paint and snake. In addition to this, the simulation is capable of running foreign, user-inserted applications, also opening drawings and texts in simulated paint and notepad.

## Libraries Used

- Tkinter: creation of user interface for os
- PIL: image library used for all image manipulation
- os: managing storage and retrieval of files between actual os and simulated os
- subprocess: generating action sounds
- random: generating random values in various parts of the operating system
- datetime: creating display clock

## UI Description

The user interface for the operating system will be created using the Tkinter library. A login window will be displayed, allowing the user to enter their login details to access a previously created account where they can access their files, or the user could create a new account, generating a username and password which they can use to log back in anytime.

Upon loggin in, the user will be presented with a home screen containing a taskbar from which the main menu can be accessed. The user will be able to navigate between all applications, files and logout from here. All applications will run in new windows, some of their user interfaces being created using the Tkinter library. Programs dropped into user files can be found and run from the search option in the main menu. Previous drawings and texts can be loaded from the same section.

## Demo

Short video demonstrating project features can be found at: https://www.youtube.com/watch?v=odljZPUPumQ&t=4s

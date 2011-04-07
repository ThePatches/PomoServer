=============
PomoServer ReadMe
=============

What is PomoServer
===================
PomoServer is a Pomodoro Technique server program written in python and
intended to replace using an egg time and a paper list by allowing the user
to specify a list of tasks in a data file and then performing the egg timer
functions as a background process.

PomoServer Parts
-----------------
The application consists of two main pieces. ``pom_serv.py`` and ``pom.py``.

The first piece, behaves like a daemon, but still must be run in the background.
It spawns a daemon thread that listens for socket requests that immediately goes
into the background while the program does all its timer waiting and pomodoro
processing in the foreground.

Once the server has started ``pom.py`` can be used to interact with the running
program. While rudimentary, a user can still see the available actions by running
the program with:

``python pom.py -h``

Remember: you will have to manually kill the service or it will run to termination,
You can either do so manually (``kill``) or you can use the ``-k`` option of the ``pom.py``
program (Note: evetually, the ``-k`` option will perform cleanup, so as a habit, it's always better
to use this method to shut down the server).

What Needs to be Done
=======================
PomoServer still needs a fair amount of work. Currently, there are two main lines of development:

1. Convert the ``.py`` code into something more amenable to a background service. While
    `this recipie <http://code.activestate.com/recipes/278731/>` is a place to start, I'd love for
    the application to become compiled code so that there is a named, running service that makes the
    server easy to identify in ``top`` or ``ps``.
2. Enhancements to the Pomodoro task list are more than welcome. It would be great to move tasks
    around the list from the command line or add them on the fly.
3. Make the task files more robust (possibly using `Configparser <http://docs.python.org/library/configparser.html>`).
    all of this work can be done in ``loader.py`` and is therefore really low-impact towards the rest of the project.
4. Notification. As I wrote the initial version for the command line, I am spitting messages out with
    ``print``. A more robust system that works well with window managers will greatly improve the
    application.
    
A Final Note: Data Files
==========================
My initial .gitignore (and all of my subsequent ones) doesn't track ``*.dat`` files which I'm using
to store task lists. Here's the inital file I'm working from::

    # This is a file I am attempting to create some tasks
    #Divider=|
    #Some Tasks
    task=Finances|Enter Stuff into Quicken|recur|inf
    task=Pomo Task Files|Update the task files for pomodoro|recur|3
    task=Empty Dishwasher|Speaks for Itself|once

All the lines marked with ``#`` are ignored (yay comments!), but tasks must be structured that way.
The general format is::
    
    task=[Task Name]|[Task Comment/Description]|[recur/once]|[inf/Times Recurring]

If the task is recuring you must indicate it with the '``recur``' keyword AND you **must** provide
a number of times for the task.
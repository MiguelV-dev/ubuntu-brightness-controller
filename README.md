ubuntu-brightness-controller - v1.0.0
=====================================


An Application Indicator allowing the user to change the brightness of the screen.

Working and tested with Unity on Ubuntu 16.04 LTS x64 with Nvidia proprietary drivers for GTX 960 4GB with only one monitor activated, but should work with any other desktop environments that support AppIndicators.

Feel free to notify me if you got it working in any other testing conditions

----------

 
Features
----------------

 - Detects automatically all monitor screens connected, adjusting the brightness level on all of them
 - 10 levels of brightness available (could be easily customized)
 - bash script (startBC.sh) so you can add this file to Startup Applications on Ubuntu


Run Instructions
----------------
Open a terminal and run the following command:

    python brightness.py

Python 2.7.12 was used in development, if not working in another version please let me know.


Screenshot
----------------

![Screenshot of ubuntu-brightness-controller](/screenshot.png?raw=true)


Future Work
----------------

 - Add a makefile, allowing the user to install and uninstall easily


Changelog:
----------------

 - v1.0.0 uploaded to a repository on github

Original Author: Miguel Ventura - https://github.com/skamv

----------


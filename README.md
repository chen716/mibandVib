
![Requirements](https://img.shields.io/badge/Python-3.6-lightgrey)
![Commit](https://img.shields.io/github/last-commit/satcar77/miband4) 
![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)

# MIBAND 4 - Python Library

> Library to interact with Xiaomi MiBand4. 
> Only works on linux.


# Setup 

- Clone this repo to your local machine



1.  Install the dependencies. Libglib2 is required for bluepy. 

    ```
    sudo apt-get install libglib2.0-dev
    pip3 install -r requirements.txt
    ```

2.  Run the miband4_console

    ```
    python3 miband4_console.py -m "CD:A7:34:6F:3C:AE"

	```
    In here you will see two functions, "display vibration at trigger" or "display vibration at trigger". Use this to start on-trigger vibration based on whether you want trigger based(explicit) or offset based(implicit). 


3. Import client.py in the file you wish to use the functions


4. Call vib_once() to vibrate the board once (minimum 1sec between each vibration) 
Note: This requires you to start the "display vibration at trigger" before you run this command.


5. Call vib_update_freq( delay ) where delay is an int to update the offset between each vibration.
Note: This requires you to start the "display vibration at trigger" before you run this command.




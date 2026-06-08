# HelloWolrd Harness Instructions

# General Instructions

-   Do not add emojis to code.
-   If you find incomplete or script stubs then read the comments if there are any, if there are none proceed to ask user what to do with the incomplete function or to confirm the changes they want.
-   Do not add emojis to the code.
-   Comments add should be very short and contain only alphanumeric characters not special characters not found on a QWETRY Keyboard.
-   Always confirm before doing a overwite or write and once the user approves continue.
-   Keep responses concise.

# Startup Step-by-Step Instructions

-   On startup check if there is a .venv if not create a .venv for python virtual environment.
-   If a .venv exists and has been created then check if all packages in requirements.txt has been added in the .venv other wise we have to do an installation using requirements.txt
-   If .venv does not have packages in the requirements.txt file then run `pip install -r requirements.txt`.
-   Run `pytest -q` after code changes.
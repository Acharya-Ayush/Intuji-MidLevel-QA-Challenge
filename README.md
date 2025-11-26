# Intuji-MidLevel-QA-Challenge
This is challenge for Automation Interview.

Before running the project make sure that all the requirements are met. 

1. Python Version: Python 3.12.2
2. Make virtual environment using command: py -m venv venv
3. Activate the environment: "NOTE: venv folder name".\Scripts\activate 
4. Install pip: py get-pip.py
5. Intialize all the requirements using requirements.txt file.
6. Add a .env file in root dir and write the credentials there so that credentials are hidden from other.

You are ready to run the tests ;D

Before Execution What to do?
- It is always crutual to keep .env file ignored but for ease I am keeping the file in the ROOT REPO
- Signup is done only one time so make sure you change the credentials from .env file everytime before you run the signup test case. 

Before running script make sure that you are in the tests directory. Pytest uses scripting technique on how to run the Object some of the examples are: 
1. What if we want to run the test end to end: pytest -s "file name" (NOTE: This will make sure to run the tests one by one. The tests will be run in ascending order on how the function is defined.)
2. What if we want to run the test parallelly: pytest -n 2 -m parallel -s (NOTE: This will make sure to run the suits which is marked as parallel in the fixture)
3. What if we only want to run one test case in the class: pytest -s "file name"::"class name"::"function name" (NOTE: This will make sure to run only one test suit)
4. What if we wanna run selective parallel suits regardless the marker: pytest -n 2 -m parallel -k "function_name_first or function_name_second or function_name_third" -s (NOTE: multiple function name saperated by or)

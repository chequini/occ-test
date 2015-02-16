# Basic robot simulation

### 1. Description

The present project is a private test for an evaluation process, the system simulates a robot in a table, the robot receive a file with a set of instruction commands, the robot would be able to process the commands in order to reach a new position in the table.

### 2. Running the test

System requirements:

 * Python 2.7
 * Standard OS python library (if not exists)
 * Standard Sys python library
 * re python library

The project was tested over **Ubuntu 14.04**.

Execute the next command in the terminal to run all test cases:

```bash
~$ python run-tests.py
```

The test cases set includes examples of use and some validation tests, the cases are the following:

 * Generic test 1 (Example 1)
 * Generic test 2 (Example 2)
 * Generic test 3 (Example 3)
 * The robot is not placed
 * Invalid command in file
 * Invalid number of paramenters in PLACE command
 * Invalid place inputs
 * Invalid new position after PLACE or MOVE
 * Multiple PLACE command and movements

The *run-tests.py* script performs multiple calls to  *robot.py* script passing the commands file path, if you want to run an specific set of instruction in a file execute the following command in a terminal:


```bash
~$ python robot.py [FilePath]
```

### 3. Tunning the system

Please, feel totally free to change the following parameters in *robot.py*:

* tableDimen = { "w":Width, "h":Height } - The table size in a grid system (Line:38)
* Debug level - Choose debug level, from 0-no show to 3-show all (Line:167)

### 4. About

Developed by Sergio Roman Iturbe

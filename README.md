# Python Script to Analyse the logfile
## (Python Script -  How many times the status has occurred in accordance with day from access log)


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Description

Here is a python script that will analyze and sort the access logs. Its been a common scenario in recent days to sort and fetch the details as per the requirements from the access logs. As I have been requested to sort the logs based on the status and its count which refers to how many times the status has occurred. Also, these details will be displed in accordance with each day. 

## Features

- Log Analyser and easy to manage
- Simple syntax and Python code is easy to understand.

## Modules Used

- logparser

## Pre-Requests

- Basic Knowledge of python
- Need to install python3.


## Behind the code

> $ cat logparser.py (it's used for log parsing and it's a outsource script)

```sh
#!/usr/bin/env  python3
import re
regex_host = r'(?P<host>.*?)'
regex_identity = r'(?P<identity>\S+)'
regex_user = r'(?P<user>\S+)'
regex_time = r'\[(?P<time>.*?)\]'
regex_request = r'\"(?P<request>.*?)\"'
regex_status = r'(?P<status>\d{3})'
regex_size = r'(?P<size>\S+)'
regex_referer = r'\"(?P<referer>.*?)\"'
regex_agent = r'\"(?P<agent>.*?)\"'
regex_space = r'\s'

pattern = regex_host + regex_space + regex_identity + regex_space + \
          regex_user + regex_space + regex_time + regex_space + \
                  regex_request + regex_space + regex_status + regex_space + \
                  regex_size + regex_space + regex_referer + regex_space + \
                  regex_agent


def parser(s):
        """
        return type : dict()
        return format: {
                       host:str , identity:str , user:str ,
                                           time:str ,request:str , status:str ,
                                           size:str , referer:str, agent:str
                                        }
        returns None if failed.
        """
        try:
                parts = re.match(pattern,s)
                return parts.groupdict()
        except Exception as err:
                print(err)
```

> $ cat loganalyser.py

```sh
import logparser

logfile = open("access.log","r")

day = {}

for line in logfile:
    
  logParts = logparser.parser(line)

  status = logParts["status"]
    
  time = logParts["time"].split(":")[0]
  
  if time not in day:
    
    day[time] = {}
    
    if status not in day[time]:
      
      day[time][status] = 1
    else:
        
      day[time][status] = day[time][status] + 1
    
  else:
    if status not in day[time]:
        
      day[time][status] = 1
    
    else:
      day[time][status] = day[time][status] + 1
    
for item in day:
  
  print("The date in which below details are of :-",item)
  print()
  print(day[item], "\n")
        
```

## User Instructions

```sh
sudo yum install git -y
sudo yum install python3
git clone https://github.com/ajish-antony/python-log-analyser.git
cd python-log-analyser
```

> A sample access log file has been provided here. Update the required access log in the log file. Further, execute the script

```sh
python3 loganalyser.py
```

## Script running Demonstration

```sh
$ python3 loganalyser.py
The date in which below details are of :- 19/Dec/2020

{'404': 50, '200': 1027, '303': 56}

The date in which below details are of :- 20/Dec/2020

{'200': 3472, '303': 170, '404': 55, '301': 1}

The date in which below details are of :- 21/Dec/2020

{'200': 3749, '303': 170, '404': 60, '301': 3}

The date in which below details are of :- 22/Dec/2020

{'200': 3357, '303': 162, '301': 1, '404': 125}

The date in which below details are of :- 23/Dec/2020

{'200': 3550, '303': 134, '404': 138, '206': 34}

The date in which below details are of :- 24/Dec/2020

{'200': 3365, '303': 181, '404': 59, '206': 1, '301': 1}

The date in which below details are of :- 25/Dec/2020

{'200': 5317, '404': 81, '303': 246}

The date in which below details are of :- 26/Dec/2020

{'200': 2177, '404': 64, '303': 28}
```

## Conclusion

Here is a python script helpful for those who are stepping into the python scripting world and at the same time can be made use for analyzing the logs as per the requirements.


### ⚙️ Connect with Me

<p align="center">
<a href="mailto:ajishantony95@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/ajish-antony/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

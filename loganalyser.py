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

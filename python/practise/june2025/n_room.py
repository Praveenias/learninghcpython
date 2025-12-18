def maximumMeetings(start,end):
  temp = zip(end,start)
  temp = sorted(temp)
  max_hrs = 0
  tempendtime = 0
  for endtime,startime in temp:
    if tempendtime < startime:
      max_hrs +=1
      tempendtime = endtime
    print(startime,endtime,tempendtime)
  print(max_hrs)


maximumMeetings([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9])
maximumMeetings([10, 12, 20],[20, 25, 30])
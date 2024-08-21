import datetime
import calendar

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][datetime.datetime.strptime(str(day)+" "+str(month)+" "+str(year), '%d %m %Y').weekday()]
    
print(Solution().dayOfTheWeek(5,3,2011))
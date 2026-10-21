
# match expression → evaluated once.
# case → defines patterns to match.
# _ → wildcard (default case).

def cheak_odd_and_even(num):
    match num % 2:
        case 0 :
            return "even"
        case 1 : 
            return "odd"
       
even_odd = cheak_odd_and_even(8)
print(even_odd)          
even_odd = cheak_odd_and_even(15)
print(even_odd) 



# 1. Write a function using match that classifies marks into Distinction, First Class, Second Class, Third Class, or Fail. Note: You can enter/get the marks from user (input).
marks = int(input("enter your maks"))
def students_marks (marks):
    match marks :
        case m if m >= 75:
            return "distinction"
        case m if m >= 65:
            return "first class"
        case m if m >= 50:
            return "secomd class"
        case m if m >= 33:
            return "third class"
        case _:
            return "fail"
        

print(students_marks(marks))
        
        
# 2. Use match to print whether a given day number (1–7) is a weekday or weekend. Default is “Invalid day”     
def weekday_name (day_number):
    match day_number:
        case 1 | 2 | 3 | 4 | 5:
            return "weekday"
        case 6 | 7:
            return "weekend"
        
print(weekday_name (7))        


# 3. Implement a traffic light system using match. Hint: Valid traffic colors – Red, Yellow, Green. Any other color is “Invalid Color”.*args
def traffic_light(light):
    match light:
        case "Red" | "Yellow" | "Green":
            return "True colors"
        case _:
            return "Invalid Color"


print(traffic_light("Red"))

def year_month(month):
    match month:
        case "maech" | "april" :
            return "spring"
        case "junr" | "july" | "august":
            return "summer"
        case  "september" | "octuber" | "november":
            return "autume"
        case "december" | "febeuary" | "january":
            return "winter"
        
        
print(year_month("december"))    
    
import math
# correlation coffecient / 
# x = Co and y = O3 / 
# sum_multiply is ths sum of x*y 
# sum_x and sum_y are the sum of all x's and y's
# n is the total number of values in the file
# sum_x2 and sum_y2 are the sum of the x and y up to 2
# Nominator_float = (n * sum_multiply)- (sum_x - sum_y)
#Denominator_float = math.sqrt((n * sum_x2 - sum_x**2)) * math.sqrt((n * sum_y2 - sum_y**2))

Nominator_float = 0 
Denominator_float = 0
n=0
sum_multiply = 0
sum_x = 0
sum_y = 0
sum_x2 =0
sum_y2 =0
m=0
with open("airpolution.txt")as file : 
    
    for line in file:
        data = line.strip().split("\t")
        if len(data) == 6 and data[0]!="City":
            City, Month , Year, co, o3, temperature = data
            co_float = float(co)
            temperature_float = float(temperature)
            n +=1
            sum_x += co_float
            sum_y += temperature_float
            sum_multiply += co_float*temperature_float
            sum_x2 += co_float*co_float
            sum_y2 += temperature_float*temperature_float

Nominator_float = (n * sum_multiply)- (sum_x*sum_y)
Denominator_float = math.sqrt((n * sum_x2 - sum_x**2)) * math.sqrt((n * sum_y2 - sum_y**2))

Corrrelation_coef = Nominator_float/Denominator_float

print(Corrrelation_coef)








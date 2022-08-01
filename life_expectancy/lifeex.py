from statistics import mean
 
max_life = -1
min_life = 9999
avg_life = 9999
yoi_life_ex = []
yoi_countries = [] 
yoi_max_life = -1
yoi_min_life = 9999

yoi = input("Enter the year of interest: ")
 
with open("life-expectancy.csv") as f:
    next(f)
 
    for line in f:
        columns = line.split(",")
        countries = columns [0]
        code = columns [1]
        year = columns[2]
        life_ex = float(columns[3])
       
        if float(life_ex) > max_life:
            max_life = float(life_ex)
            max_country = countries
 
        if float(life_ex) < min_life:
            min_life = float(life_ex)
            min_country = countries
 
        if yoi in year:

            yoi_life_ex.append(float(life_ex))
            yoi_countries.append(countries)
            yoi_ex_avg = mean(yoi_life_ex)

            if float(max(yoi_life_ex)) > yoi_max_life:
                yoi_max_life = max(yoi_life_ex)
                yoi_max_country = countries
 
            if float(min(yoi_life_ex)) < yoi_min_life:
                yoi_min_life = min(yoi_life_ex)
                yoi_min_country = countries
 
print (f"The overall min life expectancy is {min_life} years in {min_country}."   )
print (f"The overall max life expectancy is {max_life} years in {max_country}. \n")
 
print (f"For the year {yoi}: ")
print (f"The average life expectancy across all countries was {round(yoi_ex_avg, 2)}.")
print (f"The maximum life expectancy was in {yoi_max_country} with {yoi_max_life}.")
print (f"The min life expectancy was in {yoi_min_country} with {yoi_min_life}. \n")

class Person:
  def __init__(self, born, death):
    self.born = born
    self.death = death
   
class Year:
  def __init__(self, date, population):
    self.date = date
    self.population = population

def populationCount(person, year):
    if person.born <= year.date and person.death >= year.date:
        year.population += 1

       
personObjects = []
personObjects.append(Person(1920,1993))
personObjects.append(Person(1922,1991))
personObjects.append(Person(1926,1998))
personObjects.append(Person(1923,1994))
personObjects.append(Person(2000,2026))
personObjects.append(Person(1956,2029))
personObjects.append(Person(2003,2040))
personObjects.append(Person(2002,2090))
personObjects.append(Person(1920,1991))


minimumAge = min(personObjects, key = lambda x: x.born).born
maxAge = max(personObjects, key = lambda x: x.death).death +1

yearObjects = []

for i in range (minimumAge, maxAge):
    yearObjects.append(Year(i,0))

for j in yearObjects:
    for i in personObjects:
        populationCount(i, j)
    print("year count for year: "+ str(j.date) + " and the count is: " + str(j.population))
class DVD:
	def __init__(self,name,release_year, director):
		self.name = name
		self.release_year = release_year
		self.director = director
	def __str__(self):
		return f"{self.name}, directed by {self.director}, release in {self.release_year}"
dvd_collection = [None] * 15

avengers_dvd = DVD("The Avengers",2012,"Anh em nhà Russo")
dvd_collection[0] = avengers_dvd
a = DVD("The Incredible", 2004, "Brad Bird")
b = DVD("Finding Dory", 2016, "Andrew Stanton")
c = DVD("The Lion King", 2019, "Jon Favreau")
dvd_collection[1] = a
dvd_collection[2] = b
dvd_collection[10] = c
for a in dvd_collection:
    if a is not None:
        print(a)
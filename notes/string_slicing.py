name = "Eric Ncube"
#first_name = name[0:4] #cuts from index 0 to ending index exclusive
#funky_name = name[1:10:2] #cuts from index 1 to index 10 skipping every second char
#reversed_name = name[::-1] #cuts from beginning to end iterating over the name backwards

#print("First name: "+first_name)
#print("Funky name: "+funky_name)
#print("Reversed name: "+reversed_name)

website = "https://google.com"
slice = slice(8, -4) #slice object slices from index 8 to 4 places before the end
print(website[slice])
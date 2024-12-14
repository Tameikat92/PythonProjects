meekInfo = dict()

meekInfo['spirit number'] = 7
meekInfo['spirit animal'] = 'cat'

#item returns a list of (key, value) tuples
for (number,animal) in meekInfo.items():
    print(number,animal)

tuplesMeek = meekInfo.items()
print(tuplesMeek)

#Sorting List of Tuples
faveAlbums = {
    'Voyage To India': 1,
    'B-day': 2,
    'Confessions': 3
}
# return key,vales
print(faveAlbums.items())

#sort faveAlbums in order alphebetically 
print(sorted(faveAlbums.items()))

#print the sorted(in order by alphebet) list of fave albums. In key prder
for albumName, albumRank in sorted(faveAlbums.items()):
    print(albumName,albumRank)

    # sort by value instead of key
faveRapperAge = {
    'Ice Cube': 50,
    'Nas': 44,
    'Tupac': 49
}
temp = list()

#for loop that creates a list of tuples
for k,v in faveRapperAge.items():
    temp.append( (v,k) )
print(temp) #make sure indent so print can be outside of the loop

#reverse equals true means sort from high to low 
#overwriting temp essentially
temp = sorted(temp, reverse=True) 
print(temp)

#Shorter version of the sorted function
c = {
    'a': 10,
    'b': 1,
    'c': 22
}
print(sorted( [ (v,k) for k,v in c.items() ] ))

x,y = 3,4
print(y)
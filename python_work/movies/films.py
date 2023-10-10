from json import load
path="C:\\Users\\hp\\Desktop\\python_works\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    movies=load(f)
    print(len(movies))
movie_names=[m.get("title") for m in movies]
#print(movie_names)
#movie released in 2005
movie_in2005=[m.get("title") for m in movies if m.get("year")=="2005"]
#print(movie_in2005)
#movie title genre = comedy
fun_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
#print(fun_movies)
#lengthy movie title
lengthy_movie=max(movies,key=lambda m:int(m.get("runtime")))
#print(lengthy_movie)
#all genres
genres={g for m in movies for g in m.get("genres")}
#print(genres)
#comedy movies released in 2015
print("Comedy movies in 2015")
fun_movie_in2005=[m.get("title") for m in movies if m.get("year")=="2015" and "Comedy" in m.get("genres")]
print(fun_movie_in2005)
wc={}
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
#print(wc) 
mov=max(wc)
print(mov)
movies = [
    # Malayalam
    {"title": "Drishyam", "director": "Jeethu Joseph", "language": "Malayalam", "year": 2013, "genre": "Thriller"},
    {"title": "Bangalore Days", "director": "Anjali Menon", "language": "Malayalam", "year": 2014, "genre": "Drama"},
    {"title": "Premam", "director": "Alphonse Puthren", "language": "Malayalam", "year": 2015, "genre": "Romance"},
    {"title": "Kumbalangi Nights", "director": "Madhu C. Narayanan", "language": "Malayalam", "year": 2019, "genre": "Family"},

    # Tamil
    {"title": "Soorarai Pottru", "director": "Sudha Kongara", "language": "Tamil", "year": 2020, "genre": "Drama"},
    {"title": "Vikram Vedha", "director": "Pushkar-Gayathri", "language": "Tamil", "year": 2017, "genre": "Crime"},
    {"title": "Master", "director": "Lokesh Kanagaraj", "language": "Tamil", "year": 2021, "genre": "Action"},
    {"title": "Kaithi", "director": "Lokesh Kanagaraj", "language": "Tamil", "year": 2019, "genre": "Action"},

    # Telugu
    {"title": "Magadheera", "director": "S. S. Rajamouli", "language": "Telugu", "year": 2009, "genre": "Fantasy"},
    {"title": "Arjun Reddy", "director": "Sandeep Reddy Vanga", "language": "Telugu", "year": 2017, "genre": "Romance"},
    {"title": "Eega", "director": "S. S. Rajamouli", "language": "Telugu", "year": 2012, "genre": "Fantasy"},
    {"title": "Pushpa: The Rise", "director": "Sukumar", "language": "Telugu", "year": 2021, "genre": "Action"},

    # Hindi
    {"title": "3 Idiots", "director": "Rajkumar Hirani", "language": "Hindi", "year": 2009, "genre": "Comedy"},
    {"title": "Dangal", "director": "Nitesh Tiwari", "language": "Hindi", "year": 2016, "genre": "Sports"},
    {"title": "Gully Boy", "director": "Zoya Akhtar", "language": "Hindi", "year": 2019, "genre": "Musical"},
    {"title": "Chak De! India", "director": "Shimit Amin", "language": "Hindi", "year": 2007, "genre": "Sports"}
]

# {"title","director","language","year","genre"}

# print all movie_names
all_movie_names= [m.get("title") for m in movies]

print(all_movie_names)

# display all malayalam_movie_names
malayalam_movies=[m.get("title") for m in movies if m.get("language")=="Malayalam"]

print(malayalam_movies)

all_years=[m.get("year") for m in movies]

year_count = {y:all_years.count(y) for y in all_years}

max_movies= max(year_count,key=year_count.get)

print(max_movies)




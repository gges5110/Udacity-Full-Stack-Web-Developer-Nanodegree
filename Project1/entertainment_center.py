from media import Movie

def entertainment_center():
    movie_list = []
    movie1 = Movie("Captain America: Civil War", \
        "https://www.youtube.com/watch?v=QGfhS1hfTWw", \
        "http://t2.gstatic.com/images?q=tbn:ANd9GcQJHE0wTHT_pNRdZlnJj5IkzF49uMF3be1gfIIKw8A8z_3oHVRO", \
        "QGfhS1hfTWw")
    movie_list.append(movie1)

    movie2 = Movie("Neighbors 2: Sorority Rising", \
        "https://www.youtube.com/watch?v=h1pA4Oio6T8", \
        "http://t2.gstatic.com/images?q=tbn:ANd9GcST6cuzBZolESt6KVcg1aUzcFAOZU9CF4YA3OCZfHsdxeSQtbH9", \
        "h1pA4Oio6T8")

    movie_list.append(movie2)

    movie3 = Movie("That Awkward Moment", \
        "https://www.youtube.com/watch?v=wRcVgJjnFLo", \
        "http://t1.gstatic.com/images?q=tbn:ANd9GcTrFSWtS5G_u88IutD_Flen9789bPanDxf1JqUNvpxFJk5cVPyL", \
        "wRcVgJjnFLo")
    movie_list.append(movie3)

    return movie_list

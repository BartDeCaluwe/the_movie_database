import http.client
import json
from pprint import pprint as pp

class MovieDatabase:
    api_key = '382c9e3b88979c6228867c831f59e5c0'

    def getMovieById(self, movie_id):
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        url = "/3/movie/{}?language=en-US&api_key={}".format(movie_id, self.api_key)
        conn.request("GET", url)
        res = conn.getresponse()
        stringData = res.read().decode("utf-8")
        jsonData = json.loads(stringData)
        return jsonData["release_date"]

    def searchMovie(self, query):
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        url = "/3/search/movie?query={}&include_adult=false&page=1&language=en-US&api_key={}".format(query, self.api_key)
        conn.request("GET", url)
        res = conn.getresponse()
        stringData = res.read().decode("utf-8")
        jsonData = json.loads(stringData)
        return jsonData


class Program():
    def run(self):
        db = MovieDatabase()
        movie_id = 0
        while True:
            while True:
                try:
                    choice = int(input("Please choose which action you want to do\n" +
                                       "-------------------------------\n" +
                                       "1. Check if a movie is released\n" +
                                       "2. Search a movie\n" +
                                       "0. Exit the application\n" +
                                       "-------------------------------\n" +
                                       "Input: "))
                except ValueError:
                    print("Please enter a number!")
                    continue
                else:
                    break
            if choice == 0:
                exit()
            if choice == 1:
                while True:
                    try:
                        movie_id = int(input("Please give a movie id: "))
                    except ValueError:
                        print("Input given was not a number!")
                        continue
                    else:
                        break
                pp(db.getMovieById(movie_id))
            elif choice == 2:
                query = input("Please enter a search string: ")
                results = db.searchMovie(query)["results"]
                if results:
                    counter = 1
                    for item in results:
                        pp(str(counter) + ". " + item["title"])
                        counter += 1
                    print("-------------------------------\n" +
                          "0. Go back to main menu")
                    while True:
                        choice = int(input("Which movie would you like to know the release date of?\n"))
                        if choice == 0:
                            break
                        release_date = db.getMovieById(choice)
                        if release_date:
                            pp("release date: " +  release_date)


program = Program()
program.run()

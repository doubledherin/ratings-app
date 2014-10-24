from datetime import datetime
import model
import csv

def load_users(session):
    # use u.user
    with open("seed_data/u.user") as fin:
        user_reader = csv.reader(fin, delimiter="|")
        for row in user_reader:
            user = model.User()
            user.id = row[0]
            user.age = row[1]
            user.occupation = row[3]
            user.zipcode= row[4]
            session.add(user)
    session.commit()


# for line in file:
#     row = line.split()
#     user = model.User()
#     user.id = row[0]
#     user.age = row[1]
#     user.occupation = row[3]
#     user.zipcode= row[4]
#     session.add(user)



def load_movies(session):
    # use u.item
    with open("seed_data/u.item") as fin:
        movie_reader = csv.reader(fin, delimiter="|")
        for row in movie_reader:
            movie = model.Movie()


            # get release date as string
            release_date = row[2]

            if len(release_date) < 3:
                # print "We have a problem. Date not long enough."
                continue
            # convert the string to a datetime object
            # release_datetime = datetime.strptime(release_date, "%d-%b-%Y")
            release_datetime = datetime.strptime(release_date, "%d-%b-%Y")
            # YMD_release_datetime = 
            print release_datetime


            movie.id = row[0]
            movie.title = row[1]
            movie.release_date = release_date
            movie.url = row[3]
            session.add(movie)
    # session.commit()

def load_ratings(session):
    # use u.data
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    #load_users(session)
    load_movies(session)

if __name__ == "__main__":
    s = model.connect()
    main(s)


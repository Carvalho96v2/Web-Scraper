def get_pistols():
    with open('pistols.txt', 'r') as pistols:
        data = pistols.readlines()[0].split(',')
    return data

def get_movies():
    data = []
    split_string = "\\', \\'"
    try:
        movies = open('formatted_movies.txt', 'r')
    except:
        create_movies_file()
        movies = open('formatted_movies.txt', 'r')
    finally:
        for line in movies.readlines():
            line = line.strip('[').strip(']').strip("'")
            for link in line.split('\', \''):         
                link.strip("'")       
                data.append(link)   
        return data

def get_tv_shows():
    data = []
    split_string = "\\', \\'"
    try:
        tv_shows = open('formatted_tv_shows.txt', 'r')
    except:
        create_tv_file()
        tv_shows = open('formatted_tv_shows.txt', 'r')
    finally:
        for line in tv_shows.readlines():
            line = line.strip('[').strip(']').strip("'")
            for link in line.split('\', \''):         
                link.strip("'")       
                data.append(link)   
        return data

def create_movies_file():
    data = []
    with open('all_movies.csv', 'r') as movies:
        for line in movies.readlines():
            line = line.strip('"')
            for link in line.split(',/'):                
                data.append('http://www.imfdb.org/' + link)   
    with open("formatted_movies.txt", "w+") as formatted_movies:  
        formatted_movies.write(str(data).strip("['/links\\n', ").strip(", '/wiki/Zulu_Dawn\"\\n']"))
    

def update_movies(remaining_movies):
    with open('formatted_movies.txt', 'w+') as file:
        file.write(str(remaining_movies))

def update_tv_shows(remaining_tv_show):
    with open('formatted_tv_shows.txt', 'w+') as file:
        file.write(str(remaining_tv_show))

def create_tv_file():
    data = []
    try:
        with open('tv.csv', 'r') as tv_shows:
            for line in tv_shows.readlines():
                line = line.strip('"')
                for link in line.split(',/'):                
                    data.append('http://www.imfdb.org/' + link)   
        try:
            with open("formatted_tv_shows.txt", "w+") as formatted_movies:  
                formatted_movies.write(str(data).strip("['/links\\n', ").strip(", '/wiki/Zulu_Dawn\"\\n']"))
        except:
            print("Clearly I have no idea what Im doing.")
    except:
        print('TV csv file has not been created yet')


create_tv_file()
print(get_tv_shows())
print(len(get_tv_shows()))
    

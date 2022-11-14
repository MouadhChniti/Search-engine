from posixpath import split
if __name__ == "__main__":
    movies_list=["avengers endgame press","endgame infinity war","the space between us"]
    books_list=["b1 book","b2 book","b3 press","book"]
    newspaper_list=["lapresse press","blablaa","khraaa press","dkglsn"]
    tous_list=movies_list+books_list+newspaper_list
    domaine = input("enter le genre de recherche:")
    user = input("enter movie name:")
    search_list = []
    index = 0

    split_user = user.split(" ")
    if domaine.upper() == "MOVIES":


        for movies in movies_list:
            index += 1
            split_moviesList = movies.split(" ")
            for keyword1 in split_user:
                for keyword2 in split_moviesList:
                    if keyword1.lower() == keyword2.lower():
                        search_list.append(index)
        print(len(search_list),"results found \n")
        for index in search_list:
            print(movies_list[index-1]+"\n")


    if domaine.upper() == "BOOKS":


        for books in books_list:
            index += 1
            split_booksList = books.split(" ")
            for keyword1 in split_user:
                for keyword2 in split_booksList:
                    if keyword1.lower() == keyword2.lower():
                        search_list.append(index)
        print(len(search_list),"results found \n")
        for index in search_list:
            print(books_list[index-1]+"\n")        


if domaine.upper() == "NEWSPAPER":


        for newspaper in newspaper_list:
            index += 1
            split_newspaperList = newspaper.split(" ")
            for keyword1 in split_user:
                for keyword2 in split_newspaperList:
                    if keyword1.lower() == keyword2.lower():
                        search_list.append(index)
        print(len(search_list),"results found \n")
        for index in search_list:
            print(newspaper_list[index-1]+"\n")


if domaine.upper() == "TOUS":


        for tous in tous_list:
            index += 1
            split_tousList = tous.split(" ")
            for keyword1 in split_user:
                for keyword2 in split_tousList:
                    if keyword1.lower() == keyword2.lower():
                        search_list.append(index)
        print(len(search_list),"results found \n")
        for index in search_list:
            print(tous_list[index-1]+"\n")



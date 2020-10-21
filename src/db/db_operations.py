from db.db_connection import collection


def get_all_movies():
    res_arr = []
    for x in collection.find({}).:
        res_arr.append(x)
        print(x)
    
    return res_arr

import pickle
import json
new = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

new_json = new.to_json(orient='records')
similarity_json = json.dumps(similarity.tolist())

with open('movies_list.json', 'w') as f:
    f.write(new_json)

with open('similarity.json', 'w') as f:
    f.write(similarity_json)

def recommend(movie):
    sortedMovies = []
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        sortedMovies.append(new.iloc[i[0]].title)
    return sortedMovies
        
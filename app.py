from flask import Flask,request,jsonify,render_template
import pandas as pd
import scipy.sparse as sp
import json
import difflib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def define_data():
    movies_data = pd.read_csv("C:\\Users\\admin\\Desktop\\movies.csv")
    movies_data.head()
    return movies_data

# combine all selected features
def combined_data(movies_data):
    select_feature = ['genres','keywords','tagline','cast','director']
    for i in select_feature:
        movies_data[i] = movies_data[i].fillna('')
    combine_fea = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
    return combine_fea

def transform(combine_fea):
    vectorizer = TfidfVectorizer() #TfidfVectorizer is used for converting text to numercical data(feature data)
    feature_vector = vectorizer.fit_transform(combine_fea)
    similar = cosine_similarity(feature_vector) # cosine_similarity is used for finding similar one (with 0 is mist similar)
    return similar


# list of all movies which is similar to user input
def recommed_movie(user):
    movies_data = define_data()
    combine_fea = combined_data(movies_data)
    similar = transform(combine_fea)

    list_movies = movies_data['title'].tolist()
    
    find_close_list = difflib.get_close_matches(user,list_movies)
    
    close_match = find_close_list[0]
    
    index_of_movie = movies_data[movies_data.title==close_match]['index'].values[0]

    similar_score = list(enumerate(similar[index_of_movie])) 
    
    sorted_score = sorted(similar_score,key=lambda x:x[1], reverse=True)

    lt = []
    var=0
    for i in sorted_score:
        lt.append(movies_data[movies_data.index==i[0]]['title'].values[0])
        var=var+1
        if var==10:
            break

    return lt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def recommed():
	m = request.form.get("mname")
	res = recommed_movie(m)
	d = dict({int(i+1):res[i] for i in range(10)})
	json_object = json.dumps(d, indent = 4, separators=(',', ': ')) 
	return render_template('result.html',number=json_object)
	

if __name__=='__main__':
    app.run(port = 5000, debug = True)

#res=recommed_movie(mname)
    	#d=dict({i+1:res[i] for i in range(10)})
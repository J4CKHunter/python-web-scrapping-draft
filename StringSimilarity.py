import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

sentences ={
    'This is a foo bar sentence.',
    'This sentence is similar to a foo bar sentence.',
    'This is another string, but it is not quite similar to the previous ones.',
    'I am also just another string.'
}

def clean_string(text):
    text = ''.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords])

    return text

cleaned = list(map(clean_string, sentences))

print(cleaned)

vectorizer = CountVectorizer().fit_transform(cleaned)
vectors = vectorizer.toarray()

print(vectors)


csim = cosine_similarity(vectors)
print(csim)

def cosine_sim_vectors(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)

    return cosine_similarity(vec1, vec2)[0][0]

print (cosine_sim_vectors(vectors[1], vectors[0]))

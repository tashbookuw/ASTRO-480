#Noah Tashbook, based on the skeleton code

# This is pretty much the same as the language classifying code but this one will distinguish between Pokemon and animals (maybe)

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics

#


languages_data_folder = sys.argv[1] #this line is the cause of 90% of my stress in this class today
dataset = load_files(languages_data_folder)

docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.5)

vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char', use_idf=False)
# this is the thing that gets rid of small, common words because they're not super duper useful

clf = Pipeline([ ('vec', vectorizer), ('clf', Perceptron(tol=1e-3)), ]) #This is equivalent to one millitolerance

clf.fit(docs_train, y_train)

y_predicted = clf.predict(docs_test)

print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))
#this is the confusing confusion matrix

centimeter = metrics.confusion_matrix(y_test, y_predicted)

print(centimeter)


sentences = [
    u'Pikachu squirtle togepi',
    u'Rabbit horse dog',
    u'Zebra puppy cow',
	u'charizard bulbasaur',
]

predicted = clf.predict(sentences)

for s, p in zip(sentences, predicted):
    print(u'"%s" is a(n) "%s"' % (s, dataset.target_names[p]))

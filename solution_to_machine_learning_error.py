#Noah Tashbook, based on the skeleton code
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics


languages_data_folder = sys.argv[1] #this line is the cause of 90% of my stress in this class today
dataset = load_files(languages_data_folder)

docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.5)

vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char', use_idf=False)

clf = Pipeline([ ('vec', vectorizer), ('clf', Perceptron(tol=1e-3)), ])

clf.fit(docs_train, y_train)

y_predicted = clf.predict(docs_test)

print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))

centimeter = metrics.confusion_matrix(y_test, y_predicted)

print(centimeter)


sentences = [
    u'The big black bug bit the big black bear',
    u'Ich habe das unter deinem Bett gefunden.',
    u'Dies ist ein Test, um die Sprache zu erkennen.',
	u'هذا جملة وانا الاحسن من كل الطلاي',
	u'dsjbsihvbareihvb ieh fiurwhfiuhwfiuo whiu iuhwriu hfwirufh iwuhfidsh i',
	u'1234567890',
	u'holy moly guacamole',
	u'will dr. tuttle actually check to see if I wrote this code?'
	u'can I trick this machine learning algorithm #espana',
	u'what about non alphanumeric characters?',
	u'!@# $%^ &*( ][',
	u'Jesus', #will it read as spanish?
]

predicted = clf.predict(sentences)

for s, p in zip(sentences, predicted):
    print(u'The language of "%s" is (I think) "%s"' % (s, dataset.target_names[p]))

import joblib
import numpy as np
import time
from sklearn.svm import LinearSVC
from sklearn.utils import shuffle

#Variables for us
train_split = 0.2

#import data

# Data is in the form of a txt file with each line corresponding to a gamestate and optimal move.
# The First 9 characters represent the gamespace, and the 10th character represents the optimal move


data = np.loadtxt('tictac_single.txt') #loads data into numpy array
X = data[:,:9] #Creates INPUT array of shape [SAMPLE SIZE, 9]
y = data[:,9:] #Creates target array of shape[SAMPLE SIZE, 1]


# Split Data into Trianing and Testing
if(train_split):
    X, y = shuffle(X,y) #SHUFFLE THE DATA RANDOMLY

    X_train = X[:int(train_split * X.shape[0])] # USE ONLY A certain amount of data for training
    y_train = y[:int(train_split * y.shape[0])] # use only a certain amount of data for training



#***********CREATING MODELS**************


# linear SVM
print("[INFO] Now Training and Testing the svmClassifier:")

svmClassifier = LinearSVC(random_state=0, tol=1e-5) # Instantiates an SVMClassifier Object

# fit the model to the data
startTime = time.time() # Records Training start time
svmClassifier.fit(X_train, np.ravel(y_train)) # fits the model to the training data
endTime = time.time() # Records end Time

# Check Accuracy on a test set
score = svmClassifier.score(X, y) # CHECKS ACCURACY OF THE MODEL

#print stuff
print("[INFO] total time taken to train the model: {:.2f}s".format(endTime - startTime)) #print total time
print("[INFO] The svm scored " + str(score) + ' on the test Data') #print total score on the data

joblib.dump(svmClassifier, 'svmClassifier.sav') # savethe model for later use

#Reccommended Variables to Use
#NUM_NEIGHBORS = ???
#weights = ???

#K neighbors Classifier

print("[INFO] Now Training and Testing the KNNClassifier:")

#Instantiate the KNN classifier

# knnClassifier =  *** INSTANTIATE A KNeighborsClassifier ****


# fit the KNN CLassifier
startTime = time.time_ns()
# ***** FIT THE KNN CLASSIFIER to the DATA HERE ******
endTime = time.time_ns()

#print total time
print("[INFO] total time taken to train the model: {:.2f}ms".format((endTime - startTime)/1000000))

# Check Accuracy on a test set

#score = ***** SCORE THE KNN CLASSIFIER HERE ******

print("[INFO] The knn scored " + str(score) + ' on the test Data')

joblib.dump(knnClassifier, 'knnClassifier.sav') # saving the classifier

#MLP Classifier

print("[INFO] Now Training and Testing the MLPClassifier:")

#Instantiate MLP Classifier

# mlpClassifier =   *** INSTANTIATE A MLPClassifier ****

#Fit The MLP Classifier
startTime = time.time()
# **** FIT the MLP Classifier Here ****
endTime = time.time()

#print total time
print("[INFO] total time taken to train the model: {:.2f}s".format(endTime - startTime))

#Check Accuracy on the Test Set

# score = **** SCORE THE MLP CLASSIFIER HERE ********

print("[INFO] The MLP model scored " + str(score) + ' on the test Data')

joblib.dump(mlpClassifier, 'mlpClassifier.sav') # saving the MLP CLASSIFIER










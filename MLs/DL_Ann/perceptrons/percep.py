from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split 


x, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)


X_Train,X_Test, Y_Train, Y_Test =  train_test_split(x,y, random_state=42)
clf = Perceptron( 

    max_iter=1000,
    eta0=0.1,
    random_state=42,
    tol=1e-3,
    shuffle=True,
)

clf.fit(X_Train, Y_Train)

accuracy = clf.score(X_Test, Y_Test) 
print(f"The Accurac Is: {accuracy*100} %")
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
y_train = y_train.ravel()
y_test = y_test.ravel()
model_lr = LogisticRegression(max_iter=5000)
model_lr.fit(X_train,y_train)
y_pred = model_lr.predict(X_test)
print("Accuracy:",round(accuracy_score(y_test,y_pred),3))
print(classification_report(y_test,y_pred))
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
y_train = y_train.ravel()
y_test = y_test.ravel()
model_svm = SVC(probability=True,random_state=10)
model_svm.fit(X_train,y_train)
y_pred_svm = model_svm.predict(X_test)
print("Accuracy:",round(accuracy_score(y_test,y_pred_svm),3))
print(classification_report(y_test,y_pred_svm))
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
model_nn = MLPClassifier(hidden_layer_sizes=(64,32),activation='relu',max_iter=1000,random_state=10)
model_nn.fit(X_train,y_train)
y_pred_nn = model_nn.predict(X_test)
print("Accuracy:",round(accuracy_score(y_test,y_pred_nn),3))
print(classification_report(y_test,y_pred_nn))



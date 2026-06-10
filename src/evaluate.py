from sklearn.metrics import accuracy_score
acc_lr=accuracy_score(y_test,y_pred_lr)
acc_svm=accuracy_score(y_test,y_pred_svm)
acc_nn=accuracy_score(y_test,y_pred_nn)
comparison = pd.DataFrame({
                          "Model":["Logistic Regression","SVM","Neural Network"],
                         "Accuracy": [acc_lr, acc_svm ,acc_nn]
})
comparison.sort_values(by="Accuracy",ascending=False) 
comparison
Model	Accuracy
from sklearn.metrics import f1_score
print("LR F1:",
      f1_score(y_test,y_pred_lr))
print("NN F1:",
      f1_score(y_test,y_pred_nn))
print("SVM F1:",
      f1_score(y_test,y_pred_svm))
from sklearn.metrics import roc_auc_score
y_prob_lr = model_lr.predict_proba(X_test)[:,1]
y_prob_nn = model_nn.predict_proba(X_test)[:,1]
y_prob_svm = model_svm.predict_proba(X_test)[:,1]
print("LR ROC-AUC:",
      roc_auc_score(y_test,y_prob_lr))
print("NN ROC-AUC:",
      roc_auc_score(y_test,y_prob_nn))
print("SVM ROC-AUC:",
      roc_auc_score(y_test,y_prob_svm))
from sklearn.metrics import mean_squared_error
import numpy as np
rmse_lr = np.sqrt(mean_squared_error(y_test,y_pred_lr))
print("LR RMSE:",rmse_lr)
rmse_nn = np.sqrt(mean_squared_error(y_test,y_pred_nn))
print("NN RMSE:",rmse_nn)
rmse_svm = np.sqrt(mean_squared_error(y_test,y_pred_svm))
print("SVM RMSE:",rmse_svm)
from sklearn.metrics import roc_curve,roc_auc_score
import matplotlib.pyplot as plt
y_prob_lr=model_lr.predict_proba(X_test)[:,1]
fpr,tpr,_ = roc_curve(y_test,y_prob_lr)
plt.plot(fpr,tpr,label="Logistic Regression")
plt.plot([0,1],[0,1],linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
print("AUC:",roc_auc_score(y_test,y_prob_lr))

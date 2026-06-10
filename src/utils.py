from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
cm_lr=confusion_matrix(y_test,y_pred_lr)
plt.figure(figsize=(6,4))
sns.heatmap(cm_lr,annot=True,fmt='d',cmap='Blues')
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

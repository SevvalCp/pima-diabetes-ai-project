from sklearn.model_selection import train_test_split
feature_columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Glucose_missing','BloodPressure_missing','SkinThickness_missing','Insulin_missing','BMI_missing']
predicted_class = ['Outcome']
X = df_flag[feature_columns].values
y = df_flag[predicted_class].values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.30,random_state=10
,stratify = y)
print(f"Eğitim seti:{X_train.shape}")
print(f"Test seti:{X_test.shape}")
print(f"Feature class:{feature_columns}")
print(f"Predicted class:{predicted_class}{np.unique(y)}")
Eğitim seti:(537, 13)
Test seti:(231, 13)
Feature class:['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Glucose_missing', 'BloodPressure_missing', 'SkinThickness_missing', 'Insulin_missing', 'BMI_missing']
Predicted class:['Outcome'][0 1]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.drop("Outcome", axis=1))
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df.drop("Outcome", axis = 1))

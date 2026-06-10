# Pima Diyabet Yapay Zeka Projesi
## Proje Genel Bakış
Bu proje, Pima Indians Diabetes veri setini ve makine öğrenmesi algoritmalarını kullanarak bir hastanın diyabet olup olmadığını tahmin etmeyi amaçlamaktadır. Diyabetin erken teşhisi, ciddi sağlık komplikasyonlarının önlenmesi ve hasta sonuçlarının iyileştirilmesi açısından kritik öneme sahiptir.
Proje, uçtan uca bir Yapay Zeka Proje Yaşam Döngüsünü takip etmektedir:
### Problem Tanımı
### Veri Toplama
### Veri Ön İşleme
### Keşifsel Veri Analizi (EDA)
### Model Geliştirme
### Model Değerlendirme
### Dağıtım (Deployment) Hazırlığı
## Problem Tanımı
Diyabet, dünya genelinde en yaygın kronik hastalıklardan biridir. Hastalığın erken aşamada tespit edilmesi, tedavi etkinliğini önemli ölçüde artırır ve sağlık maliyetlerini azaltır.
Bu projenin amacı, tıbbi ölçümlere dayanarak diyabet durumunu tahmin edebilen bir makine öğrenmesi modeli geliştirmektir.
### Paydaşlar
#### Sağlık profesyonelleri
#### Hastaneler ve klinikler
#### Hastalar
#### Araştırmacılar
### Başarı Kriterleri
#### Yüksek sınıflandırma doğruluğu
#### Yüksek ROC-AUC skoru
#### Güvenilir tahmin performansı
#### Açıklanabilir sonuçlar
### Kısıtlar
#### Sınırlı veri seti boyutu
#### Olası sınıf dengesizliği
#### Eksik ve gürültülü veriler
## Veri Seti Bilgisi
### Veri Seti
Pima Indians Diabetes Dataset
### Kaynak
#### Kaynak:Kaggle/UCI Machine Learning Repository
#### Kaynak:https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
### Özellikler
| Özellik                  | Açıklama                     |
| ------------------------ | ---------------------------- |
| Pregnancies              | Gebelik sayısı               |
| Glucose                  | Plazma glukoz konsantrasyonu |
| BloodPressure            | Diyastolik kan basıncı       |
| SkinThickness            | Triseps deri kalınlığı       |
| Insulin                  | Serum insülin seviyesi       |
| BMI                      | Vücut kitle indeksi          |
| DiabetesPedigreeFunction | Genetik diyabet risk skoru   |
| Age                      | Hastanın yaşı                |
| Outcome                  | Diyabet durumu (0/1)         |
### Veri Seti Boyutu
Toplam Kayıt: 768
Özellik Sayısı: 8
Hedef Değişken: Outcome
## Keşifsel Veri Analizi (EDA)
EDA, veri setini daha iyi anlamak ve önemli örüntüleri belirlemek için yapılmıştır.
### Yapılan Analizler
#### İstatistiksel özetler
#### Eksik değer analizi
#### Sınıf dağılım analizi
#### Korelasyon analizi
#### Aykırı değer tespiti
#### Özellik dağılım analizi
### Temel Bulgular
#### Glukoz, diyabet sonucu ile en güçlü ilişkiye sahiptir.
#### BMI ve yaş önemli tahmin değişkenleridir.
#### Bazı değişkenlerde eksik veri olarak yorumlanabilecek sıfır değerler bulunmaktadır.
#### Veri setinde orta düzeyde sınıf dengesizliği vardır.
### Görselleştirmeler
Aşağıdaki görselleştirmeler oluşturulmuştur:
#### Sınıf Dağılımı
#### Histogramlar
#### Kutu Grafikleri (Boxplot)
#### Korelasyon Isı Haritası
#### ROC Eğrisi
#### Karmaşıklık Matrisi (Confusion Matrix)
##### Görseller /images klasöründe bulunmaktadır
## Veri Ön İşleme
Aşağıdaki ön işleme adımları uygulanmıştır:
### Veri yükleme ve inceleme
### Özellik seçimi
## Veri Ön İşleme
Aşağıdaki ön işleme adımları uygulanmıştır:
### Veri yükleme ve inceleme
### Özellik seçimi
### StandardScaler ile veri normalizasyonu
### Eğitim-test bölme işlemi
### Cross-validation (çapraz doğrulama)
## Makine Öğrenmesi Modelleri
Üç farklı makine öğrenmesi algoritması uygulanmış ve karşılaştırılmıştır.
### Lojistik Regresyon
Temel model olarak kullanılan doğrusal sınıflandırma algoritmasıdır.
### Destek Vektör Makineleri (SVM)
Sınıflandırma problemleri için etkili bir gözetimli öğrenme algoritmasıdır.
### Yapay Sinir Ağı (NN)
Karmaşık ilişkileri öğrenebilen ve çok katmanlı yapılarla çalışan bir derin öğrenme modelidir.
## Model Değerlendirme
Aşağıdaki performans metrikleri kullanılmıştır:
### Accuracy
### Precision
### Recall
### F1 Skoru
### ROC-AUC
### RMSE
### Cross Validation
Modelin genellenebilirliğini değerlendirmek için 10 katlı çapraz doğrulama uygulanmıştır.
Değerlendirme Sonuçları
#### OPTIMIZATION MODEL COMPARISON =
Logistic Regression:0.797
SVM:0.801
Neural Network:0.745
#### Cross Validation Scores:
[0.74074074 0.74074074 0.75925926 0.72222222 0.7037037  0.7962963
 0.81481481 0.62264151 0.71698113 0.69811321]
Ortalama:0.7316
#### Accuracy_score
<img width="272" height="157" alt="image" src="https://github.com/user-attachments/assets/c516866d-627a-4b49-8ebd-6018fbcd1164" />
#### F1_score
LR F1: 0.6802721088435374
NN F1: 0.6040268456375839
SVM F1: 0.6933333333333334
#### Roc_auc_score
LR ROC-AUC: 0.8548971193415636
NN ROC-AUC: 0.7937448559670781
SVM ROC-AUC: 0.8350617283950617
#### RMSE
LR RMSE: 0.4510689564392605
NN RMSE: 0.5053822864043174
SVM RMSE: 0.4462445508173732
#### En İyi Model
Deneysel sonuçlara göre, Lojistik Regresyon en dengeli performansı ve en yüksek ROC-AUC skorunu elde etmiştir.

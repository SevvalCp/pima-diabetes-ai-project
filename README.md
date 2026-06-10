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
Kaynak:Kaggle/UCI Machine Learning Repository
Kaynak:https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
## Özellikler
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


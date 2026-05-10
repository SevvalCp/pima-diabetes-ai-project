# Veri Toplama & Etiketleme
## Veri Envanteri
### Veri Kaynağı
Bu projede kullanılan veri seti,diyabet tahmini çalışmalarında yaygın olarak tercih edilen Pima Indians Diabetes Dataset veri setidir.
Veri seti,kadın bireylere ait çeşitli sağlık ölçümlerini içermekte olup bireylerin diyabet hastası olup olmadığını belirlemeyi amaçlamaktadır.
#### Pima Indians Diabetes Dataset
Kaynak:Kaggle/UCI Machine Learning Repository
Kaynak:https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
### Veri Seti Özeti
Veri seti toplamda 768 gözlem(satır) ve 8 bağımsız değişken(özellik) içermektedir.Ayrıca bireyin diyabet durumunu gösteren 1 hedef değişken bulunmaktadır.
Her satır bir bireyi temsil etmektedir.Özellikler bireyin sağlık ölçümleri ve fiziksel bilgilerini içermektedir
(768,9)
#### Toplam gözlem sayısı:768
#### Toplam özellik sayısı:8
#### Hedef değişken sayısı:1
Hedef değişken:Bireyin diyabet hastası olup olmadığını göstermektedir.(Outcome).
Outcome değer 0 ise birey "Diyabet değil",outcome değer 1 ise birey "Diyabet hastası".
Bu proje bir ikili sınıflandırma(binary classification) problemidir.
### Veri Ön İşleme ve Temizleme Planı
Makine öğrenmesi modellerinin daha doğru ve güvenilir sonuçlar verebilmesi için veri seti üzerinde çeşitli veri ön işleme işlemleri uygulanacaktır.
#### Gerçekçi Olmayan 0 Değerlerin Düzenlenmesi
Veri setindeki bazı sütunlarda biyolojik olarak gerçekçi olmayan 0 değerleri bulunmaktadır.Özellikle aşağıdaki değişkenlerde sıfır değeri anlamlı değildir:
##### Glucose
##### BloodPressure
##### SkinThickness
##### Insulin
##### BMI
Bu nedenle söz konusu değerler eksik veri olarak değerlendirilecektir.
<img width="978" height="537" alt="image" src="https://github.com/user-attachments/assets/5c088a88-6fdc-49bc-82a8-099d1338ec23" />
##### Gerçekçi Olmayan 0 Değerlerin İşlenmesi
Gerçekçi olmayan 0 değerleri eksik veri olarak işaretlenecektir ve veri kaybını önlemek amacıyla uygun yöntemlerle doldurulacaktır.
Kullanılması planlanan yöntemler:
###### Ortalama(Mean) ile doldurma
###### Veri dağılımına göre uygun yöntemin seçilmesi
##### Veri Görselleştirme
Veri setinin daha iyi anlaşılması amacıyla çeşitli görselleştirme işlemleri yapılacaktır.
Planlanan görselleştirmeler:
###### Histogram grafikleri
###### Korelasyon matrisi
###### Eksik Değer Tespiti
###### Sınıf dağılımı grafikleri
###### Heatmap görselleştirmeleri
###### Boxplot grafikleri
##### Veri Ölçeklendirme
Makine öğrenmesi algoritmalarının performansını artırmak amacıyla gerekli durumlarda veri ölçeklendirme işlemleri uygulanacaktır.
Kullanılması planlanan yöntemler:
###### StandardScaler
###### MinMaxScaler
Özellikle Logistic Regression,SVM ve KNN gibi algoritmalar için ölçeklendirme önemli bir adımdır.
#### Boş Değer Tespiti
Bu veri setinde eksik(null) değer yoktur.
<img width="397" height="272" alt="image" src="https://github.com/user-attachments/assets/6c683925-bb9a-4023-8d4d-7fec9f95aa4d" />
### Veri Sözlüğü
| Değişken | Açıklama  |Veri Tipi|
|----------|----------|----------|
| Pregnancies   | Bireyin geçirdiği hamilelik sayısı  | Sayısal  |
|  Glucose    | Kandaki glikoz (şeker) seviyesi   |  Sayısal  |
| BloodPressure |  Dinlenme halindeki kan basıncı değeri | Sayısal |
|  SkinThickness    |  Deri kıvrım kalınlığı ölçümü      | Sayısal     |
| Insulin   | Kandaki insülin seviyesi  | Sayısal  |
|  BMI    |  Vücut kitle indeksi | Sayısal    |
| DiabetesPedigreeFunction   |  Aile geçmişine bağlı diyabet riski katsayısı | Sayısal   |
|  Age    | Bireyin yaşı    | Sayısal       |
| Outcome  | Diyabet durumu(0: Sağlıklı, 1: Diyabet)| Kategorik |

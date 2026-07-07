## Streamlit Uygulamasını Çalıştırma

Bu projede kullanıcı arayüzü **Streamlit** kullanılarak geliştirilmiştir.
Diyabet risk tahmin sistemini kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### 1. Projeyi Visual Studio Code ile Açma

Öncelikle proje klasörünü **Visual Studio Code** ile açın.
Bilgisayarınızda Python'un kurulu olduğundan ve gerekli kütüphanelerin yüklendiğinden emin olun.

### 2. Gerekli Kütüphanelerin Kurulması

Visual Studio Code içerisindeki terminali açın ve proje içerisindeki gerekli kütüphaneleri yükleyin:
```bash pip install -r requirements.txt```

### 3. Streamlit Uygulamasını Başlatma

Streamlit uygulama dosyasının bulunduğu klasöre gidin.

```bash cd proje_klasoru```

Streamlit uygulamasını çalıştırmak için komutu kullanın:
```bash streamlit run app.py ```

### 4. Uygulamaya Erişim

Komut başarılı bir şekilde çalıştırıldığında Streamlit yerel bir sunucu başlatacaktır.
Uygulama genellikle otomatik olarak varsayılan internet tarayıcısında açılır.
Eğer otomatik açılmazsa, terminalde gösterilen aşağıdaki adrese giderek uygulamaya erişebilirsiniz:

```http://localhost:8501```

### 5. Diyabet Tahmin Sisteminin Kullanımı

Uygulama açıldıktan sonra kullanıcıdan aşağıdaki bilgiler istenir:
* Gebelik sayısı (Pregnancies)
* Glikoz değeri (Glucose)
* Kan basıncı (Blood Pressure)
* Cilt kalınlığı (Skin Thickness)
* İnsülin değeri (Insulin)
* Vücut kitle indeksi (BMI)
* Diyabet soy ağacı fonksiyonu (Diabetes Pedigree Function)
* Yaş (Age)
Daha sonra kullanıcı aşağıdaki makine öğrenmesi modellerinden birini seçebilir:
* Logistic Regression
* Support Vector Machine (SVM)
* Neural Network
#### **Predict** butonuna basıldığında seçilen modele göre diyabet risk tahmini gerçekleştirilir.

### Önemli Bilgilendirme

Bu uygulama, makine öğrenmesi modelleri kullanılarak geliştirilmiş bir **diyabet risk tahmin sistemidir**.
Elde edilen sonuçlar tıbbi tanı yerine geçmez ve %100 kesin sonuç garantisi vermez.
En güvenilir tahmin performansı için **Neural Network modeli önerilmektedir**.
Sağlık ile ilgili kesin kararlar mutlaka uzman sağlık profesyonelleri tarafından verilmelidir.

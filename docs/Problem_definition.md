# Problem Tanımlama
## Problem Tanımı
Diyabet erken teşhis edilmediğinde kalp-damar hastalıkları,böbrek yetmezliği,görme kaybı ve sinir hasarı gibi ciddi sağlık problemlerine neden olabilmektedir.
Hastalığın başlangıç evrelerinde belirtiler her zaman açık şekilde görülmediği için birçok birey uzun süre diyabet hastası olduğunu fark edememektedir.
Geleneksel teşhis yöntemleri uzman değerlendirmesi ve laboratuvar testleri gerektirdiğinden zaman ve maliyet açısından yük oluşturabilmektedir.
Bu nedenle sağlık verileri kullanılarak otomatik tahmin sistemlerinin geliştirilmesi büyük önem taşımaktadır. 
Bu projede veri setinde yer alan belirli tanısal ölçümlere dayanarak bireylerin diyabet hastası olup olmadığını makine öğrenmesi yöntemleri ile tanısal olarak tahmin etmek amaçlanmıştır. 
Çalışmada kullanılan veriler üzerinden modeller eğitilerek, bireyin diyabet riskini otomatik olarak belirleyen bir karar destek sistemi geliştirilmesi hedeflenmiştir. 
Böylece erken teşhis sürecine katkı sağlanması,erken teşhis oranlarının artırılması,sağlık çalışanlara hastalığın tespit sürecinde destek olması ve sağlık hizmetlerinin daha verimli hale getirilmesi amaçlanmaktadır.

## Problem
Bu çalışmada çözülmek istenen temel problem, bireylerin sağlık verileri kullanılarak diyabet hastası olup olmadıklarının doğru şekilde tahmin edilmesidir. 
Veri setinde yer alan glikoz seviyesi,kan basıncı,insülin değeri,vücut kitle indeksi (BMI),yaş ve gebelik sayısı gibi özellikler kullanılarak bir sınıflandırma modeli oluşturulacaktır. 
Modelin amacı,bireyin “diyabet” veya “diyabet değil” sınıflarından hangisine ait olduğunu tahmin etmektir. 
Makine öğrenmesi algoritmaları kullanılarak geliştirilecek bu sistemin;yüksek doğruluk oranına sahip olması,yanlış teşhis oranını azaltması,erken teşhis sürecini desteklemesi,sağlık uzmanlarına yardımcı olması beklenmektedir. 
Bu kapsamda farklı makine öğrenmesi algoritmaları eğitilecek, performansları karşılaştırılacak ve en başarılı model belirlenmeye çalışılacaktır.
Karşılaştırmalar sonucu en başarılı olan model ile ilerlenecektir. 

## Paydaş Analizi
Bu projeden doğrudan veya dolaylı olarak etkilenen paydaşlar şunlardır:
### Hastaneler:Hastaneler,geliştirilen sistem sayesinde hastaların risk analizlerini daha hızlı gerçekleştirebilir ve teşhis süreçlerini destekleyebilir. 
### Doktorlar ve sağlık çalışanları:Doktorlar,makine öğrenmesi tabanlı tahmin sonuçlarını yardımcı karar destek sistemi olarak kullanabilir.Bu sistem sayesinde sağlık çalışanlarının iş yükünün de hafifletilmesi amaçlamnmıştır.
### Hastalar:Hastaların erken risk tespiti sayesinde daha hızlı tedavi sürecine başlanabilir ve olası komplikasyonların önüne geçilebilir.
### Sağlık Kuruluşları:Sağlık kuruluşları,toplum sağlığı analizlerinde ve erken teşhis çalışmalarında bu tür sistemlerden faydalanabilir. 

## Başarı Metrikleri
Model performansını değerlendirmek için aşağıdaki metrikler kullanılacaktır:
### Accuracy(Doğruluk):Modelin toplam tahminler içerisindeki doğru tahmin oranını göstermektedir. 
### Precision(Kesinlik):Pozitif tahmin edilen bireylerin gerçekten diyabet hastası olma oranını ifade eder.
### Recall(Duyarlılık):Gerçek diyabet hastalarının model tarafından doğru şekilde tespit edilme oranını göstermektedir.
### F1 Score:Precision ve Recall değerlerinin harmonik ortalamasıdır.Özellikle dengesiz veri setlerinde önemli bir metriktir.
### ROC-AUC:Modelin sınıfları ayırt etme başarısını ölçen performans metriğidir.AUC değerinin yüksek olması modelin daha başarılı olduğunu göstermektedir. 

## Kısıtlar
### Küçük Veri Seti:Veri setinin sınırlı sayıda örnek içermesi modelin genelleme performansını etkileyebilir. 
### Eksik Veriler:Bazı sütunlarda eksik veya sıfır değerler bulunabilir.Bu durum veri ön işleme aşamasında ek işlemler gerektirmektedir. 
### Veri Dengesizliği:Diyabet hastası ve sağlıklı birey sayıları arasında dengesizlik bulunmaktadır.Bu durum modelin bazı sınıflara eğilim göstermesine neden olabilir. 
### Gerçek Dünya Karmaşıklığı:Gerçek hayatta diyabet oluşumunu etkileyen çok daha fazla faktör bulunmaktadır.Veri seti tüm sağlık koşullarını tam olarak temsil etmeyebilir. 
### Anlamsız/Gerçekçi Olmayan Değerler:Veri setinde bazı sütunlarda gerçek hayatta anlamlı olmayan çok sayıda 0 değeri bulunmaktadır.Özellikle glikoz seviyesi, insülin değeri, BMI ve kan basıncı gibi özelliklerde bulunan sıfır değerler biyolojik olarak gerçekçi değildir. 
Bu nedenle veri ön işleme aşamasında söz konusu değerlerin analiz edilmesi ve uygun yöntemlerle düzeltilmesi gerekmektedir. 

## Literatür Özeti
Literatürde diyabet tahmini üzerine yapılan çalışmalarda birçok makine öğrenmesi algoritmasının başarılı sonuçlar verdiği görülmektedir. 
Logistic Regression algoritması yorumlanabilir yapısı nedeniyle sıklıkla tercih edilmektedir. 
Random Forest algoritması yüksek doğruluk oranı ve aşırı öğrenmeye karşı dayanıklılığı ile öne çıkmaktadır. 
Support Vector Machine(SVM),özellikle sınıflandırma problemlerinde güçlü performans göstermektedir. 
K-Nearest Neighbors(KNN) ve Decision Tree algoritmaları diyabet tahmini çalışmalarında yaygın şekilde kullanılmaktadır. 
Araştırmalar,veri ön işleme ve özellik mühendisliği işlemlerinin model performansını önemli ölçüde artırdığını göstermektedir. 
Bu projede de farklı algoritmalar karşılaştırılarak en uygun model belirlenmeye çalışılacaktır. 


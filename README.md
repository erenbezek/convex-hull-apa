# Convex Hull Analyzer: Brute Force vs. Graham Scan

Düzlemdeki rastgele bir nokta kümesini çevreleyen en küçük dışbükey poligonu (**Convex Hull**) bulan iki farklı algoritmanın teorik ve deneysel analiz aracıdır.

## 🎯 Projenin Amacı
Bu proje, **Bursa Teknik Üniversitesi** Algoritma Analizi ve Tasarımı dersi kapsamında geliştirilmiştir. Temel amacı:
* [cite_start]**Kaba Kuvvet ($O(n^3)$)** ve **Graham Scan ($O(n \log n)$)** algoritmalarının teorik karmaşıklıklarını gerçek çalışma süreleri ile ilişkilendirmek. [cite: 3, 4]
* [cite_start]Büyük veri setlerinde algoritmalar arasındaki dramatik performans farkını görsel ve deneysel olarak kanıtlamak. [cite: 8]

## 🛠️ Teknik Özellikler
* [cite_start]**Dinamik Girdi:** Kullanıcı uygulama üzerinden $N$ (nokta sayısı) değerini anlık olarak değiştirebilir. [cite: 18]
* [cite_start]**İnteraktif GUI:** Matplotlib tabanlı arayüz ile algoritmaların sonuçları canlı olarak ekranda çizdirilir. [cite: 18, 19]
* [cite_start]**Kapsamlı Performans Testi:** Tek bir butonla farklı $N$ değerleri için otomatik zaman ölçümü ve karşılaştırmalı grafik üretimi yapılır. [cite: 52]



## [cite_start]📊 Algoritma Karşılaştırması [cite: 21]

| Özellik | Kaba Kuvvet (Brute Force) | Graham Scan |
| :--- | :--- | :--- |
| **Teorik Karmaşıklık** | [cite_start]$O(n^3)$ [cite: 38] | [cite_start]$O(n \log n)$ [cite: 43] |
| **Yöntem** | [cite_start]Her nokta çiftini ve konumunu kontrol eder. [cite: 24] | [cite_start]Açısal sıralama ve yığın (stack) yapısını kullanır. [cite: 27, 28] |
| **Büyük Veri Performansı** | [cite_start]$N=1500$ sonrası çalışma süresi makul sınırların dışına çıkar. [cite: 118, 119] | [cite_start]Çok büyük veri setlerinde dahi stabil ve hızlı çalışır. [cite: 144] |

## 📉 Deneysel Bulgular
Yapılan testlerde aşağıdaki kritik sonuçlar elde edilmiştir:
* [cite_start]**Verimlilik Farkı:** $N=5000$ noktada Kaba Kuvvet algoritması yaklaşık **112 saniye** sürerken [cite: 125, 235][cite_start], Graham Scan aynı işlemi **0.005 saniye** içinde tamamlamaktadır. [cite: 152]
* [cite_start]**İşlem Yükü:** Kaba Kuvvet için çalışma süresi makine kaynaklarına bağlı olarak **23 dakikaya** kadar çıkabilmektedir. [cite: 135]



## 🚀 Kurulum ve Kullanım
Proje tek bir Python dosyası üzerinden çalışacak şekilde tasarlanmıştır.

1.  **Gereksinimleri yükleyin:**
    ```bash
    pip install numpy matplotlib
    ```
2.  **Uygulamayı çalıştırın:**
    ```bash
    python algoproje.py
    ```

## [cite_start]🤖 Yapay Zeka (LLM) Katkısı [cite: 95]
Proje geliştirme sürecinde **Gemini (LLM)** bir destek ve öğrenme aracı olarak kullanılmıştır:
* [cite_start]**Hata Ayıklama:** Graham Scan algoritmasında hassas zaman ölçümü için `time.perf_counter` kullanımı LLM desteğiyle sağlanmıştır. [cite: 369]
* [cite_start]**GUI Tasarımı:** Matplotlib `widgets` modülü üzerinden TextBox ve Button yapıları kurulmuştur. [cite: 371, 372]
* [cite_start]**Doğrulama:** Üretilen kodlar ve teorik analizler manuel olarak doğrulanmıştır. [cite: 376]

---
[cite_start]**Yazar:** Eren Bezek (22360859011) [cite: 106, 107]  
[cite_start]**Danışman:** Dr. Öğretim Üyesi Seçkin YILMAZ [cite: 110]

---

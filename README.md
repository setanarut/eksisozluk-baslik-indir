# Ekşi Sözlük başlık arşivleyici (Scrapper)

Ekşi Sözlük başlıklarını CSV olarak arşivler. (pandas)


# Kullanım

Gerekli paketleri kurmak için:

```bash
pip3 install -r requirements.txt
```


Komut satırına aşağıdaki şekilde ekşi başlık adresini argüman olarak yazın:

```bash
python3 eksi_indir.py https://eksisozluk1923.com/armut--34642
```

İlerleme çubuğu:

```bash
Sayfalar indiriliyor: 100%|████████████████████| 20/20 [00:08<00:00,  2.33 sayfa/s]
dosya kaydedildi:  armut--34642.csv
```

# CSV dosyasını tek sayfa HTML yapma

Çok fazla sayfalı ekşisözlük başlıklarında tavsiye edilmez

```bash
python3 csv2html.py armut--34642.csv
```

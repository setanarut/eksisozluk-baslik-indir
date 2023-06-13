# Ekşi Sözlük başlık arşivleyici (Scraper)

Ekşi Sözlük başlıklarını CSV olarak arşivler. (pandas)


## Kullanım

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

## Örnek CSV

|entry                                                                                                                                                                    |yazar                             |tarih     |entry_id|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|----------|--------|
|dibine du$er, bide pi$ipte du$enleri wardir turk milletini temsil eder ..                                                                                                |lord                              |1999-06-20|10204   |
|argoda antenle benzer anlam ta$ir. (bkz: anten)                                                                                                                          |rotting horse on the deadly ground|1999-07-08|17392   |
|dalinda guzel, ac karna yiyince karin agritiyo  armut seklinde balonlar vardir                                                                                           |lord                              |1999-08-16|26971   |
|1-bir meyve ce$idimiz 2-murat adli arkada$larma hitap edi$ tarzim :)                                                                                                     |elmyra                            |1999-08-16|27181   |
|birçok soru cümlesine cevap olarak söylenebilecek bir sözcük.  örnek:  - aaa o elindeki ne? - armut.                                                                     |guru                              |2000-04-24|145395  |
|minik olanlari nefis tatli, bal gibi olur, cerez niyetine yenir ucer beser..tam mevsimi bu aralar..                                                                      |cressida                          |2000-06-28|218278  |
|sarısı makbuldur, inşallah.                                                                                                                                              |guru                              |2000-10-15|247784  |
|sahibinin cronos usta oldugu anet in en eski odalarindan birisi. zamaninda bu oda yuzunden cok sava$lar cikmi$ti (bkz. eski gunler).                                     |castro                            |2001-08-10|589665  |
|manavların herkese üstü kapalı ,ima yoluyla, ayı diye hitap etmesine sebebiyet veren sarı renkli meyvegil.   manavcı: -gel abi geeeellllllllll... armutun iyisi burada...|beckham                           |2001-10-03|707761  |
|(bkz: armudun iyisini ayilar yer)                                                                                                                                        |zeneboge                          |2001-10-12|730792  |

## CSV dosyasını tek sayfa HTML yapma

Çok fazla sayfalı ekşisözlük başlıklarında tavsiye edilmez

```bash
python3 csv2html.py armut--34642.csv
```

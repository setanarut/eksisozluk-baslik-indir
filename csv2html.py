import pandas as pd
import sys

dosya = str(sys.argv[1])

df = pd.read_csv(dosya)

ht = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            font-size: 11pt;
            line-height: 1.4;
            text-align: right;
            color: rgba(255, 255, 255, 0.766);
            background-color: rgb(40, 40, 40);
            max-width: 500px;
  margin: auto;
  padding: 10px;
            font-family: sans-serif}
        sup {
            padding-top: 0%;
            color: rgb(230, 149, 163)
        }
        p {
            text-align: left;
            padding: 12pt;
            background-color:rgba(255, 255, 255, 0.071);
            white-space: break-spaces;}
    </style>
</head>
<body>"""

kp = """
</body>
</html>"""
with open(dosya + ".html", "w") as outfile:
    outfile.write(ht)
    outfile.write("\n".join("<p> " + str(entry) + "</p>" + "<sup>" + str(yazar) + " - " + str(tarih) + " - " + str(entry_id) + "</sup>" for tarih, yazar, entry, entry_id in zip (df.tarih, df.yazar, df.entry, df.entry_id)))
    outfile.write(kp)

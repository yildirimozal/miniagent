---
name: xml-format
version: 0.1.0
description: Sıkışık veya okunması zor XML/HTML metinlerini girintili ve düzgün formata çevirir.
icon: "📝"
example_prompt: "Şu XML'i düzelt: <root><item>test</item></root>"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [python3]
  internet: false
tags: [xml, format, developer, parser]
---

# XML Format Skill

Kullanıcının verdiği XML string'ini ayrıştırıp (parse) göze hoş gelen, uygun boşluk ve girintilerle formatlanmış hale (pretty print) getirir.

## Yöntem

Bunu Python'un standart kütüphanesindeki `xml.dom.minidom` modülünü kullanarak bash üzerinden yapabiliriz:

```bash
python3 -c '
import sys
import xml.dom.minidom
try:
    xml_string = sys.argv[1]
    dom = xml.dom.minidom.parseString(xml_string)
    # Boş satırları temizleyip formatlamak için
    pretty_xml = "\n".join([line for line in dom.toprettyxml(indent="  ").split("\n") if line.strip()])
    print(pretty_xml)
except Exception as e:
    print(f"HATA: XML ayrıştırma başarısız oldu. {e}")
' "XML_ICERIGI_BURAYA"
```

## Sonuç işleme

Sonuç başarılıysa dönen metni Markdown `xml` kod bloğu içinde kullanıcıya sun.
Eğer ayrıştırma (parse) hatası oluşursa, hatayı Türkçe olarak bildir ve XML'in eksik veya hatalı etiketler içerdiğini belirt.

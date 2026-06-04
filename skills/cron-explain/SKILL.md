---
name: cron-explain
version: 0.1.0
description: Bir cron ifadesini insan tarafından okunabilir Türkçe açıklamaya çevirir.
icon: "⏱️"
example_prompt: "'*/5 * * * *' cron ifadesi ne anlama geliyor?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [cron, schedule, time, dev]
---

# Cron Explain Skill

Bir cron ifadesini (5 veya 6 alanlı) insan tarafından okunabilir Türkçe
açıklamaya çevirmek için `python3` kullanılır. Tamamlayıcı skill'ler:
`date-calc` (tarih aritmetiği), `timezone-convert` (zaman dilimi dönüşümü).

## Çalıştırılacak komut

```
python3 -c "
fields = '<cron_ifadesi>'.split()
labels = ['dakika', 'saat', 'ayın günü', 'ay', 'haftanın günü']
if len(fields) == 6:
    labels.insert(0, 'saniye')
gun_isimleri = {0:'Pazar',1:'Pazartesi',2:'Salı',3:'Çarşamba',4:'Perşembe',5:'Cuma',6:'Cumartesi',7:'Pazar'}
ay_isimleri = {1:'Ocak',2:'Şubat',3:'Mart',4:'Nisan',5:'Mayıs',6:'Haziran',7:'Temmuz',8:'Ağustos',9:'Eylül',10:'Ekim',11:'Kasım',12:'Aralık'}
for i, (f, l) in enumerate(zip(fields, labels)):
    if f == '*':
        print(f'{l}: her {l}')
    elif f.startswith('*/'):
        print(f'{l}: her {f[2:]} {l}da bir')
    elif ',' in f:
        print(f'{l}: {f} değerlerinde')
    elif '-' in f:
        print(f'{l}: {f} aralığında')
    else:
        print(f'{l}: {f}')
"
```

`<cron_ifadesi>` yerine kullanıcının verdiği cron ifadesini koy.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Her alanı ayrı ayrı açıkla
- Sonunda tek bir **özet cümle** oluştur (ör. "Her gün saat 03:00'te çalışır")
- Yaygın kalıpları tanı ve doğal dilde ifade et:
  - `0 0 * * *` → "Her gece yarısı"
  - `*/5 * * * *` → "Her 5 dakikada bir"
  - `0 9 * * 1-5` → "Hafta içi her gün saat 09:00'da"

## Hata durumları

- **Geçersiz alan sayısı:** Cron ifadesi 5 veya 6 alandan oluşmalı; eksik/fazla
  alan varsa uyar.
- **Geçersiz değer:** Alanlar beklenmeyen karakter içeriyorsa bildir.
- **`python3` bulunamadı:** Python 3 kurulu olmalı.

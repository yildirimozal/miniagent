---
name: password-strength
version: 0.1.0
description: Bir parolanın gücünü (entropi/tahmin süresi) kabaca değerlendirir.
icon: "💪"
example_prompt: "şu parola ne kadar güçlü?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [security, password, entropy]
---

# Password Strength Skill

Bir parolanın kaba güç tahminini (karakter havuzu + uzunluk → entropi biti)
hesaplar. Python ile yerel çalışır; parola hiçbir yere gönderilmez.

> 🔐 **Güvenlik:** Parolayı komut satırına yazmak onu **shell geçmişine ve
> süreç listesine** sızdırır. Parolayı geçici bir dosyaya kaydet, oradan oku,
> sonra dosyayı sil.

## Çalıştırılacak komut

Parolayı geçici bir dosyaya koy (örn. `~/pw.txt`), sonra:

```
python3 -c '
import sys, math
p = open(sys.argv[1]).read().rstrip("\n")
pool = 0
if any(c.islower() for c in p): pool += 26
if any(c.isupper() for c in p): pool += 26
if any(c.isdigit() for c in p): pool += 10
if any(not c.isalnum() for c in p): pool += 33
bits = len(p) * math.log2(pool) if pool else 0
verdict = ("çok zayıf" if bits < 28 else "zayıf" if bits < 36 else
           "orta" if bits < 60 else "güçlü" if bits < 128 else "çok güçlü")
print(f"uzunluk={len(p)}  havuz={pool}  entropi≈{bits:.0f} bit  →  {verdict}")
' ~/pw.txt
```

İşlem sonrası: `rm ~/pw.txt`.

## Sonuç işleme

`bash` tool'undan gelen sonucu kullanıcıya **doğal Türkçe** ile aktar:
- Entropi bitini ve sözel değerlendirmeyi söyle
- Bu **kaba bir tahmin**: sözlük kelimeleri, yaygın desenler (123456, qwerty)
  hesaba katılmaz — gerçek güç daha düşük olabilir
- İyileştirme öner: uzunluk artır, karakter çeşitliliği ekle, anlamlı kelime kullanma
- Parolayı geçici dosyadan **silmesini** hatırlat

## Hata durumları

- **`python3` bulunamadı:** Python 3 kur.
- **Dosya bulunamadı:** Geçici parola dosyasının yolunu teyit et.
- **Boş çıktı/0 bit:** Dosya boş; parola gerçekten girilmiş mi kontrol et.

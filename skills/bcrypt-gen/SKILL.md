---
name: bcrypt-gen
version: 0.1.0
description: Verilen düz metni (şifreyi) bcrypt algoritması ile hashler.
icon: "🔐"
example_prompt: "Şu şifre için bcrypt hash oluştur: gizlisifre123"
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
tags: [security, password, hash, bcrypt]
---

# Bcrypt Hash Generator Skill

Veritabanına elle kullanıcı eklerken veya test yaparken geliştiricilerin sık sık ihtiyaç duyduğu `bcrypt` hash değerini oluşturur.

## Yöntem

Eğer sistemde Node.js varsa `bcrypt` kütüphanesi gerekebilir. Eğer Python varsa `bcrypt` modülü veya standart kütüphane alternatifleri kullanılabilir. Ancak en garantili yol Python kullanarak bunu test etmektir. Python'da `bcrypt` kurulu değilse, standart `hashlib` ile pbkdf2 gibi bir alternatif sunulabilir veya hata verilir.

```bash
python3 -c '
import sys
try:
    import bcrypt
    password = sys.argv[1].encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    print("BCRYPT_HASH:", hashed.decode("utf-8"))
except ImportError:
    print("HATA: Python bcrypt kütüphanesi kurulu değil. (pip install bcrypt)")
' "SIFRE_BURAYA"
```

## Sonuç işleme

Hash işlemi başarılı olursa, `BCRYPT_HASH` yazısından sonra gelen $2b$... şeklindeki değeri kullanıcıya Markdown kod bloğunda göster.
Eğer kurulu olmadığı için hata verirse, "Sisteminizde bcrypt modülü yüklü değil, yüklemek için `pip install bcrypt` komutunu kullanabilirsiniz" uyarısını yap.

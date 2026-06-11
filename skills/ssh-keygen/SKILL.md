---
name: ssh-keygen
version: 0.1.0
description: Yeni bir SSH anahtar çifti (ed25519 veya RSA) üretir.
icon: "🗝️"
example_prompt: "github için yeni bir ssh anahtarı oluştur"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ssh-keygen]
  internet: false
tags: [security, ssh, key, generate]
---

# SSH Keygen Skill

Yeni bir SSH anahtar çifti üretir. Modern öneri **ed25519**; uyumluluk gerekirse
4096-bit RSA.

## Çalıştırılacak komut

**ed25519 (önerilen):**

```
ssh-keygen -t ed25519 -C "<yorum/mail>" -f <çıktı_yolu>
```

**RSA 4096 (eski sistemler için):**

```
ssh-keygen -t rsa -b 4096 -C "<yorum/mail>" -f <çıktı_yolu>
```

`<çıktı_yolu>` örn. `~/.ssh/id_github`. İki dosya üretilir: private key
(`<yol>`) ve public key (`<yol>.pub`). `ssh-keygen` **parola (passphrase)**
sorar — boş bırakılabilir ama güvenlik için parola önerilir.

> ⚠️ Mevcut bir anahtarın üzerine yazmamak için yeni, benzersiz bir dosya adı
> seç (`~/.ssh/id_ed25519` zaten varsa farklı ad ver).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Private ve public key dosyalarının yollarını belirt
- **Sadece `.pub` (public) dosyası paylaşılır** — private key asla paylaşılmaz
- GitHub/sunucuya eklemek için `.pub` içeriğini göstermeyi öner
  (`cat <yol>.pub`)

## Hata durumları

- **Dosya zaten var:** `ssh-keygen` üzerine yazmak ister; mevcut anahtarı
  kaybetmemek için farklı ad kullan.
- **`~/.ssh` yok:** `mkdir -p ~/.ssh && chmod 700 ~/.ssh` ile oluştur.
- **İzin hatası:** Hedef dizine yazma izni gerekir.

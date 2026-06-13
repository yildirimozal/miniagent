---
name: kill-port
version: 0.1.0
description: Belirtilen portu (örn. 3000) dinleyen süreci bulur ve onaylı şekilde sonlandırır.
icon: "🔌"
example_prompt: "3000 portunu kullanan süreci kapat"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, process_control]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [lsof]
  internet: false
tags: [network, port, process, kill, dev]
---

# Kill Port Skill

"Port zaten kullanımda / address already in use" hatasının çözümü: bir portu
dinleyen süreci bulur ve **kullanıcı onayıyla** sonlandırır.

> ⚠️ Bu skill bir süreci **öldürür** (geri alınamaz; kaydedilmemiş iş kaybolabilir).
> Önce hangi sürecin öldürüleceğini **göster**, kullanıcıdan **onay al**, sonra öldür.

## Çalıştırılacak komut

**1. Önce portu KİM tutuyor — göster (öldürme):**

```
lsof -i :<port>
```

Bu; süreç adını (COMMAND), PID'i, kullanıcıyı ve durumu listeler. Çıktıyı
kullanıcıya göster ve **"bu süreci kapatayım mı?"** diye sor.

**2. Onaydan sonra — nazikçe sonlandır (SIGTERM):**

```
lsof -ti :<port> | xargs kill
```

`lsof -ti` sadece PID döndürür; `kill` (sinyal 15) sürece düzgün kapanma şansı verir.

**3. Hâlâ ölmediyse — zorla (SIGKILL):**

```
lsof -ti :<port> | xargs kill -9
```

`-9` son çare; veriyi kaydetme şansı bırakmaz.

**Linux'ta `lsof` yoksa alternatif:**

```
fuser -k <port>/tcp
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Önce hangi sürecin (ad + PID) portu tuttuğunu söyle, onay iste
- Öldürdükten sonra portun boşaldığını teyit et (1. komutu tekrar çalıştır,
  çıktı boşsa port serbest)
- Zorla (`-9`) gerekti mi belirt

## Hata durumları

- **Çıktı boş (port boşta):** O portu dinleyen süreç yok; kullanıcıya bildir,
  öldürecek bir şey yok.
- **`Operation not permitted` / izin reddedildi:** Süreç başka bir kullanıcıya
  (ya da root'a) ait olabilir; `sudo` gerekebilir ama **otomatik sudo çalıştırma**
  — kullanıcıya durumu söyle, kararı ona bırak.
- **`lsof: command not found` (Linux):** `fuser -k <port>/tcp` dene ya da
  `sudo apt install lsof`.
- **Birden fazla süreç aynı portta:** `xargs kill` hepsini hedefler; kullanıcı
  yalnız birini istiyorsa ilgili PID'i tek tek ver.

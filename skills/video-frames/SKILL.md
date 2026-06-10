---
name: video-frames
version: 0.1.0
description: Bir videoyu tek tek kare (PNG/JPG) görsellere ayırır.
icon: "🎬"
example_prompt: "video.mp4'ü saniyede 1 kare olacak şekilde karelerine ayır"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ffmpeg]
  internet: false
tags: [media, video, frames, image, file]
---

# Video Frames Skill

Bir videoyu kare kare görsellere ayırır. `ffmpeg` kullanılır. Tüm kareleri
çıkarmak çok sayıda dosya üretebilir; varsayılan olarak saniyede 1 kare önerilir.

## Çalıştırılacak komut

**Saniyede 1 kare (makul varsayılan):**

```
ffmpeg -i <video> -vf fps=1 <çıktı_dizini>/kare_%04d.png
```

`kare_%04d.png` → `kare_0001.png`, `kare_0002.png` … şeklinde numaralandırır.

**Tüm kareler (DİKKAT: yüzlerce/binlerce dosya):**

```
ffmpeg -i <video> <çıktı_dizini>/kare_%04d.png
```

**Tek bir kare (örn. 10. saniye):**

```
ffmpeg -ss 10 -i <video> -frames:v 1 <çıktı_dizini>/kare.png
```

Önce `<çıktı_dizini>`'ni oluştur: `mkdir -p <çıktı_dizini>`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Kaç kare oluştuğunu (`ls <dizin> | wc -l`) ve dosya adı desenini belirt
- Tüm kareler isteniyorsa önce dosya sayısı tahminini ver, sonra onay iste

## Hata durumları

- **`ffmpeg: command not found`:** `brew install ffmpeg` / `apt install ffmpeg`.
- **Çok fazla dosya oluştu:** `-vf fps=N` ile kare hızını düşür.
- **Çıktı dizini yok:** Önce `mkdir -p` ile oluştur.
- **Girdi okunamadı:** Video yolu/formatı hatalı.

---
name: video-to-gif
version: 0.1.0
description: Bir videoyu (veya kısmını) animasyonlu GIF'e çevirir.
icon: "🎞️"
example_prompt: "klip.mp4'ü gif yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ffmpeg]
  internet: false
tags: [media, video, gif, convert, file]
---

# Video to GIF Skill

Bir videoyu animasyonlu GIF'e çevirir. `ffmpeg` kullanılır; fps ve genişlik
düşürülerek dosya boyutu makul tutulur.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
ffmpeg -i <video> -vf "fps=10,scale=480:-1:flags=lanczos" <çıktı.gif>
```

- `fps=10` — saniyedeki kare (düşük = küçük dosya)
- `scale=480:-1` — genişlik 480px, yükseklik orantılı

**Belirli bir aralık için** (örn. 5. saniyeden 3 saniye):

```
ffmpeg -ss 5 -t 3 -i <video> -vf "fps=10,scale=480:-1:flags=lanczos" <çıktı.gif>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan GIF'in yolunu ve dosya boyutunu (`ls -lh`) belirt
- Dosya büyükse `fps` veya `scale` düşürmeyi öner

## Hata durumları

- **`ffmpeg: command not found`:** macOS `brew install ffmpeg`, Linux
  `sudo apt install ffmpeg`.
- **GIF çok büyük:** `fps` ve `scale` değerlerini düşür.
- **Girdi okunamadı:** Video yolu/formatı hatalı veya bozuk.

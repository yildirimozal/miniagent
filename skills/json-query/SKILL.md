---
name: json-query
version: 0.1.0
description: Bir JSON dosyasından jq ile değer çeker, filtreler veya dönüştürür.
icon: "🔍"
example_prompt: "data.json'daki kullanıcıların e-postalarını listele"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [jq]
  internet: false
tags: [json, query, jq, data, dev]
---

# JSON Query Skill

Bir JSON dosyasından `jq` ile belirli değerleri çeker, filtreler veya yeniden
şekillendirir — API yanıtlarıyla ve yapılandırma dosyalarıyla çalışmanın hızlı
yolu. (Tüm dosyayı güzel formatlamak için `json-format`'ı kullan; bu skill
**sorgulama** içindir.)

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
jq '<filtre>' <dosya.json>
```

Sık kullanılan filtreler:
- `.key` — bir alanı al (`jq '.name' f.json`)
- `.a.b.c` — iç içe alan
- `.items[0]` — dizinin ilk elemanı; `.items[]` — tüm elemanlar
- `.users[].email` — her objeden bir alan
- `keys` — objenin anahtarları; `length` — eleman sayısı
- `.items[] | select(.active == true)` — koşullu filtre
- `.items | map(.price) | add` — dönüştür + topla
- `-r` bayrağı: çıktıyı tırnak işaretsiz **ham** metin verir (liste üretirken faydalı)

**Kullanıcı JSON metnini yapıştırdıysa** (dosya değil): shell tırnak sorunlarını
önlemek için metni geçici bir dosyaya kaydetmesini iste (örn. `~/in.json`),
sonra yukarıdaki komutu o dosyayla çalıştır.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- İstenen değer(ler)i net göster; liste uzunsa sayısını da belirt
- `jq` çıktısı zaten okunaklıdır; ham metin için `-r` kullanıldığını not edebilirsin
- Hangi filtrenin uygulandığını kısaca açıkla (kullanıcı öğrensin)

## Hata durumları

- **`jq: command not found`:** macOS `brew install jq`, Linux `sudo apt install jq`.
- **`jq: error ... Cannot index ...`:** Filtre veri yapısıyla uyuşmuyor (örn.
  diziye `.key` uyguladın); önce `jq 'keys'` veya `jq 'type'` ile yapıyı incele.
- **`parse error`:** Dosya geçerli JSON değil; `json-format` ile doğrula.
- **Boş/`null` çıktı:** Alan yok; yazımı ve yolu (`.a.b`) kontrol et, `jq 'keys'`
  ile mevcut anahtarlara bak.

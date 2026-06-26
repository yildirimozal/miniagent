---
name: csv-stats
version: 0.1.0
description: Bir CSV dosyasındaki sayısal sütunun istatistiğini hesaplar (sayı, toplam, ortalama, min, max).
icon: "📊"
example_prompt: "satislar.csv'nin 3. sütununun ortalaması ne?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [awk]
  internet: false
tags: [csv, data, stats, analysis]
---

# CSV Stats Skill

Bir CSV dosyasındaki sayısal bir sütunun temel istatistiklerini hesaplar:
kayıt sayısı, toplam, ortalama, en küçük, en büyük. Excel açmadan hızlı analiz.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır (`<N>` = sütun numarası, başlık satırı atlanır):

```
awk -F, 'NR>1 && $<N>!="" {n++; s+=$<N>; if(min==""||$<N>+0<min)min=$<N>; if($<N>+0>max)max=$<N>} END{if(n>0) printf "sayı=%d toplam=%g ortalama=%.4g min=%g max=%g\n", n, s, s/n, min, max; else print "sayısal veri yok"}' <dosya.csv>
```

- `-F,` ayraç virgül; tab için `-F'\t'`, noktalı virgül için `-F';'`
- `NR>1` başlık satırını atlar (başlık yoksa kaldır)
- `$<N>` yerine gerçek sütun numarasını yaz (örn. `$3`)

**Sütun adından numara bulmak için** önce başlığı gör: `head -1 <dosya.csv>`.

## Sonuç işleme

`bash` tool'undan gelen sonucu kullanıcıya **doğal Türkçe** ile aktar:
- Sayı / toplam / ortalama / min / max'ı düzenli sun
- Hangi sütunun analiz edildiğini belirt
- Sütunda sayısal olmayan değerler varsa (boş/metin) atlandığını not et

## Hata durumları

- **`sayısal veri yok` / hepsi 0:** Yanlış sütun numarası ya da sütun metin
  içeriyor olabilir; `head -1` ile başlığı, birkaç satırı kontrol et.
- **Ayraç yanlış:** Değerler tek sütunmuş gibi geliyorsa `-F` ayracını düzelt
  (`,` / `;` / tab).
- **Dosya bulunamadı:** Yolu teyit et.
- **Alıntılı virgüllü değerler:** Hücre içinde virgül varsa `-F,` yanlış böler;
  bu durumda Python `csv` modülü gerekir (kullanıcıya bildir).

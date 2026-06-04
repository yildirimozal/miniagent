# 🧩 Skill Kataloğu

Mini Agent'ın sahip olduğu tüm skill'lerin kapsamlı listesi.

Her skill, `skills/` dizini altında kendi klasöründe yer alır ve [Ajanox Skill Spec v1.0](https://github.com/yildirimozal/miniagent) uyumlu bir `SKILL.md` dosyası içerir. Agent çalıştığında bu dosyalar otomatik olarak taranır ve sisteme yüklenir.

> **Toplam: 37 skill** · 8 kategori

---

## 📊 Kategoriye Göre Dağılım

| Kategori | Adet | Açıklama |
|---|:---:|---|
| [🖥️ Sistem & Donanım](#%EF%B8%8F-sistem--donanım) | 7 | OS, CPU, RAM, disk, pil, ekran bilgisi |
| [📂 Dosya İşlemleri](#-dosya-i̇şlemleri) | 7 | Dosya arama, oluşturma, arşiv, hash, metadata |
| [🌐 Ağ & İnternet](#-ağ--i̇nternet) | 7 | DNS, WHOIS, HTTP, TLS, hava durumu |
| [🔧 Geliştirici Araçları](#-geliştirici-araçları) | 7 | Encoding, UUID, JSON, CSV, kod temizleme |
| [🔀 Git İşlemleri](#-git-i̇şlemleri) | 3 | Log, status, diff |
| [📝 Metin İşleme](#-metin-i̇şleme) | 3 | Satır/kelime sayımı, slugify |
| [⏰ Tarih & Zaman](#-tarih--zaman) | 2 | Tarih aritmetiği, zaman dilimi dönüşümü |
| [🧪 Meta / Diğer](#-meta--diğer) | 1 | Skill iskeleti oluşturma |

---

## 🖥️ Sistem & Donanım

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🖥️ | [`system-info`](skills/system-info/SKILL.md) | Makine hakkında detaylı sistem bilgisi verir (OS, CPU, RAM, disk). | *"Sistemim hakkında bilgi ver"* |
| 🧮 | [`cpu-stats`](skills/cpu-stats/SKILL.md) | Sistemin yük ortalamasını (load average) ve uptime'ı gösterir. | *"Sistemin yükü ne durumda?"* |
| 🔋 | [`battery`](skills/battery/SKILL.md) | Pil durumunu (şarj %'si, AC bağlı mı, kalan süre) gösterir. | *"Pil yüzdem ne?"* |
| 💾 | [`disk-usage`](skills/disk-usage/SKILL.md) | Tüm filesystem'ların disk kullanım özetini gösterir. | *"Diskimde ne kadar boş alan var?"* |
| ⚡ | [`process-top`](skills/process-top/SKILL.md) | CPU veya belleğe göre en aktif süreçleri listeler. | *"En çok CPU kullanan süreçler?"* |
| 🖥️ | [`screen-info`](skills/screen-info/SKILL.md) | Bağlı ekranların çözünürlük, refresh rate ve renk derinliği bilgisi. | *"Ekranımın çözünürlüğü ne?"* |
| 🔔 | [`mac-notification`](skills/mac-notification/SKILL.md) | macOS'ta masaüstü bildirimi gösterir. Sadece Mac'te çalışır. | *"Bana 'mola zamanı' diye bildirim gönder"* |

---

## 📂 Dosya İşlemleri

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📁 | [`find-large-files`](skills/find-large-files/SKILL.md) | Bir klasördeki en büyük dosyaları/alt klasörleri bulur. | *"İndirilenler'de en büyük dosyalar neler?"* |
| 🔍 | [`file-find`](skills/file-find/SKILL.md) | Belirtilen dizinde isim/desen ile dosya veya klasör arar. | *"~/Desktop'ta 'rapor' içeren dosyaları bul"* |
| 📝 | [`file-create`](skills/file-create/SKILL.md) | Yeni dosya oluşturur; uzantıya göre boilerplate template uygular. | *"~/Desktop/script.py adlı Python dosyası oluştur"* |
| 📦 | [`archive-list`](skills/archive-list/SKILL.md) | Bir zip/tar/tar.gz arşivinin içeriğini listeler (çıkarmadan). | *"Bu zip'in içinde neler var?"* |
| 🔒 | [`hash-file`](skills/hash-file/SKILL.md) | Bir dosyanın sha256 veya md5 checksum'unu hesaplar. | *"installer.dmg'in sha256 hash'i ne?"* |
| 🖼️ | [`image-info`](skills/image-info/SKILL.md) | Bir görsel dosyanın boyut, format ve metadata bilgisini gösterir. | *"foto.jpg'in çözünürlüğü ne?"* |
| 📄 | [`pdf-text`](skills/pdf-text/SKILL.md) | Bir PDF dosyasından düz metni çıkarır. | *"Şu PDF'in metnini çıkar: rapor.pdf"* |

---

## 🌐 Ağ & İnternet

> ℹ️ Bu kategorideki skill'lerin çoğu **internet bağlantısı** gerektirir.

| İkon | Skill | Açıklama | Örnek Prompt | İnternet |
|:---:|---|---|---|:---:|
| 🌤️ | [`weather`](skills/weather/SKILL.md) | Bir şehrin güncel hava durumunu söyler. | *"İstanbul'da hava nasıl?"* | ✅ |
| 🌐 | [`dns-lookup`](skills/dns-lookup/SKILL.md) | Bir domain için DNS sorgusu çalıştırır (A, MX, TXT vb.). | *"anthropic.com'un DNS A kayıtları?"* | ✅ |
| 🌍 | [`ip-location`](skills/ip-location/SKILL.md) | Public IP adresini ve coğrafi konum bilgisini gösterir. | *"IP adresim nerede görünüyor?"* | ✅ |
| 📡 | [`http-headers`](skills/http-headers/SKILL.md) | Bir URL'ye HEAD isteği atıp HTTP yanıt başlıklarını gösterir. | *"github.com'un HTTP header'ları?"* | ✅ |
| 🔐 | [`cert-info`](skills/cert-info/SKILL.md) | Bir HTTPS domain'inin TLS sertifika bilgilerini gösterir. | *"github.com sertifikası ne zaman bitiyor?"* | ✅ |
| 🔎 | [`whois`](skills/whois/SKILL.md) | Bir domain için WHOIS kayıt bilgisini getirir. | *"anthropic.com'un WHOIS bilgisi?"* | ✅ |
| 🔌 | [`open-ports`](skills/open-ports/SKILL.md) | Makinedeki açık portları ve dinleyen süreçleri listeler. | *"Hangi portlar açık?"* | ❌ |
| 🔌 | [`network-interfaces`](skills/network-interfaces/SKILL.md) | Yerel ağ arabirimlerini ve IP adreslerini listeler. | *"Hangi network interface'lere bağlıyım?"* | ❌ |

---

## 🔧 Geliştirici Araçları

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🔁 | [`base64-codec`](skills/base64-codec/SKILL.md) | Metni veya dosyayı base64 ile encode/decode eder. | *"Bu base64'ü çöz: SGVsbG8="* |
| 🔣 | [`url-codec`](skills/url-codec/SKILL.md) | Metni URL-encode veya URL-decode eder. | *"Şu metni URL encode et: hello world"* |
| 🆔 | [`uuid-gen`](skills/uuid-gen/SKILL.md) | Rastgele UUID (v4) üretir. | *"Bana 3 tane UUID üret"* |
| 📑 | [`json-format`](skills/json-format/SKILL.md) | JSON verisini düzgün biçimlendirir (pretty print). | *"Şu JSON'u formatla: {…}"* |
| 📑 | [`csv-preview`](skills/csv-preview/SKILL.md) | Bir CSV dosyasının ilk N satırını sütun hizalı gösterir. | *"data.csv'nin ilk 10 satırı"* |
| 🧹 | [`code-cleaner`](skills/code-cleaner/SKILL.md) | Kod dosyalarını analiz eder, eksik docstring ekler, import temizler. | *"Şu klasördeki kodları temizle"* |
| 🪄 | [`skill-create`](skills/skill-create/SKILL.md) | Yeni bir Ajanox-uyumlu skill iskeleti oluşturur. | *"weather adlı yeni skill iskeleti oluştur"* |

---

## 🔀 Git İşlemleri

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🌳 | [`git-log`](skills/git-log/SKILL.md) | Bir Git reposundaki son commit'leri özetler. | *"Bu repoda son commit'ler neler?"* |
| 📋 | [`git-status`](skills/git-status/SKILL.md) | Çalışma ağacının kısa durumunu ve branch bilgisini gösterir. | *"Bu repoda neler değişmiş?"* |
| 🔀 | [`git-diff`](skills/git-diff/SKILL.md) | Working tree veya staged değişiklikleri gösterir. | *"Staged olmayan değişiklikleri göster"* |

---

## 📝 Metin İşleme

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📏 | [`wc-stats`](skills/wc-stats/SKILL.md) | Bir dosyanın satır, kelime ve karakter sayısını verir. | *"notes.md kaç satır?"* |
| 🔗 | [`slugify`](skills/slugify/SKILL.md) | Bir metni URL-uyumlu slug haline getirir. | *"'Merhaba Dünya!' başlığını slug yap"* |
| — | [`my-skill`](skills/my-skill/SKILL.md) | Şablon skill (boş iskelet — özelleştirme için). | — |

---

## ⏰ Tarih & Zaman

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📅 | [`date-calc`](skills/date-calc/SKILL.md) | Tarih aritmetiği yapar (N gün/ay sonra/önce hangi tarih). | *"Bugünden 90 gün sonra hangi tarih?"* |
| 🌍 | [`timezone-convert`](skills/timezone-convert/SKILL.md) | Zamanı farklı zaman dilimleri arasında çevirir. | *"İstanbul'da 15:00, New York'ta kaç?"* |

---

## 📋 İzin Matrisi

Her skill, `SKILL.md` frontmatter'ında hangi izinleri gerektirdiğini belirtir:

| İzin | Adet | Açıklama |
|---|:---:|---|
| `shell_safe` | 37 | Güvenli shell komutu çalıştırır (tüm skill'ler) |
| `file_read` | 12 | Dosya okuma erişimi gerektirir |
| `network_read` | 6 | İnternet bağlantısı gerektirir |
| `system_info` | 2 | Sistem bilgisi erişimi |
| `file_write` | 2 | Dosya yazma erişimi (`file-create`, `skill-create`) |
| `notification` | 1 | Bildirim gönderme (`mac-notification`) |

---

## 🔗 Harici Bağımlılıklar

Çoğu skill yalnızca standart sistem araçlarını kullanır. Aşağıdaki tabloda özel kurulum gerektirebilecek bağımlılıklar listelenmiştir:

| Bağımlılık | Kullanan Skill'ler | Kurulum |
|---|---|---|
| `python3` | `url-codec`, `json-format`, `slugify` | Çoğu sistemde yüklü |
| `curl` | `weather` | Çoğu sistemde yüklü |
| `pdftotext` | `pdf-text` | `brew install poppler` |
| `osascript` | `mac-notification` | macOS'ta yerleşik |
| `system_profiler` | `screen-info` | macOS'ta yerleşik |
| `uuidgen` | `uuid-gen` | Çoğu sistemde yüklü |
| `ifconfig` | `network-interfaces` | Çoğu sistemde yüklü |
| `whois` | `whois` | `brew install whois` |

---

## 🚀 Yeni Skill Ekleme

Kendi skill'ini eklemek için:

1. `skill-create` skill'ini kullanarak iskelet oluştur:
   ```
   Sen: "deploy-check adlı yeni bir skill oluştur"
   ```
2. Ya da manuel olarak `skills/<skill-adı>/SKILL.md` dosyası oluştur
3. Frontmatter'da `name` ve `description` alanlarını doldur
4. Agent'ı yeniden başlat — skill otomatik olarak kataloglanacak

Detaylı format için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

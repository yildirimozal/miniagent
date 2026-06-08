# 🧩 Skill Kataloğu

Mini Agent'ın sahip olduğu tüm skill'lerin kapsamlı listesi.

Her skill, `skills/` dizini altında kendi klasöründe yer alır ve [Ajanox Skill Spec v1.0](https://github.com/yildirimozal/miniagent) uyumlu bir `SKILL.md` dosyası içerir. Agent çalıştığında bu dosyalar otomatik olarak taranır ve sisteme yüklenir.

> **Toplam: 60 skill** · 9 kategori

---

## 📊 Kategoriye Göre Dağılım

| Kategori | Adet | Açıklama |
|---|:---:|---|
| [🖥️ Sistem & Donanım](#%EF%B8%8F-sistem--donanım) | 9 | OS, CPU, RAM, disk, pil, ekran, Docker, bildirim |
| [📂 Dosya İşlemleri](#-dosya-i̇şlemleri) | 9 | Arama, oluşturma, karşılaştırma, arşiv, hash, metadata |
| [🌐 Ağ & İnternet](#-ağ--i̇nternet) | 10 | DNS, WHOIS, HTTP, TLS, ping, IP, portlar |
| [🔧 Geliştirici Araçları](#-geliştirici-araçları) | 11 | Encoding, UUID, şifre, hash, JWT, regex, cron |
| [🗂️ Veri & Format](#%EF%B8%8F-veri--format) | 8 | JSON, CSV, YAML, XML, SQL, TS dönüşümleri |
| [🔀 Git İşlemleri](#-git-i̇şlemleri) | 6 | Log, status, diff, branch, conflict, gitignore |
| [📝 Metin İşleme](#-metin-i̇şleme) | 3 | Satır/kelime sayımı, slugify, bul-değiştir |
| [⏰ Tarih & Zaman](#-tarih--zaman) | 2 | Tarih aritmetiği, zaman dilimi dönüşümü |
| [🧪 Meta / Diğer](#-meta--diğer) | 2 | Skill iskeleti, şablon |

---

## 🖥️ Sistem & Donanım

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🖥️ | [`system-info`](skills/system-info/SKILL.md) | Makine hakkında detaylı sistem bilgisi verir (OS, CPU, RAM, disk). | *"Sistemim hakkında bilgi ver"* |
| 🧮 | [`cpu-stats`](skills/cpu-stats/SKILL.md) | Sistemin yük ortalamasını (load average) ve uptime'ı gösterir. | *"Sistemin yükü ne durumda?"* |
| 🧠 | [`memory-usage`](skills/memory-usage/SKILL.md) | Sistemin RAM kullanım detayını gösterir (toplam, kullanılan, boş). | *"RAM'im ne durumda?"* |
| 🔋 | [`battery`](skills/battery/SKILL.md) | Pil durumunu (şarj %'si, AC bağlı mı, kalan süre) gösterir. | *"Pil yüzdem ne?"* |
| 💾 | [`disk-usage`](skills/disk-usage/SKILL.md) | Tüm filesystem'ların disk kullanım özetini gösterir. | *"Diskimde ne kadar boş alan var?"* |
| ⚡ | [`process-top`](skills/process-top/SKILL.md) | CPU veya belleğe göre en aktif süreçleri listeler. | *"En çok CPU kullanan süreçler?"* |
| 🖥️ | [`screen-info`](skills/screen-info/SKILL.md) | Bağlı ekranların çözünürlük, refresh rate ve renk derinliği bilgisi. | *"Ekranımın çözünürlüğü ne?"* |
| 🐳 | [`docker-stats`](skills/docker-stats/SKILL.md) | Çalışan Docker konteynerlerinin kaynak kullanımını gösterir. | *"Hangi docker konteynerleri ne kadar RAM yiyor?"* |
| 🔔 | [`mac-notification`](skills/mac-notification/SKILL.md) | macOS'ta masaüstü bildirimi gösterir. Sadece Mac'te çalışır. | *"Bana 'mola zamanı' diye bildirim gönder"* |

---

## 📂 Dosya İşlemleri

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📁 | [`find-large-files`](skills/find-large-files/SKILL.md) | Bir klasördeki en büyük dosyaları/alt klasörleri bulur. | *"İndirilenler'de en büyük dosyalar neler?"* |
| 🔍 | [`file-find`](skills/file-find/SKILL.md) | Belirtilen dizinde isim/desen ile dosya veya klasör arar. | *"~/Desktop'ta 'rapor' içeren dosyaları bul"* |
| 📝 | [`file-create`](skills/file-create/SKILL.md) | Yeni dosya oluşturur; uzantıya göre boilerplate template uygular. | *"~/Desktop/script.py adlı Python dosyası oluştur"* |
| ⚖️ | [`file-compare`](skills/file-compare/SKILL.md) | İki dosyayı karşılaştırıp aralarındaki farkları gösterir (diff). | *"config.txt ile config.bak farkları?"* |
| 📦 | [`archive-list`](skills/archive-list/SKILL.md) | Bir zip/tar/tar.gz arşivinin içeriğini listeler (çıkarmadan). | *"Bu zip'in içinde neler var?"* |
| 📦 | [`archive-create`](skills/archive-create/SKILL.md) | Dosya veya klasörlerden zip ya da tar.gz arşivi oluşturur. | *"~/Desktop/proje klasörünü zip'le"* |
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
| 📶 | [`ping`](skills/ping/SKILL.md) | Bir host'a ping atarak erişilebilirliği ve gecikmeyi ölçer. | *"google.com'a ping at"* | ✅ |
| 🩺 | [`api-health-check`](skills/api-health-check/SKILL.md) | Bir API/web adresine istek atıp HTTP durumunu ve gecikmeyi ölçer. | *"API ayakta mı: https://api.github.com"* | ✅ |
| 🔌 | [`open-ports`](skills/open-ports/SKILL.md) | Makinedeki açık portları ve dinleyen süreçleri listeler. | *"Hangi portlar açık?"* | ❌ |
| 🔌 | [`network-interfaces`](skills/network-interfaces/SKILL.md) | Yerel ağ arabirimlerini ve IP adreslerini listeler. | *"Hangi network interface'lere bağlıyım?"* | ❌ |

---

## 🔧 Geliştirici Araçları

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🔁 | [`base64-codec`](skills/base64-codec/SKILL.md) | Metni veya dosyayı base64 ile encode/decode eder. | *"Bu base64'ü çöz: SGVsbG8="* |
| 🔣 | [`url-codec`](skills/url-codec/SKILL.md) | Metni URL-encode veya URL-decode eder. | *"Şu metni URL encode et: hello world"* |
| 🆔 | [`uuid-gen`](skills/uuid-gen/SKILL.md) | Rastgele UUID (v4) üretir. | *"Bana 3 tane UUID üret"* |
| 🔑 | [`password-gen`](skills/password-gen/SKILL.md) | Rastgele güçlü şifre oluşturur. | *"16 karakterli güvenli bir şifre oluştur"* |
| 🔐 | [`bcrypt-gen`](skills/bcrypt-gen/SKILL.md) | Verilen düz metni (şifreyi) bcrypt algoritması ile hashler. | *"Şu şifre için bcrypt hash: gizli123"* |
| 🗝️ | [`rsa-keypair-gen`](skills/rsa-keypair-gen/SKILL.md) | Test amaçlı RSA public/private anahtar çifti oluşturur. | *"Bana bir RSA anahtar çifti oluştur"* |
| 🎫 | [`jwt-decode`](skills/jwt-decode/SKILL.md) | JWT (JSON Web Token) içeriğini çözümler ve gösterir. | *"Şu JWT'yi decode et: eyJhbG..."* |
| 🔍 | [`regex-tester`](skills/regex-tester/SKILL.md) | Verilen metin üzerinde regex eşleşmelerini test eder. | *"Şu metinde e-posta adreslerini bul"* |
| ⏱️ | [`cron-explain`](skills/cron-explain/SKILL.md) | Bir cron ifadesini okunabilir Türkçe açıklamaya çevirir. | *"`*/5 * * * *` ne anlama geliyor?"* |
| 🌐 | [`curl-to-fetch`](skills/curl-to-fetch/SKILL.md) | cURL komutunu JavaScript `fetch()` koduna çevirir. | *"Şu cURL'i fetch yap: curl -X POST ..."* |
| 🧹 | [`code-cleaner`](skills/code-cleaner/SKILL.md) | Kod dosyalarını analiz eder, eksik docstring ekler, import temizler. | *"Şu klasördeki kodları temizle"* |

---

## 🗂️ Veri & Format

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🧾 | [`json-format`](skills/json-format/SKILL.md) | JSON verisini düzgün biçimlendirir (pretty print) ve doğrular. | *"Şu config.json'u formatla"* |
| 📑 | [`csv-preview`](skills/csv-preview/SKILL.md) | Bir CSV dosyasının ilk N satırını sütun hizalı gösterir. | *"data.csv'nin ilk 10 satırı"* |
| 🔄 | [`json-to-csv`](skills/json-to-csv/SKILL.md) | JSON verisini CSV formatına dönüştürür veya tersini yapar. | *"data.json'u CSV'ye çevir"* |
| 📘 | [`json-to-ts`](skills/json-to-ts/SKILL.md) | Bir JSON objesinden TypeScript Interface oluşturur. | *"Şu JSON'dan TS interface yap"* |
| 🔄 | [`yaml-to-json`](skills/yaml-to-json/SKILL.md) | YAML formatındaki metni JSON formatına çevirir. | *"Bu YAML'ı JSON yap"* |
| ⚙️ | [`env-to-json`](skills/env-to-json/SKILL.md) | `.env` formatındaki key-value çiftlerini JSON'a çevirir. | *"Bu env değişkenlerini JSON'a çevir"* |
| 📝 | [`xml-format`](skills/xml-format/SKILL.md) | Sıkışık XML/HTML metnini girintili ve okunabilir hale getirir. | *"Şu XML'i düzelt: `<root>...`"* |
| 🗄️ | [`sql-format`](skills/sql-format/SKILL.md) | Tek satırlık/karmaşık SQL sorgularını okunabilir biçime getirir. | *"Şu SQL'i formatla: SELECT ..."* |

---

## 🔀 Git İşlemleri

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🌳 | [`git-log`](skills/git-log/SKILL.md) | Bir Git reposundaki son commit'leri özetler. | *"Bu repoda son commit'ler neler?"* |
| 📋 | [`git-status`](skills/git-status/SKILL.md) | Çalışma ağacının kısa durumunu ve branch bilgisini gösterir. | *"Bu repoda neler değişmiş?"* |
| 🔀 | [`git-diff`](skills/git-diff/SKILL.md) | Working tree veya staged değişiklikleri gösterir. | *"Staged olmayan değişiklikleri göster"* |
| 🌿 | [`git-branch`](skills/git-branch/SKILL.md) | Repodaki branch'leri listeler ve aktif branch'i gösterir. | *"Bu repodaki branch'ler neler?"* |
| ⚔️ | [`git-conflict-finder`](skills/git-conflict-finder/SKILL.md) | Çözülmemiş Git conflict (çakışma) noktalarını bulur. | *"Projede çözülmemiş conflict var mı?"* |
| 🙈 | [`git-ignore-gen`](skills/git-ignore-gen/SKILL.md) | Belirtilen teknolojiler için hazır `.gitignore` şablonu oluşturur. | *"Node, Python ve macOS için gitignore"* |

---

## 📝 Metin İşleme

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📏 | [`wc-stats`](skills/wc-stats/SKILL.md) | Bir dosyanın satır, kelime ve karakter sayısını verir. | *"notes.md kaç satır?"* |
| 🔗 | [`slugify`](skills/slugify/SKILL.md) | Bir metni URL-uyumlu slug haline getirir. | *"'Merhaba Dünya!' başlığını slug yap"* |
| 🔤 | [`text-replace`](skills/text-replace/SKILL.md) | Bir dosyadaki belirli bir metni bulup başkasıyla değiştirir. | *"config.txt'te 'localhost' → '192.168.1.1'"* |

---

## ⏰ Tarih & Zaman

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📅 | [`date-calc`](skills/date-calc/SKILL.md) | Tarih aritmetiği yapar (N gün/ay sonra/önce hangi tarih). | *"Bugünden 90 gün sonra hangi tarih?"* |
| 🌍 | [`timezone-convert`](skills/timezone-convert/SKILL.md) | Zamanı farklı zaman dilimleri arasında çevirir. | *"İstanbul'da 15:00, New York'ta kaç?"* |

---

## 🧪 Meta / Diğer

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🪄 | [`skill-create`](skills/skill-create/SKILL.md) | Yeni bir Ajanox-uyumlu skill iskeleti oluşturur. | *"weather adlı yeni skill iskeleti oluştur"* |
| — | [`my-skill`](skills/my-skill/SKILL.md) | Şablon skill (boş iskelet — özelleştirme için). | — |

---

## 📋 İzin Matrisi

Her skill, `SKILL.md` frontmatter'ında hangi izinleri gerektirdiğini belirtir. Aşağıda Ajanox Skill Spec v1.0'ın **standart izinleri** ve katalogdaki kullanım sayıları yer alır:

| İzin | Adet | Açıklama |
|---|:---:|---|
| `shell_safe` | 60 | Güvenli shell komutu çalıştırır (tüm skill'ler) |
| `file_read` | 17 | Dosya okuma erişimi gerektirir |
| `network_read` | 7 | İnternet bağlantısı gerektirir |
| `file_write` | 4 | Dosya yazma erişimi (`archive-create`, `file-create`, `skill-create`, `text-replace`) |
| `system_info` | 3 | Sistem bilgisi erişimi (`memory-usage`, `open-ports`, `system-info`) |
| `notification` | 1 | Bildirim gönderme (`mac-notification`) |

> ⚠️ **Not:** Son eklenen bazı skill'ler standart dışı ikinci bir izin etiketi (örn. `bcrypt_gen`, `jwt_decode`) taşıyor; bunlar spec'in 14 geçerli izninden birine (genelde `shell_safe` yeterli, ağ kullananlar için `network_read`) göçürülmeli. Detay için aşağıdaki bağımlılık tablosu ve `CONTRIBUTING.md`.

---

## 🔗 Harici Bağımlılıklar

Çoğu skill yalnızca standart sistem araçlarını kullanır. Aşağıdaki tabloda özel kurulum gerektirebilecek bağımlılıklar listelenmiştir:

| Bağımlılık | Kullanan Skill'ler (örnek) | Kurulum |
|---|---|---|
| `python3` | `json-format`, `slugify`, `url-codec`, `regex-tester`, `json-to-ts` … | Çoğu sistemde yüklü |
| `curl` | `weather`, `api-health-check`, `git-ignore-gen`, `http-headers` | Çoğu sistemde yüklü |
| `openssl` | `cert-info`, `rsa-keypair-gen`, `bcrypt-gen` | Çoğu sistemde yüklü |
| `dig` | `dns-lookup` | `bind`/`dnsutils` |
| `docker` | `docker-stats` | [docker.com](https://docs.docker.com/get-docker/) |
| `pdftotext` | `pdf-text` | `brew install poppler` |
| `whois` | `whois` | `brew install whois` |
| `osascript` | `mac-notification` | macOS'ta yerleşik |
| `system_profiler` | `screen-info` | macOS'ta yerleşik |

---

## 🚀 Yeni Skill Ekleme

Kendi skill'ini eklemek için:

1. `skill-create` skill'ini kullanarak iskelet oluştur:
   ```
   Sen: "deploy-check adlı yeni bir skill oluştur"
   ```
2. Ya da manuel olarak `skills/<skill-adı>/SKILL.md` dosyası oluştur.
3. Frontmatter'da zorunlu alanları doldur: `name`, `version`, `description`, `ajanox`, `permissions` (spec'in 14 geçerli izninden seç — `sudo` yasak).
4. Göndermeden önce spec uyumunu doğrula: `ajanox skill check skills/<skill-adı>`.
5. Agent'ı yeniden başlat — skill otomatik olarak kataloglanacak.

Detaylı format için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

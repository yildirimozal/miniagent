# 🧩 Skill Kataloğu

Mini Agent'ın sahip olduğu tüm skill'lerin kapsamlı listesi.

Her skill, `skills/` dizini altında kendi klasöründe yer alır ve [Ajanox Skill Spec v1.0](https://github.com/yildirimozal/miniagent) uyumlu bir `SKILL.md` dosyası içerir. Agent çalıştığında bu dosyalar otomatik olarak taranır ve sisteme yüklenir.

> **Toplam: 113 skill** · 12 kategori

---

## 📊 Kategoriye Göre Dağılım

| Kategori | Adet | Açıklama |
|---|:---:|---|
| [🖥️ Sistem & Donanım](#%EF%B8%8F-sistem--donanım) | 10 | OS, CPU, RAM, disk, pil, ekran, Docker, bildirim, uyku engelleme |
| [📂 Dosya İşlemleri](#-dosya-i̇şlemleri) | 12 | Arama, oluşturma, karşılaştırma, arşiv, hash, metadata, ağaç, kopya, tür tespiti |
| [🌐 Ağ & İnternet](#-ağ--i̇nternet) | 14 | DNS, WHOIS, HTTP, TLS, ping, IP, portlar, port kapatma/test, DNS, URL çözme |
| [🔧 Geliştirici Araçları](#-geliştirici-araçları) | 11 | Encoding, UUID, şifre, hash, JWT, regex, cron |
| [🗂️ Veri & Format](#%EF%B8%8F-veri--format) | 10 | JSON, CSV, YAML, XML, SQL, TS, jq sorgu, CSV istatistik |
| [📑 Ofis / Belge](#-ofis--belge) | 9 | LibreOffice: PDF, format dönüşümü, metin, görsel, epub |
| [🎬 Medya](#-medya) | 9 | Görsel/video: boyut, format, sıkıştırma, GIF, kare, ses |
| [🔐 Güvenlik & Şifreleme](#-güvenlik--şifreleme) | 9 | GPG/age, SSH/TOTP, parola, checksum, EXIF temizleme, maskeleme |
| [🔀 Git İşlemleri](#-git-i̇şlemleri) | 16 | Log, status, diff, branch, conflict, güvenlik, gitignore, blame, search, stash, tag, undo, cleanup, sync, katkıcılar, kimlik |
| [📝 Metin İşleme](#-metin-i̇şleme) | 7 | Sayım, slugify, bul-değiştir, sırala, tekilleştir, harf |
| [⏰ Tarih & Zaman](#-tarih--zaman) | 4 | Tarih aritmetiği, zaman dilimi, epoch, gün farkı |
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
| ☕ | [`keep-awake`](skills/keep-awake/SKILL.md) | Bilgisayarı belirli süre/komut bitene kadar uyutmaz (caffeinate). | *"bilgisayarı 1 saat uyutma"* |

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
| 🌲 | [`dir-tree`](skills/dir-tree/SKILL.md) | Bir dizinin ağaç görünümünü (alt klasör + dosya) çıkarır. | *"~/Projeler'in ağaç yapısını göster"* |
| 👯 | [`duplicate-finder`](skills/duplicate-finder/SKILL.md) | İçerikçe aynı (yinelenen) dosyaları hash'e göre bulur. | *"~/Downloads'taki kopyaları bul"* |
| 🔬 | [`file-type`](skills/file-type/SKILL.md) | Bir dosyanın gerçek türünü uzantıdan bağımsız tespit eder. | *"bu uzantısız dosya aslında ne?"* |

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
| 🔌 | [`port-check`](skills/port-check/SKILL.md) | Bir host'ta TCP portunun açık/erişilebilir olup olmadığını test eder. | *"example.com 443 portu açık mı?"* | ✅ |
| 🔗 | [`expand-url`](skills/expand-url/SKILL.md) | Kısaltılmış URL'i tıklamadan gerçek hedefine çözer. | *"şu link nereye gidiyor?"* | ✅ |
| 🔌 | [`open-ports`](skills/open-ports/SKILL.md) | Makinedeki açık portları ve dinleyen süreçleri listeler. | *"Hangi portlar açık?"* | ❌ |
| 🔌 | [`network-interfaces`](skills/network-interfaces/SKILL.md) | Yerel ağ arabirimlerini ve IP adreslerini listeler. | *"Hangi network interface'lere bağlıyım?"* | ❌ |
| 🔌 | [`kill-port`](skills/kill-port/SKILL.md) | Bir portu dinleyen süreci bulup onaylı şekilde sonlandırır. | *"3000 portunu kullanan süreci kapat"* | ❌ |
| 🌊 | [`flush-dns`](skills/flush-dns/SKILL.md) | OS/çözücüyü tespit edip DNS önbelleğini temizleme komutunu verir. | *"DNS önbelleğini temizle"* | ❌ |

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
| 🔍 | [`json-query`](skills/json-query/SKILL.md) | Bir JSON dosyasından jq ile değer çeker, filtreler, dönüştürür. | *"data.json'daki e-postaları listele"* |
| 📊 | [`csv-stats`](skills/csv-stats/SKILL.md) | Bir CSV sütununun istatistiği (sayı/toplam/ort/min/max). | *"satislar.csv 3. sütun ortalaması?"* |
| 📑 | [`csv-preview`](skills/csv-preview/SKILL.md) | Bir CSV dosyasının ilk N satırını sütun hizalı gösterir. | *"data.csv'nin ilk 10 satırı"* |
| 🔄 | [`json-to-csv`](skills/json-to-csv/SKILL.md) | JSON verisini CSV formatına dönüştürür veya tersini yapar. | *"data.json'u CSV'ye çevir"* |
| 📘 | [`json-to-ts`](skills/json-to-ts/SKILL.md) | Bir JSON objesinden TypeScript Interface oluşturur. | *"Şu JSON'dan TS interface yap"* |
| 🔄 | [`yaml-to-json`](skills/yaml-to-json/SKILL.md) | YAML formatındaki metni JSON formatına çevirir. | *"Bu YAML'ı JSON yap"* |
| ⚙️ | [`env-to-json`](skills/env-to-json/SKILL.md) | `.env` formatındaki key-value çiftlerini JSON'a çevirir. | *"Bu env değişkenlerini JSON'a çevir"* |
| 📝 | [`xml-format`](skills/xml-format/SKILL.md) | Sıkışık XML/HTML metnini girintili ve okunabilir hale getirir. | *"Şu XML'i düzelt: `<root>...`"* |
| 🗄️ | [`sql-format`](skills/sql-format/SKILL.md) | Tek satırlık/karmaşık SQL sorgularını okunabilir biçime getirir. | *"Şu SQL'i formatla: SELECT ..."* |

---

## 📑 Ofis / Belge

> ℹ️ Bu kategorideki skill'ler **LibreOffice** (`soffice`) gerektirir; bazıları ek araç (`pdftoppm`) kullanır.

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📄 | [`office-to-pdf`](skills/office-to-pdf/SKILL.md) | Ofis belgesini (docx/odt/xlsx/pptx) headless PDF'e çevirir. | *"rapor.docx dosyasını PDF yap"* |
| 📚 | [`office-batch-pdf`](skills/office-batch-pdf/SKILL.md) | Bir klasördeki tüm ofis belgelerini toplu PDF'e çevirir. | *"sunumlar klasöründekileri PDF yap"* |
| 🔄 | [`office-convert`](skills/office-convert/SKILL.md) | Formatlar arası dönüştürür (docx↔odt, xlsx↔ods, pptx↔odp). | *"rapor.docx'i odt'ye çevir"* |
| 📊 | [`spreadsheet-to-csv`](skills/spreadsheet-to-csv/SKILL.md) | Hesap tablosunu (xlsx/ods) CSV'ye çevirir. | *"veriler.xlsx'i CSV yap"* |
| 📈 | [`csv-to-xlsx`](skills/csv-to-xlsx/SKILL.md) | CSV'yi Excel (xlsx) veya Calc (ods) tablosuna çevirir. | *"veriler.csv'yi xlsx yap"* |
| 📝 | [`office-to-text`](skills/office-to-text/SKILL.md) | Ofis belgesinden (docx/odt) düz metin çıkarır. | *"rapor.docx metnini çıkar"* |
| 🌐 | [`office-to-html`](skills/office-to-html/SKILL.md) | Ofis belgesini (docx/odt) HTML'e çevirir. | *"yazi.docx'i HTML yap"* |
| 🖼️ | [`office-to-images`](skills/office-to-images/SKILL.md) | Sunum/belge sayfalarını PNG görsele çevirir. | *"sunum.pptx slaytlarını PNG yap"* |
| 📖 | [`office-to-epub`](skills/office-to-epub/SKILL.md) | Metin belgesini (odt/docx) EPUB e-kitaba çevirir. | *"kitap.odt'yi epub yap"* |

---

## 🎬 Medya

> ℹ️ Bu kategorideki skill'ler **ffmpeg** (video) veya **sips/ImageMagick** (görsel) gerektirir.

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📐 | [`image-resize`](skills/image-resize/SKILL.md) | Bir görseli belirtilen boyuta/yüzdeye yeniden boyutlandırır. | *"foto.jpg'i 800px genişliğe küçült"* |
| 🖼️ | [`image-convert`](skills/image-convert/SKILL.md) | Görseli formatlar arası çevirir (png↔jpg↔webp↔heic). | *"foto.png'i jpg yap"* |
| 🗜️ | [`image-compress`](skills/image-compress/SKILL.md) | Görselin dosya boyutunu kaliteyi ayarlayarak küçültür. | *"banner.jpg'i sıkıştır"* |
| 🎞️ | [`video-to-gif`](skills/video-to-gif/SKILL.md) | Bir videoyu (veya kısmını) animasyonlu GIF'e çevirir. | *"klip.mp4'ü gif yap"* |
| 🎬 | [`video-frames`](skills/video-frames/SKILL.md) | Bir videoyu tek tek kare (PNG/JPG) görsellere ayırır. | *"video.mp4'ü karelerine ayır"* |
| 🎵 | [`extract-audio`](skills/extract-audio/SKILL.md) | Videodan ses parçasını çıkarıp ses dosyası olarak kaydeder. | *"ders.mp4'ten sesi mp3 yap"* |
| 📉 | [`video-compress`](skills/video-compress/SKILL.md) | Videonun dosya boyutunu H.264/CRF ile küçültür. | *"büyük-video.mov'u sıkıştır"* |
| 📺 | [`video-info`](skills/video-info/SKILL.md) | Medya dosyasının süre, çözünürlük, codec bilgisini gösterir. | *"video.mp4 kaç saniye?"* |
| 📑 | [`image-to-pdf`](skills/image-to-pdf/SKILL.md) | Bir veya birden fazla görseli tek PDF'te birleştirir. | *"taramaları tek PDF yap"* |

---

## 🔐 Güvenlik & Şifreleme

> ℹ️ Bu skill'ler `gpg`, `age`, `ssh-keygen`, `oathtool` gibi araçlar gerektirir. Gizli veriyi (parola, secret) komut satırına değil, dosyaya yazıp oradan okuyun.

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🔒 | [`gpg-encrypt`](skills/gpg-encrypt/SKILL.md) | Bir dosyayı GPG ile şifreler (parola veya alıcı anahtarı). | *"gizli.pdf'i parolayla şifrele"* |
| 🔓 | [`gpg-decrypt`](skills/gpg-decrypt/SKILL.md) | GPG ile şifrelenmiş dosyayı (.gpg/.asc) çözer. | *"gizli.pdf.gpg'i çöz"* |
| 🛡️ | [`age-encrypt`](skills/age-encrypt/SKILL.md) | Dosyayı `age` ile şifreler/çözer (modern, sade). | *"notlar.txt'i age ile şifrele"* |
| 🗝️ | [`ssh-keygen`](skills/ssh-keygen/SKILL.md) | Yeni SSH anahtar çifti (ed25519/RSA) üretir. | *"github için ssh anahtarı oluştur"* |
| 🔢 | [`totp-gen`](skills/totp-gen/SKILL.md) | TOTP secret'tan anlık 2FA kodu üretir. | *"şu TOTP secret için kod üret"* |
| 💪 | [`password-strength`](skills/password-strength/SKILL.md) | Bir parolanın gücünü (entropi) kabaca değerlendirir. | *"şu parola ne kadar güçlü?"* |
| ✅ | [`verify-checksum`](skills/verify-checksum/SKILL.md) | Dosyayı beklenen sha256/md5 ile karşılaştırıp doğrular. | *"installer.dmg'in sha256'sı şu mu: ..."* |
| 📷 | [`strip-exif`](skills/strip-exif/SKILL.md) | Fotoğraftan EXIF/konum metadata'sını siler (mahremiyet). | *"foto'yu paylaşmadan konum bilgisini temizle"* |
| 🖊️ | [`redact`](skills/redact/SKILL.md) | Dosyadaki e-posta/IP/token'ları maskeleyip paylaşılabilir kopya üretir. | *"log.txt'teki mail ve IP'leri gizle"* |

---

## 🔀 Git İşlemleri

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 🌳 | [`git-log`](skills/git-log/SKILL.md) | Bir Git reposundaki son commit'leri özetler. | *"Bu repoda son commit'ler neler?"* |
| 📋 | [`git-status`](skills/git-status/SKILL.md) | Çalışma ağacının kısa durumunu ve branch bilgisini gösterir. | *"Bu repoda neler değişmiş?"* |
| 🔀 | [`git-diff`](skills/git-diff/SKILL.md) | Working tree veya staged değişiklikleri gösterir. | *"Staged olmayan değişiklikleri göster"* |
| 🌿 | [`git-branch`](skills/git-branch/SKILL.md) | Repodaki branch'leri listeler ve aktif branch'i gösterir. | *"Bu repodaki branch'ler neler?"* |
| ⚔️ | [`git-conflict-finder`](skills/git-conflict-finder/SKILL.md) | Çözülmemiş Git conflict (çakışma) noktalarını bulur. | *"Projede çözülmemiş conflict var mı?"* |
| 🛡️ | [`repo-safety-check`](skills/repo-safety-check/SKILL.md) | Commit veya PR öncesi secret sızıntısı, conflict marker, büyük dosya ve diff hijyeni kontrolü yapar. | *"Bu repoyu commit atmadan önce güvenlik açısından kontrol et"* |
| 🙈 | [`git-ignore-gen`](skills/git-ignore-gen/SKILL.md) | Belirtilen teknolojiler için hazır `.gitignore` şablonu oluşturur. | *"Node, Python ve macOS için gitignore"* |
| 👤 | [`git-blame`](skills/git-blame/SKILL.md) | Bir dosyanın her satırını kimin/hangi commit'te değiştirdiğini gösterir. | *"agent.py 50-60. satırları kim yazmış?"* |
| 🕵️ | [`git-search`](skills/git-search/SKILL.md) | Git geçmişinde kod/değişiklik/commit mesajı arar (pickaxe). | *"'API_KEY' ne zaman eklendi?"* |
| 📦 | [`git-stash`](skills/git-stash/SKILL.md) | Stash'leri (geçici kaydedilmiş değişiklikler) listeler ve gösterir. | *"bu repoda stash'te ne var?"* |
| 🏷️ | [`git-tag`](skills/git-tag/SKILL.md) | Tag'leri listeler veya yeni sürüm etiketi oluşturur. | *"bu repodaki tag'leri göster"* |
| ↩️ | [`git-undo`](skills/git-undo/SKILL.md) | Yaygın Git hatalarını (commit/add/push) güvenle geri alma rehberi. | *"son commit'i geri al, değişikliklerim kalsın"* |
| 🧹 | [`git-cleanup`](skills/git-cleanup/SKILL.md) | Merge edilmiş yerel branch'leri bulup onaylı şekilde toplu siler. | *"merge olmuş eski branch'leri temizle"* |
| 🔄 | [`git-sync`](skills/git-sync/SKILL.md) | Mevcut branch'i uzaktan güvenle günceller (fetch + fast-forward). | *"bu branch'i uzaktan güncelle"* |
| 👥 | [`git-contributors`](skills/git-contributors/SKILL.md) | Katkıcıları commit sayısına göre sıralı listeler. | *"bu repoya kim ne kadar katkı vermiş?"* |
| 🪪 | [`git-whoami`](skills/git-whoami/SKILL.md) | Bu repoda commit kimliğini (isim/e-posta) gösterir. | *"bu repoda hangi mail ile commit atıyorum?"* |

---

## 📝 Metin İşleme

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📏 | [`wc-stats`](skills/wc-stats/SKILL.md) | Bir dosyanın satır, kelime ve karakter sayısını verir. | *"notes.md kaç satır?"* |
| 🔗 | [`slugify`](skills/slugify/SKILL.md) | Bir metni URL-uyumlu slug haline getirir. | *"'Merhaba Dünya!' başlığını slug yap"* |
| 🔤 | [`text-replace`](skills/text-replace/SKILL.md) | Bir dosyadaki belirli bir metni bulup başkasıyla değiştirir. | *"config.txt'te 'localhost' → '192.168.1.1'"* |
| 🔢 | [`sort-lines`](skills/sort-lines/SKILL.md) | Bir dosyanın satırlarını sıralar (alfabetik/sayısal/ters/benzersiz). | *"liste.txt'i alfabetik sırala"* |
| ♻️ | [`dedup-lines`](skills/dedup-lines/SKILL.md) | Tekrar eden satırları kaldırır (sıra korunabilir). | *"liste.txt'teki tekrarları temizle"* |
| 🔡 | [`case-convert`](skills/case-convert/SKILL.md) | Metni büyük/küçük/başlık (Title) harfe çevirir. | *"şu metni büyük harf yap"* |
| 🔎 | [`count-occurrences`](skills/count-occurrences/SKILL.md) | Bir dosyada bir kelime/desenin kaç kez geçtiğini sayar. | *"log.txt'te 'ERROR' kaç kez geçiyor?"* |

---

## ⏰ Tarih & Zaman

| İkon | Skill | Açıklama | Örnek Prompt |
|:---:|---|---|---|
| 📅 | [`date-calc`](skills/date-calc/SKILL.md) | Tarih aritmetiği yapar (N gün/ay sonra/önce hangi tarih). | *"Bugünden 90 gün sonra hangi tarih?"* |
| 🌍 | [`timezone-convert`](skills/timezone-convert/SKILL.md) | Zamanı farklı zaman dilimleri arasında çevirir. | *"İstanbul'da 15:00, New York'ta kaç?"* |
| ⏱️ | [`epoch-convert`](skills/epoch-convert/SKILL.md) | Unix timestamp ↔ insan-okunur tarih dönüşümü. | *"1700000000 hangi tarih?"* |
| 📆 | [`days-between`](skills/days-between/SKILL.md) | İki tarih arasındaki gün sayısını hesaplar. | *"2026-01-01 ile bugün arası kaç gün?"* |

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
| `shell_safe` | 113 | Güvenli shell komutu çalıştırır (tüm skill'ler) |
| `process_control` | 1 | Süreç sonlandırma/kontrol (`kill-port`) |
| `file_read` | 54 | Dosya okuma erişimi gerektirir |
| `network_read` | 12 | İnternet bağlantısı gerektirir |
| `file_write` | 26 | Dosya yazma erişimi (dosya/arşiv/şablon + 9 LibreOffice + 8 Medya + Güvenlik skill'leri) |
| `system_info` | 3 | Sistem bilgisi erişimi (`memory-usage`, `open-ports`, `system-info`) |
| `notification` | 1 | Bildirim gönderme (`mac-notification`) |

> ✅ Tüm skill'ler Ajanox Skill Spec v1.0'ın 14 geçerli izninden birini kullanır (`sudo` ve standart dışı etiketler yoktur).

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
| `pdftoppm` | `office-to-images` | `brew install poppler` |
| `soffice` | `office-to-pdf`, `office-convert`, `spreadsheet-to-csv` … (9 Ofis skill'i) | `brew install --cask libreoffice` |
| `ffmpeg` / `ffprobe` | `video-to-gif`, `video-frames`, `extract-audio`, `video-compress`, `video-info` | `brew install ffmpeg` |
| `sips` / ImageMagick | `image-resize`, `image-convert`, `image-compress`, `image-to-pdf` | `sips` macOS'ta yerleşik; `brew install imagemagick` |
| `gpg` | `gpg-encrypt`, `gpg-decrypt` | `brew install gnupg` |
| `age` | `age-encrypt` | `brew install age` |
| `oathtool` | `totp-gen` | `brew install oath-toolkit` |
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

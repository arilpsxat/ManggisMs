# ManggisMs

ManggisMs adalah sebuah script sederhana yang di gunakan untuk bot telegram. Script ini di tulis dengan bahasa python.

## Module yang digunakan

- requests
- json
- datetime
- pytz
- re

## Mengatur token bot dan zona waktu

Ganti `BOT_TOKEN` dengan token bot teman², didalam file `main.py`. Seperti di bawah ini

```python
bot = Telegram('1234567898:AAEz2T73lm-5mOaoC1FaZ_IS0TXzaD3Pv4k', 'TIME_ZONE')
```

Kemudian, untuk `TIME_ZONE` ganti dengan zona waktu teman². Seperti di bawah ini

```python
bot = Telegram('1234567898:AAEz2T73lm-5mOaoC1FaZ_IS0TXzaD3Pv4k', 'Etc/GMT-7')
```
- `Etc/GMT-7` untuk **WIB**
- `Etc/GMT-8` untuk **WITA**
- `Etc/GMT-9` untuk **WIT**

## Memfilter pesan

Untuk memfilter pesan yang masuk, teman² bisa gunakan `bot.cektMessage()` kemudian isi argumen dengan beberapa argumen di bawah ini.

> Teman² juga bisa menggabungkan seluruh argumen yang ada di bawah ini

#### Argumen `mtext`

`mtext` di gunakan untuk mengecek pesan text yang di terima, apabila sama maka akan di terima.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mtext=['/start', '/help']):
			...
```

Kode di atas mengartikan bahwa hanya pesan `/start` dan `/help` yang akan di terima, dan diproses.

> Teman² juga bisa langsung menggunakan pola regex di isian `mtext`

#### Argumen `mfid`

`mfid` di gunakan untuk mengecek id user, apabila id user sama, maka akan diterima.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mtext=['/start'], mfid=[1234567898, 9876543212]):
			...
```

Kode di atas menunjukkan bahwa hanya pesan text `/start` yang di kirim oleh user dengan id `1234567898` dan `9876543212` saja yang akan di terima, dan di proses.

#### Argumen `mctype`

`mctype` di gunakan untuk mengecek apakah pesan yang di terima itu dari chat `private/group/supergroup/channel`.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mfid=[1234567898, 9876543212], mtext=['/start'], mctype=['group']):
			...
```

Kode di atas menunjukkan bahwa hanya pesan text `/start` yang di kirim oleh user id `1234567898` dan `9876543212` dari pesan `group` saja yang diproses, jadi apabila kedua user id itu mengirim di chat private, maka bot akan mengabaikannya.

#### Argumen `mform`

`mform` digunakan untuk mengecek apakah pesan berupa animation/video/photo/audio dll.

> Saya sarankan tidak menggunakan argumen `mtext`, apabila menggunakan `mform` dengan isian selain `text`

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mform=['photo']):
			...
```

Kode di atas menunjukkan bahwa hanya pesan berupa gambar saja yang akan diterima, dan di proses.

#### Argumen `mcapt`

`mcapt` di gunakan untuk menegecek caption yang ada pada animation, video, photo, dll. Apabila caption sama dengan isian `mcapt`, maka pesan akan di terima.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mform=['photo'], mcapt=['/convert']):
			...
```

Kode di atas menunjukkan bahwa hanya pesan berupa foto dengan caption `/convert` saja yang akan di terima, selain itu maka akan di abaikan.

> Teman² juga bisa langsung menggunakan pola regex di isian `mcapt`. Teman² juga bisa menambah isian dari `mcapt` seperti ini `mcapt=['/start', '/help']`, dan bukan hanya 2, teman² bisa tambahkan lagi sesuai kebutuhan.

#### Argumen `mctitle`

`mctitle` di gunakan untuk mengecek title sebuah group/supergroup/channel, apabila isian `mctitle` sama, maka akan di terima.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mctitle=['ManggisMs']):
			...
```

Kode di atas menunjukkan bahwa hanya menerima pesan yang chat title-nya berupa `ManggisMs`.

> Teman² juga bisa langsung menggunakan pola regex di isian `mctitle`. Dan teman² juga bisa memperbanyak isian dari `mctitle`, tapi jangan kebablasan.

#### Argumen `mfusername`

`mfusername` di gunakan untuk mengecek, apakah user menggunakan username atau tidak.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mctype=['group'], mfusername=[True]):
			...
```

> `True` untuk Benar(user memakai username)
> `False` untuk Salah(user tidak memakai username)

> Apabila teman² mengisi `mfusername` dengan `False`, maka akan berfungsi sebagai kebalikannya `True`(hanya pesan user yang tidak memakai username yang di terima, sedangakan user yang memakai username pesannya akan di abaikan.)

Kode di atas menunjukkan bahwa hanya pesan group dengan user yang memakai username saja yang di terima, sedangkan user yang tidak memakai username pesannya akan di abaikan.

#### Argumen `clock`

`clock` di gunakan untuk mengecek, apakah pesan yang di terima itu sesuai pada jam yang telah di atur, maka akan di terima.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(clock=[1, 0, 16, 38]):
			...
```

Kode di atas menunjukkan bahwa, apabila pesan yang di terima itu berada di antara jam `1:0 - 16:38` yang diterima. Mungkin teman² akan mengerti dengan melihat table di bawah ini

| Jam   | Sama Dengan |
| ----- | ----------- |
| 1, 0  | 01, 00      |
| 0, 30 | 00, 30      |
| 22, 0 | 22, 00      |

#### Argumen `day`

`day` di gunakan untuk mengecek, apakah hari di mana pesan yang di kirim itu sama dengan hari yang di isi di argumen `day`

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(day=[0, 1, 6]):
			...
```

| Number | Hari   |
| ------ | ------ |
| 0      | Ahad   |
| 1      | Senin  |
| 2      | Selasa |
| 3      | Rabu   |
| 4      | Kamis  |
| 5      | Jum'at |
| 6      | Sabtu  |

Kode di atas menunjukkan bahwa hanya pesan yang di kirim pada hari `Ahad`, `Senin` dan `Sabtu` saja yang diterima, apabila menerima pesan selain pada hari `Ahad`, `Senin` dan `Sabtu` maka pesan di abaikan.

#### Argumen `dom`

`dom` di gunakan untuk mengecek, apakah tanggal dimana pesan di terima itu sama dengan tanggal yang ada di `dom`. Apabila sama maka akan diterima.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(dom=[1, 23]):
			...
```

Kode diatas menunjukkan bahwa pesan akan di terima pada tanggal `1` dan `23` saja, untuk selain tanggal tersebut bot akan mengabaikannya.

#### Argumen `month`

`month` di gunakan untuk mengecek, apakah bulan dimana pesan itu diterima sama dengan bulan yang di isi pada argumen `month`, apabila sama maka diterima.

##### Penggunaan

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(month=[1, 2, 11]):
			...
```

| Number | Bulan     |
| ------ | --------- |
| 1      | Januari   |
| 2      | Februari  |
| 3      | Maret     |
| 4      | April     |
| 5      | Mei       |
| 6      | Juni      |
| 7      | Juli      |
| 8      | Agustus   |
| 9      | September |
| 10     | Oktober   |
| 11     | November  |
| 12     | Desember  |

Kode di atas menunjukkan bahwa, pesan yang diterima hanya pada bulan `Januari`, `Frebuari` dan `November` saja.

Teman² juga bisa menambahkan statement elif, seperti di bawah ini

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mtext=['/start']):
			...
		elif bot.cektMessage(mform=['photo'], mcapt=['/convert']):
			...
		elif bot.cektMessage(mtext=['/database'], mfid=[1234567898]):
			...
```

## Proses pesan

Maksud proses pesan adalah bagaimana cara untuk mengirim pesan pada user(cara membalas pesan user). Teman² bisa menggunakan `bot.postReq()`, kemudian isi argumen berupa nama `method` dan `parameter`, seperti di bawah ini

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mtext=['/start']):
			bot.postReq('sendMessage', text=['Hai kak!'], chat_id=[bot.ai])
```

Kode di atas menunjukkan bahwa, apabila seseorang mengirim pesan text `/start`, maka bot akan membalas `Hai kak!`.

> `bot.ai` adalah sebuah peoperty yang isinya berupa field id chat

Untuk mengetahui method² dan parameter, teman² bisa lihat [di sini](https://core.telegram.org/bots/api)

## Mendapatkan field

Untuk mendapatkan field, teman² bisa lakukan secara manual, seperti dibawah ini

`bot.update['message]['chat']['id']`

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mtext=['/start']):
			chatid = bot.update['message]['chat']['id']
			bot.postReq('sendMessage', text=['Hai kak!'], chat_id=[chat_id])
		elif bot.cektMessage(mtext=['/help']):
			chatid = bot.update['message]['chat']['id']
			iduser = bot.update['message']['from']['id']
			teks = bot.update['message']['text']
			bot.postReq('sendMessage', text=['Pesan: ' + teks + '\nId: ' + iduser], chat_id=[chat_id])
```

Atau teman² bisa menggunakan property yang didalamnya berupa field yang sudah disediakan, berikut beberapa property field

- `bot.ac` from `Message => From => Id`
- `bot.ad` from `Message => From => First Name`
- `bot.ae` from `Message => From => Last Name`
- `bot.af` from `Message => From => Username`
- `bot.ag` from `Message => Date`
- `bot.ai` from `Message => Chat => Id`
- `bot.aj` from `Message => Chat => Type`
- `bot.ak` from `Message => Chat => Title`
- `bot.al` from `Message => Chat => Username`
- `bot.am` from `Message => Chat => First Name`
- `bot.an` from `Message => Chat => Last Name`
- `bot.ao` from `Message => Text`
- `bot.ap` from `Message => Caption`

```python
while True:
	if bot.centMessage:
		if bot.cektMessage(mtext=['/start']):
			bot.postReq('sendMessage', text=['Anda mengirim pesan text: ' + bot.ao], chat_id=[bot.ai])
```

## Menjalankan script

Jalankan file `main.py`

#### Terminal
```sh
python main.py
```

> Apabila muncul tulisan `Bot running ...`, berarti bot sudah berjalan.

## Thanks to

• [banghasan](https://github.com/banghasan)

• [butthx](https://github.com/butthx)

• [rushkii](https://github.com/rushkii)

• [hansputera](https://github.com/hansputera)

## License

Lisensi [The Unlicense](https://unlicense.org)

## Nota Bene

Saya minta maaf apabila ada kesalahan pada penamaan dan penulisan, dan saya minta maaf apabila ada kata yang tidak sesuai.

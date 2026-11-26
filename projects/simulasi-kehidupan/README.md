# Simulasi Kehidupan

Game simulasi kehidupan 3D voxel di Bumi: dunia pulau bersungai dan berhutan yang terus berjalan (server-backed, dunia tersimpan dan tetap hidup saat halaman ditutup).

## Fitur utama

- Setiap penduduk AI punya ciri khas sendiri — kepribadian, keahlian, penampilan — yang diwariskan ke keturunannya
- Tiap keluarga punya wilayah berwarna sendiri tempat mereka membangun
- Penduduk bisa lapar, sakit, belajar, bekerja sesuai bakat (petani, pembangun, penyembuh, peneliti, pengumpul), bersosialisasi, menikah, berkembang biak, membuat kesalahan, dan mati
- 15 inovasi berjenjang (Api → Roket) plus inovasi lanjutan tanpa batas; sebelum ada Tulisan, pengetahuan bisa hilang jika semua pemegangnya mati
- Musim & cuaca, bencana (banjir, kebakaran hutan, wabah), god powers (hujan berkah, kirim makanan, sembuhkan, wabah, meteor)
- Waktu resmi 1 jam dunia nyata = 1 hari simulasi, plus mode percepat dan tombol +30 Hari
- Upgrade kota ala city-builder: jalan aspal antar bangunan, gedung bertingkat sampai 4 lantai, layanan publik (sekolah, kantor polisi, pemadam, taman kota, balai kota) yang dibiayai pajak, tingkatan kota Settlement → Metropolis
- Peta 112×112 petak (196 plot wilayah), silsilah keluarga, grafik populasi

## Teknologi

TypeScript, render 3D voxel (instanced), server-backed dengan penyimpanan dunia persisten.

Kode aplikasi tidak dicerminkan di repo portofolio ini (aplikasi server-backed dengan build dan data dunia tersendiri); halaman ini adalah ringkasan proyeknya.

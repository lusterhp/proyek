# views order

from django.shortcuts import render

# Create your views here.

def order(request):
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "Penjadwalan Produksi",
        'subheading': 'Silahkan Melakukan Permintaan Penjadwalan Produksi Pada Laman Form Pendaftaran atau Melihat Daftar Penjadwalan Produksi Pada Laman List Jadwal',
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/order' ,'Penjadwalan Produksi' ],
            ['/order/form' ,'Form Pendaftaran' ],
            ['/order/daftar' ,'List Jadwal' ],
        ],
    }
    return render(request, 'order/order.html', context)

def daftar(request):
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "List Jadwal",
        'subheading': "Berikut Adalah List Penjadwalan yang Telah Terdaftar",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
       'nav': [
            ['/' ,'Halaman Utama' ],
            ['/order' ,'Penjadwalan Produksi' ],
            ['/order/form' ,'Form Pendaftaran' ],
            ['/order/daftar' ,'List Jadwal' ],
        ],
    }

    return render(request, 'order/order.html', context)

def form(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Form Pendaftaran",
        'subheading': 'Silahkan Mengisi Form untuk Meminta Penjadwalan Produksi',
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/order' ,'Penjadwalan Produksi' ],
            ['/order/form' ,'Form Pendaftaran' ],
            ['/order/daftar' ,'List Jadwal' ],
        ],
    }

    return render(request, 'order/order.html', context)
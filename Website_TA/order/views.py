# views order

from django.shortcuts import render

# Create your views here.

def order(request):
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'konten': 'Silahkan Mlakukan Permintaan Penjadwalan Produksi Dengan Mengisi Form',
        'banner': 'order/img/banner.png',
        'nav': [
            ['/' ,'Halaman Utama' ],
        ],
        'nav2': [
            ['/order' ,'Penjadwalan Produksi' ],
        ],
        'subnav2': [
            ['/order/form' ,'Form Permintaan Penjadwalan Produksi' ],
            ['/order/daftar' ,'Daftar Penjadwalan Produksi' ],
        ],
    }
    return render(request, 'order/order.html', context)

def daftar(request):
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'konten': "Berikut adalah daftar penjadwalan:",
        'banner': 'order/img/banner.png',
        'nav': [
            ['/' ,'Halaman Utama' ],
        ],
        'nav2': [
            ['/order' ,'Penjadwalan Produksi' ],
        ],
        'subnav2': [
            ['/order/form' ,'Permintaan Penjadwalan Produksi' ],
            ['/order/daftar' ,'Daftar Penjadwalan Produksi' ],
        ],
    }

    return render(request, 'order/order.html', context)

def form(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'konten': 'Silahkan Mengisi Form untuk Meminta Penjadwalan Produksi',
        'banner': 'order/img/banner.png',
        'nav': [
            ['/' ,'Halaman Utama' ],
        ],
        'nav2': [
            ['/order' ,'Penjadwalan Produksi' ],
        ],
        'subnav2': [
            ['/order/form' ,'Permintaan Penjadwalan Produksi' ],
            ['/order/daftar' ,'Daftar Penjadwalan Produksi' ],
        ],
    }

    return render(request, 'order/order.html', context)
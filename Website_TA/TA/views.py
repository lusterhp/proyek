# views home

from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'konten': 'Daftar Menu:',
        'banner': 'img/banner.png',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/about' ,'Tentang Pembuat' ],
            ['/order' ,'Penjadwalan Produksi' ],
        ],
    }

    return render(request, 'home.html', context)
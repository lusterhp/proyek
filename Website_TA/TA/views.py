# views home

from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'konten': '',
        'banner': 'img/banner.png',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/about' ,'Tentang Pembuat' ],
            ['/order' ,'List Penjadwalan' ],
            ['/produk' ,'List Pesanan' ],
            ['/projectshop' ,'List Asset' ],
        ],
        'konek': 'TA SYIFA',
    }

    return render(request, 'home.html', context)
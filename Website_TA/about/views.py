# views about

from django.shortcuts import render

# Create your views here.

def about(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'konten': "Tentang Pembuat",
        'banner': 'about/img/banner.png',
        'nav': [
            ['/' ,'Halaman Utama' ],
        ],
    }

    return render(request, 'about/about.html', context)

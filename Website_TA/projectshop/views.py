# views projectshop

from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def asset(request):
    lapak = LapakKerja.objects.all()
    alat = PeralatanKerja.objects.all()
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "List Asset",
        'subheading': "Berikut Adalah List Asset yang Dimiliki",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/projectshop' ,'List Asset' ],
            ['/projectshop/tambah-asset' ,'Tambah Asset' ],
        ],
        'Lapak':lapak,
        'Alat':alat,
    }

    return render(request, 'projectshop/asset.html', context)

def form(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Penambahan Asset",
        'subheading': "Silahkan memilih tautan untuk menambahkan asset",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/projectshop' ,'List Asset' ],
            ['/projectshop/tambah-asset' ,'Tambah Asset' ],
        ],
    }

    return render(request, 'projectshop/form.html', context)

def form1(request):
    if request.POST:
        form1 = FormLapak(request.POST)
        if  form1.is_valid():
            form1.save()
            form1 = FormLapak()
            pesan = "Lapak berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Lapak",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/projectshop' ,'List Asset' ],
                    ['/projectshop/tambah-asset' ,'Tambah Asset' ],
                    ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
                ],
                'lapak':form1,
                'pesan' : pesan,
                    }
            return render(request, 'projectshop/form1.html', context)

    else:
        form1 = FormLapak()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/projectshop' ,'List Asset' ],
                ['/projectshop/tambah-asset' ,'Tambah Asset' ],
                ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
            ],
            'lapak':form1,
        }

        return render(request, 'projectshop/form1.html', context)

    # form1 = FormLapak()
    # if request.method == 'POST':
    #     LapakKerja.objects.create(
    #         nama_lapak = request.POST.get('nama_lapak'),
    #         availabilitas = request.POST.get('availabilitas'),
    #     )

    # context = {
    #     'judul': 'Project Shop SPTM',
    #     'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #     'heading': "Form Penambahan Asset",
    #     'subheading': "Silahkan Mengisi Form untuk Menambahkan Lapak",
    #     'banner': 'about/img/banner.png',
    #     'app_css': 'order/css/style.css',
    #     'nav': [
    #         ['/' ,'Halaman Utama' ],
    #         ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
    #         ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
    #         ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
    #     ],
    #     'lapak':form1,
    # }
    # return render(request, 'projectshop/form1.html', context)

def form2(request):
    if request.POST:
        form2 = FormKode(request.POST)
        if   form2.is_valid():
             form2.save()
             form2 = FormKode()
             pesan = "Kode Alat berhasil ditambahkan"
             context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Kode Alat",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/projectshop' ,'List Asset' ],
                    ['/projectshop/tambah-asset' ,'Tambah Asset' ],
                    ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
                ],
                'kode':form2,
                'pesan' : pesan,
                    }
             return render(request, 'projectshop/form2.html', context)

    else:
        form2 = FormKode()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/projectshop' ,'List Asset' ],
                ['/projectshop/tambah-asset' ,'Tambah Asset' ],
                ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
            ],
            'kode':form2,
        }

        return render(request, 'projectshop/form2.html', context)

    # form2 = FormKode()
    # if request.method == 'POST':
    #     KodePeralatan.objects.create(
    #     kode_alat = request.POST.get('kode_alat'),
    #     )

    # context = {
    #     'judul': 'Project Shop SPTM',
    #     'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #     'heading': "Form Penambahan Asset",
    #     'subheading': "Silahkan Mengisi Form untuk Menambahkan Kode Alat",
    #     'banner': 'about/img/banner.png',
    #     'app_css': 'order/css/style.css',
    #     'nav': [
    #         ['/' ,'Halaman Utama' ],
    #         ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
    #         ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
    #         ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
    #     ],
    #     'kode':form2,
    # }
    # return render(request, 'projectshop/form2.html', context)

def form3(request):
    if request.POST:
        form3 = FormAlat(request.POST)
        if form3.is_valid():
            form3.save()
            form3 = FormAlat()
            pesan = "Alat berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Peralatan",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/projectshop' ,'List Asset' ],
                    ['/projectshop/tambah-asset' ,'Tambah Asset' ],
                    ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
                ],
                'alat':form3,
                'pesan' : pesan,
            }
            return render(request, 'projectshop/form3.html', context)

    else:
        form3 = FormAlat()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/projectshop' ,'List Asset' ],
                ['/projectshop/tambah-asset' ,'Tambah Asset' ],
                ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
            ],
            'alat':form3,
        }

        return render(request, 'projectshop/form3.html', context)

    # form3 = FormAlat()
    # if request.method == 'POST':
    #     PeralatanKerja.objects.create(
    #         nama_alat = request.POST['nama_alat'],
    #         kodealat_id = request.POST['kodealat_id'],
    #         availabilitas = request.POST['availabilitas'],
    #     )

    # context = {
    #     'judul': 'Project Shop SPTM',
    #     'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #     'heading': "Form Penambahan Asset",
    #     'subheading': "Silahkan Mengisi Form untuk Menambahkan Peralatan",
    #     'banner': 'about/img/banner.png',
    #     'app_css': 'order/css/style.css',
    #     'nav': [
    #         ['/' ,'Halaman Utama' ],
    #         ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
    #         ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
    #         ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
    #     ],
    #     'alat':form3,
    # }
    # return render(request, 'projectshop/form3.html', context)





    # if request.POST:
    #     form = FormLapak(request.POST)
    #     form2 = FormKode(request.POST)
    #     form3 = FormAlat(request.POST)
    #     if  form.is_valid():
    #         form.save()
    #         form = FormLapak()
    #         pesan = "Lapak berhasil ditambahkan"
    #         context = {
    #             'judul': 'Project Shop SPTM',
    #             'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #             'heading': "Form Penambahan Asset",
    #             'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #             'banner': 'about/img/banner.png',
    #             'app_css': 'order/css/style.css',
    #             'nav': [
    #                 ['/' ,'Halaman Utama' ],
    #                 ['/order' ,'Penjadwalan Produksi' ],
    #                 ['/produk' ,'List Produksi' ],
    #                 ['/projectshop' ,'List Asset' ],
    #                 ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #             ],
    #             'lapak':form,
    #             'kode':form2,
    #             'alat':form3,
    #             'pesan' : pesan,
    #                 }
    #         return render(request, 'projectshop/form.html', context)
    #     elif form2.is_valid():
    #          form2.save()
    #          form2 = FormKode()
    #          pesan = "Kode Alat berhasil ditambahkan"
    #          context = {
    #             'judul': 'Project Shop SPTM',
    #             'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #             'heading': "Form Penambahan Asset",
    #             'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #             'banner': 'about/img/banner.png',
    #             'app_css': 'order/css/style.css',
    #             'nav': [
    #                 ['/' ,'Halaman Utama' ],
    #                 ['/order' ,'Penjadwalan Produksi' ],
    #                 ['/produk' ,'List Produksi' ],
    #                 ['/projectshop' ,'List Asset' ],
    #                 ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #             ],
    #             'lapak':form,
    #             'kode':form2,
    #             'alat':form3,
    #             'pesan' : pesan,
    #                 }
    #          return render(request, 'projectshop/form.html', context)
    #     elif form3.is_valid():
    #          form3.save()
    #          form3 = FormAlat()
    #          pesan = "Alat berhasil ditambahkan"
    #          context = {
    #             'judul': 'Project Shop SPTM',
    #             'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #             'heading': "Form Penambahan Asset",
    #             'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #             'banner': 'about/img/banner.png',
    #             'app_css': 'order/css/style.css',
    #             'nav': [
    #                 ['/' ,'Halaman Utama' ],
    #                 ['/order' ,'Penjadwalan Produksi' ],
    #                 ['/produk' ,'List Produksi' ],
    #                 ['/projectshop' ,'List Asset' ],
    #                 ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #             ],
    #             'lapak':form,
    #             'kode':form2,
    #             'alat':form3,
    #             'pesan' : pesan,
    #                 }
    #          return render(request, 'projectshop/form.html', context)

    # else:
    #     form = FormLapak()
    #     form2 = FormKode()
    #     form3 = FormAlat()
    #     context = {
    #         'judul': 'Project Shop SPTM',
    #         'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #         'heading': "Form Penambahan Asset",
    #         'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #         'banner': 'about/img/banner.png',
    #         'app_css': 'order/css/style.css',
    #         'nav': [
    #             ['/' ,'Halaman Utama' ],
    #             ['/order' ,'Penjadwalan Produksi' ],
    #             ['/produk' ,'List Produksi' ],
    #             ['/projectshop' ,'List Asset' ],
    #             ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ],
    #         'lapak':form,
    #         'kode':form2,
    #         'alat':form3,
    #     }

    #     return render(request, 'projectshop/form.html', context)
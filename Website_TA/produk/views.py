# views produk

from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def tambah(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Form Penambahan Produk",
        'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/produk' ,'List Pesanan' ],
            ['/produk/tambah' ,'Halaman Penambahan Produk' ],
        ],
    }

    return render(request, 'produk/tambah.html', context)

def produk(request):
    if request.POST:
        form = FormProduk(request.POST)
        if form.is_valid():
            form.save()
            form = FormProduk()
            pesan = "Produk berhasil ditambahkan"
            form2 = FormModel
            form3 = FormVariant
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Produk",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                    ['/produk/tambah-produk' ,'Tambah Produk' ],
                ],
                'produk':form,
                'pesan' : pesan,
            }

            return render(request, 'produk/produk.html', context)

    else:
        form = FormProduk()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Produk",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                ['/produk/tambah-produk' ,'Tambah Produk' ],
            ],
            'produk':form,
        }

        return render(request, 'produk/produk.html', context)       

def model(request):
    if request.POST:
        form2 = FormModel(request.POST)
        if form2.is_valid():
            form2.save()
            form2 = FormModel()
            pesan = "Model Produk berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Produk",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                    ['/produk/tambah-model' ,'Tambah Model Produk' ],
                ],
                'model':form2,
                'pesan': pesan,
            }

            return render(request, 'produk/model.html', context)

    else:
        form2 = FormModel()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Produk",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                ['/produk/tambah-model' ,'Tambah Model Produk' ],
            ],
            'model':form2,
        }

        return render(request, 'produk/model.html', context)

def variant(request):
    if request.POST:
        form3 = FormVariant(request.POST)
        if form3.is_valid():
            form3.save()
            form3 = FormVariant()
            pesan = "Variant Model Produk berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Produk",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                    ['/produk/tambah-variant' ,'Tambah Variant Model Produk' ],
                ],
                'variant':form3,
                'pesan': pesan,
            }

            return render(request, 'produk/variant.html', context)

    else:
        form3 = FormVariant()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Produk",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                ['/produk/tambah-variant' ,'Tambah Variant Model Produk' ],
            ],
            'variant':form3,
        }

        return render(request, 'produk/variant.html', context)

def material(request):
    if request.POST:
        form = FormMaterial(request.POST)
        if form.is_valid():
            form.save()
            form = FormMaterial()
            pesan = "Material berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Material",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Material",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                    ['/produk/tambah-material' ,'Tambah Material Produk' ],
                ],
                'material':form,
                'pesan' : pesan,
            }

            return render(request, 'produk/material.html', context)

    else:
        form = FormMaterial()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Material",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Material",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                ['/produk/tambah-material' ,'Tambah Material Produk' ],
            ],
            'material':form,
        }

        return render(request, 'produk/material.html', context)

def list(request):
    list = Variant.objects.all()
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "List Pesanan",
        'subheading': "Berikut Adalah List Pesanan yang Telah Dijadwalkan Produksinya",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/produk' ,'List Pesanan' ],
            ['/produk/tambah' ,'Halaman Penambahan Produk' ],
        ],
        'List':list,
    }

    return render(request, 'produk/list.html', context)
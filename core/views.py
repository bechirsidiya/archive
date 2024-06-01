from django.shortcuts import render, get_object_or_404
from TC.models import Archivetc, Matiers1
from GEM.models import Archivegm ,Matiergm
from GAB.models import Archivegab ,Matiergab
from PPV.models import Archiveppv, Matierppv
from PSA.models import Archivepsa , Matierpsa
from STA.models import Archivesta , Matiersta



def index(request):
    """
    Render the homepage.
    """
    return render(request, "core/index.html")

def tc_view(request):
    """
    Render the TC page with a list of all matiers.
    """
    matiers = Matiers1.objects.all()
    return render(request, "core/tc.html", {
        'matiers': matiers,
    })

def matier_detailtc(request, matier_id):
    """
    Render the detail page for a specific matier, including its related PDFs.
    """
    matier = get_object_or_404(Matiers1, id=matier_id)
    pdfs = matier.archive.all()
    return render(request, 'core/matier_detailtc.html', {'matier': matier, 'pdfs': pdfs})


def gem_view(request):
    """
    Render the GEM page with a list of all matiers.
    """
    matiers = Matiergm.objects.all()
    return render(request, "core/gem.html", {
        'matiers': matiers,
    })

def matier_detailgem(request, matier_id):
    """
    Render the detail page for a specific matier, including its related PDFs.
    """
    matier = get_object_or_404(Matiergm, id=matier_id)
    pdfs = matier.archive.all()
    return render(request, 'core/matier_detailgem.html', {'matier': matier, 'pdfs': pdfs})



def gab_view(request):
    """
    Render the GAB page with a list of all matiers.
    """
    matiers = Matiergab.objects.all()
    return render(request, "core/gab.html", {
        'matiers': matiers,
    })

def matier_detailgab(request, matier_id):
    """
    Render the detail page for a specific matier, including its related PDFs.
    """
    matier = get_object_or_404(Matiergab, id=matier_id)
    pdfs = matier.archive.all()
    return render(request, 'core/matier_detailgab.html', {'matier': matier, 'pdfs': pdfs})


def ppv_view(request):
    """
    Render the ppv page with a list of all matiers.
    """
    matiers = Matierppv.objects.all()
    return render(request, "core/ppv.html", {
        'matiers': matiers,
    })

def matier_detailppv(request, matier_id):
    """
    Render the detail page for a specific matier, including its related PDFs.
    """
    matier = get_object_or_404(Matierppv, id=matier_id)
    pdfs = matier.archive.all()
    return render(request, 'core/matier_detailppv.html', {'matier': matier, 'pdfs': pdfs})



def psa_view(request):
    """
    Render the TC page with a list of all matiers.
    """
    matiers = Matierpsa.objects.all()
    return render(request, "core/psa.html", {
        'matiers': matiers,
    })

def matier_detailpsa(request, matier_id):
    """
    Render the detail page for a specific matier, including its related PDFs.
    """
    matier = get_object_or_404(Matierpsa, id=matier_id)
    pdfs = matier.archive.all()
    return render(request, 'core/matier_detailpsa.html', {'matier': matier, 'pdfs': pdfs})


def sta_view(request):
    """
    Render the TC page with a list of all matiers.
    """
    matiers = Matiersta.objects.all()
    return render(request, "core/sta.html", {
        'matiers': matiers,
    })

def matier_detailsta(request, matier_id):
    """
    Render the detail page for a specific matier, including its related PDFs.
    """
    matier = get_object_or_404(Matiersta, id=matier_id)
    pdfs = matier.archive.all()
    return render(request, 'core/matier_detailsta.html', {'matier': matier, 'pdfs': pdfs})
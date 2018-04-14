from .views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^clanak', ClanakView.as_view()),
    url(r'^slika', SlikaView.as_view()),
    url(r'^dokument', DokumentView.as_view()),
    url(r'^grandstream', GrandstreamView.as_view()),
    url(r'^korisnik', KorisnikView.as_view()),
    url(r'^partner', PartnerView.as_view()),
    url(r'^kontakt', KontaktView.as_view()),
    url(r'^filler', TekstMarketingView.as_view()),
    url(r'^zaposlenik', ZaposlenikView.as_view()),
]

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import pandas as pd

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    df = pd.read_excel('data-398-2022-08-16.xlsx', engine="openpyxl")
    df_req = df[['Name', 'District', 'StationName']]
    print(df_req)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(df_req, 25)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': df_req,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

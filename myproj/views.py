import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic.list import ListView
import basedosdados as bd
from .settings import GOOGLE_CLOUD_PROJECT_ID
from django.core.serializers import serialize

# def first(request):
#     return render(request, 'first.html', {})

def api(request):
    '''
    Ex: http://127.0.0.1:8000/api/?linha=862
    '''
    data = request.GET
    linha = data.get('linha')
    num_ordem = data.get('num_ordem')
    empresa = data.get('empresa') #TODO
    df = bd.read_sql ( "SELECT * FROM `datario.transporte_rodoviario_municipal.gps_onibus` LIMIT 1000" , billing_project_id = GOOGLE_CLOUD_PROJECT_ID )
    if linha:
        df2=df.query("servico == '" + linha + "'")
    elif num_ordem:
        df2 = df[df['id_veiculo'].str.contains(num_ordem)]
    else:
        df2=df
    result = df2.to_json(orient="records")
    parsed = json.loads(result)

    return JsonResponse(parsed,safe=False)
    # return serialize("geojson",parsed, geometry_field="point",)# fields=["name"])

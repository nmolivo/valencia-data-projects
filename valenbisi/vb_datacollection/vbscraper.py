import pandas as pd
import requests
import json
from time import sleep

counter = 0

while counter < 672:
    if counter % 8 == 0:
        print(counter)
    r = requests.get("http://mapas.valencia.es/lanzadera/opendata/Valenbisi/JSON")
    if r.status_code != 200:
        sleep(15*60)
        continue #sends to the front of the loop without adding to counter
    
    res = r.json()
    
    X_values = []
    Y_values = []
    name_values = []
    number_values = []
    open_values = []
    ticket_values = []
    available_values = []
    free_values = []
    total_values = []
    update_values = []
    
    for record in range(0, len(res['features'])):
        xx = res['features'][record]['geometry']['coordinates'][0]
        yy = res['features'][record]['geometry']['coordinates'][1]
        nombre = res['features'][record]['properties']['name']
        numero = res['features'][record]['properties']['number']
        abierto = res['features'][record]['properties']['open']
        boleta = res['features'][record]['properties']['ticket']
        disponible = res['features'][record]['properties']['available']
        feliz = res['features'][record]['properties']['free']
        cantidad = res['features'][record]['properties']['total']
        fecha = res['features'][record]['properties']['updated_at']

        X_values.append(xx)
        Y_values.append(yy)
        name_values.append(nombre)
        number_values.append(numero)
        open_values.append(abierto)
        ticket_values.append(boleta)
        available_values.append(disponible)
        free_values.append(feliz)
        total_values.append(cantidad)
        update_values.append(fecha)
        
    bici_dict = {"X":X_values,
            "Y":Y_values,
            "name":name_values,
            "number":number_values,
            "open": open_values,
            "ticket":ticket_values,
            "available":available_values,
            "free":free_values,
            "total":total_values,
            "update":update_values}
    
    df = pd.DataFrame(bici_dict)
    
    fname = 'vb_data/valencia_bisi_'+"%05d" % (counter,)+'.json'
    df.to_json(fname, force_ascii=False)
    
    counter += 1
    sleep(15*60)
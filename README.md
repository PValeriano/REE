# REE
## Inicio rápido
```
from ree import REE
from datetime import datetime

instancia = REE()

precios = instancia.get_PVPC()
fecha_llamada = instancia.date.strftime('%d-%m-%y')

precios_hora = [[datetime.strptime(d.get("datetime"),
                 "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%H:%M"),f"{d.get('value')} €/KwH"] for d in precios]

print(f'Los precios del día {fecha_llamada} son: \n {precios_hora}')
```

Conector al endpoint del mercado de precios en tiempo real para la península ibérica de [Red Eléctrica de España](https://www.ree.es/es/apidatos). \
Los precios para el día siguiente se suelen actualizar pasadas las 20:15 de cada día. Si el programa se ejecuta antes de las 20:30 (CET) entonces se devuelven los precios del día actual. \
Contiene dos métodos:
  - ```get_PVPC()```: devuelve los precios del mercado del precio voluntario para el pequeño consumidor.
  - ```get_PMS()```: devuelve el precio marginal del sistema.

Se pueden usar junto con ```self.date``` para recuperar el día al que corresponden los datos.

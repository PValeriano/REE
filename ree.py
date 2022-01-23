class REE():
    def __init__(self):
        self._date = None
        self._api_endpoint_base = 'https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?'
        self._params = None
        self._start_date = None
        self._end_date = None
        self._api_endpoint = None
        self._data = None
        self._last_update = None
        self._description = None
        
    @property
    def date(self):
        '''
        Fecha de petición de precios.
        '''
        return self._date
    
    @property
    def description(self):
        '''
        Descripción del endpoint de REE.es usado en la llamada.
        '''
        return self._description
    
    @property
    def last_update(self):
        '''
        Fecha y hora de subida de los datos por parte de REE.
        '''
        return self._last_update
    
    def update_parameters(self):
        '''
        Actualización de parámetros de fecha y hora para la construcción del endpoint.
        '''
        if self._start_date != f'{self._date}T00:00':
            if datetime.now().hour < 20 and datetime.now().minute < 30:
                self._date = date.today()
            else:
                self._date = date.today() + timedelta(days=1)
            self._start_date = f'{self._date}T00:00'
            self._end_date = f'{self._date}T23:59'
            self._api_endpoint = f'{self._api_endpoint_base}start_date={self._start_date}&end_date={self._end_date}&time_trunc=hour'
            
        
    def get_data(self):
        '''
        Petición de datos si no hay datos en memoria o si los datos son de un día diferente a d+1 o d.
        '''
        if self._data == None or self._start_date != f'{self._date}T00:00':
            self.update_parameters()
            self._data = requests.get(self._api_endpoint)
            self._last_update = self._data.json().get('data').get('attributes').get('last-update')
            self._description = self._data.json().get('data').get('type')
        #return self._data

    def get_PVPC(self):
        '''
        PVPC (€/MWh)
        '''
        self.get_data()
        return self._data.json().get('included')[0].get('attributes').get('values')
    
    def get_PMS(self):
        '''
        Precio mercado spot (€/MWh)
        '''
        self.get_data()
        return self._data.json().get('included')[1].get('attributes').get('values')

if __name__ == '__main__':
    inst = REE()
    print(inst.get_PVPC())
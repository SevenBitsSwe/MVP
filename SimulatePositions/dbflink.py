import clickhouse_connect

class BatchDatabaseUser():
    def __init__(self):
        self.databaseClient = clickhouse_connect.get_client(
            host='clickhouse', 
            port=8123, 
            username='default', 
            password='pass'
        )
    
    def getFirstUser(self) -> dict:
        utenti = self.databaseClient.query('''
        SELECT
            u.id,
            u.nome,
            u.cognome,
            u.genere,
            u.data_nascita,
            u.stato_civile,
            i.interesse
        FROM 
            nearyou.utente AS u
        INNER JOIN
            nearyou.interesseUtente AS i 
        ON
            u.id = i.utente
        LIMIT 1
        ''').result_rows

        if not utenti:
            return {
                "id": "00000000-0000-0000-0000-000000000000",
                "Nome": "Utente",
                "Cognome": "Test",
                "Genere": "M",
                "Data_nascita": "1990-01-01",
                "Stato_civile": "Single",
                "Interesse1": "Sport"
            }

        user_dict = {
            "id": str(utenti[0][0]),  # Converti UUID in stringa
            "Nome": utenti[0][1],
            "Cognome": utenti[0][2],
            "Genere": utenti[0][3],
            "Data_nascita": utenti[0][4],
            "Stato_civile": utenti[0][5],
        }
        c = 1
        for utente in utenti:
            key = "Interesse"+str(c)
            user_dict[key] = utente[6]
            c += 1

        return user_dict
    
    def getActivities(self, lon, lat) -> list:
        params = {
            'lon': lon,
            'lat': lat
        }

        query = '''
        SELECT
            a.id,
            a.nome,
            a.indirizzo,
            a.tipologia,
            a.descrizione,
            geoDistance(%(lon)s, %(lat)s, a.lon, a.lat) as distanza
        FROM 
            nearyou.attivita AS a
        WHERE
            geoDistance(%(lon)s, %(lat)s, a.lon, a.lat) <= 300
        '''
        
        return self.databaseClient.query(query, parameters=params).result_rows
    
    def getActivityCoordinates(self, activityName) -> dict:
        param = {'nome': activityName}
        query = '''
        SELECT 
            a.lon,
            a.lat
        FROM 
            nearyou.attivita AS a  
        WHERE
            a.nome = %(nome)s
        '''
        dizionario = self.databaseClient.query(query, parameters=param)
        if len(dizionario.result_set) == 0:
            return {"lon": 0, "lat": 0}
        else: 
            return dizionario.first_item
        
    def getLastMessageCoordinates(self) -> dict: 
        query = '''
        SELECT 
            longitude,
            latitude
        FROM nearyou.messageTable
        ORDER BY creationTime DESC 
        LIMIT 1
        '''    
        dizionario = self.databaseClient.query(query)
        if len(dizionario.result_set) == 0:
            return {"longitude": 0, "latitude": 0}
        else: 
            return dizionario.first_item

    def getActivityID(self, activityName) -> str:
        param = {'nome': activityName}
        query = '''
        SELECT 
            toString(a.id) as id
        FROM 
            nearyou.attivita AS a  
        WHERE
            a.nome = %(nome)s
        '''
        dizionario = self.databaseClient.query(query, parameters=param)
        if len(dizionario.result_set) == 0:
            return "00000000-0000-0000-0000-000000000000"
        else: 
            return dizionario.first_item["id"]
from Core.IActivityRepository import IActivityRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.ActivityDTO import ActivityDTO

class ClickhouseActivityRepository(IActivityRepository):
    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    def get_activities_in_range(self, lon, lat, max_distance) -> list:
        params = {
            'lon': lon,
            'lat': lat,
            'max_distance': max_distance
        }

        query ='''
        SELECT
            a.name,
            a.address,
            a.type,
            a.description,
            geoDistance( %(lon)s , %(lat)s  ,a.longitude ,a.latitude) as distanza
        FROM 
            nearyou.activity AS a
        WHERE
            geoDistance( %(lon)s , %(lat)s  ,a.longitude ,a.latitude) <= %(max_distance)s
        '''
        conn = self.__db_conn.connect()
        return conn.query(query,parameters=params).result_rows

    def get_activity_for_user(self, interests, activity_list):
        activity_list_filtered_for_type = []

        #filtro per tipologia
        for activity in activity_list:
            if activity[2] in interests:
                activity_list_filtered_for_type.append(activity)

        if len(activity_list_filtered_for_type) == 0:
            return None

        #filtro per distanza
        activity_min = min(activity_list_filtered_for_type, key=lambda a: a[4])

        return activity_min

    def get_activity_spec_from_name(self, activity_name) -> ActivityDTO:
        param = {'nome':activity_name}
        query = '''
        SELECT 
            *
        FROM 
            nearyou.activity AS a  
        WHERE
            a.name = %(nome)s
        '''
        conn = self.__db_conn.connect()
        dizionario = conn.query(query, parameters=param)
        if len(dizionario.result_set) == 0:
            return ActivityDTO()
        else:
            return ActivityDTO(dizionario.first_item['activity_uuid'],
                              dizionario.first_item['name'],
                              float(dizionario.first_item['longitude']),
                              float(dizionario.first_item['latitude']),
                              dizionario.first_item['address'],
                              dizionario.first_item['type'],
                              dizionario.first_item['description'])

# {'activity_uuid': UUID('a61e3f8d-098e-442b-996f-02fd849bb1b1'),
# 'name': 'Gasperi, Almagi e Lollobrigida SPA',
#  'longitude': 11.8444214, 'latitude': 45.3785957,
#  'address': 'Contrada Altera, Montegallo, Bellamonte, Grosseto, 51021, Italia',
#  'type': 'Educazione', 'description': 'Centro di formazione'}

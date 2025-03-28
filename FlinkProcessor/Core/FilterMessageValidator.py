from pyflink.datastream.functions import FilterFunction
from datetime import datetime
import uuid

class FilterMessageValidator(FilterFunction):
    """
    Filtra i messaggi Kafka invalidi o potenzialmente dannosi.
    I messaggi che non passano la validazione vengono scartati.
    """
    def open(self,runtime_context):
        pass
    
    def filter(self, value):
        # Validazione dei campi obbligatori
        print(value)
        # Validazione del range di latitudine/longitudine
        lat = value[1]
        lon = value[2]
        if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
            return False

        if lat < -90 or lat > 90 or lon < -180 or lon > 180:
            return False
        # Validazione temporale (esempio)
        received_at = value[3]
        try:
            datetime.strptime(received_at, '%Y-%m-%d %H:%M:%S')
        except (ValueError, TypeError):
            return False

        # Validazione dimensioni massime
        user_id = value[0]
        # Validazione che l'user_id sia un UUID valido
        try:
            uuid_obj = uuid.UUID(user_id, version=4)
        except (ValueError, TypeError):
            return False

        # Verifica contenuti potenzialmente dannosi (esempio base)
        for val in value:
            if isinstance(val, str):
                # Controllo base per SQL injection
                suspicious_patterns = ["--", ";", "DROP", "DELETE", "UPDATE", "INSERT", "SELECT * FROM"]
                if any(pattern.lower() in val.lower() for pattern in suspicious_patterns):
                    return False

        return True

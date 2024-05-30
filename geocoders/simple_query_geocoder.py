from geocoders.geocoder import Geocoder


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
         node = API.get_area(area_id)
        adress = node.name

        if node.parent_id is None: # Если сразу попадается страна
            return adress

        while node := API.get_area(node.parent_id):

            adress = node.name + ' ' + adress  # Добавляет имя родительского узла к уже сформированному адресу

            
            if node.parent_id is None: # Проверяет, является ли родительский узел корневым

                break
        raise NotImplementedError()


class Satelite:
    def __init__(self, nombre, n_catalogo, latitud, longitud, altitud):

        if type(nombre) != str or not nombre.strip():
            raise ValueError("El satelite debe tener un nombre")

        if type(n_catalogo) != int:
            raise ValueError("El numero de catalogo debe ser un entero")

        if type(latitud) not in (int, float):
            raise ValueError("La latitud debe ser numerica")

        if not -90 <= latitud <= 90:
            raise ValueError("La latitud debe estar entre -90 y 90")

        if type(longitud) not in (int, float):
            raise ValueError("La longitud debe ser numerica")

        if not -180 <= longitud <= 180:
            raise ValueError("La longitud debe estar entre -180 y 180")

        if type(altitud) not in (int, float):
            raise ValueError("La altitud debe ser numerica")

        if altitud < 100:
            raise ValueError("La altitud debe ser de al menos 100 km",)

        self.nombre = nombre
        self.n_catalogo = n_catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def tipo_orbita(self):
        if self.altitud < 2000:
            return "LEO"
        if self.altitud < 34000:
            return "MEO"
        if self.altitud <= 37000:
            return "GEO"
        return "HEO"

    def descripcion (self):
        return (f"{self.nombre} | {self.n_catalogo} | {self.tipo_orbita()} | {self.altitud}")

    def zona(self,long_min,lat_min,long_max,lat_max):
        if float(lat_min)<=self.latitud<=float(lat_max) and float(long_min)<=self.longitud<=float(long_max):
            return True
        return False
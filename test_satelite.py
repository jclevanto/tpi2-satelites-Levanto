from satelite import Satelite
import pytest

def test_orbita_LEO():
    satelite = Satelite("leo", 25544, 0, 0, 400)
    assert satelite.tipo_orbita() == "LEO"


def test_orbita_MEO():
    satelite = Satelite("meo", 25545, 0, 0, 10000)
    assert satelite.tipo_orbita() == "MEO"


def test_orbita_GEO():
    satelite = Satelite("geo", 25546, 0, 0, 35786)
    assert satelite.tipo_orbita() == "GEO"


def test_orbita_HEO():
    satelite = Satelite("heo", 25547, 0, 0, 38000)
    assert satelite.tipo_orbita() == "HEO"

def test_nombre_no_es_string():
    with pytest.raises(ValueError, match="El satelite debe tener un nombre"):
        Satelite(123, 25544, 0, 0, 400)


def test_nombre_vacio():
    with pytest.raises(ValueError, match="El satelite debe tener un nombre"):
        Satelite("   ", 25544, 0, 0, 400)


def test_catalogo_no_es_entero():
    with pytest.raises(ValueError, match="El numero de catalogo debe ser un entero"):
        Satelite("sat", "25544", 0, 0, 400)


def test_latitud_no_numerica():
    with pytest.raises(ValueError, match="La latitud debe ser numerica"):
        Satelite("sat", 25544, "cero", 0, 400)


def test_latitud_menor_al_limite():
    with pytest.raises(ValueError, match="La latitud debe estar entre -90 y 90"):
        Satelite("sat", 25544, -91, 0, 400)


def test_latitud_mayor_al_limite():
    with pytest.raises(ValueError, match="La latitud debe estar entre -90 y 90"):
        Satelite("sat", 25544, 91, 0, 400)


def test_longitud_no_numerica():
    with pytest.raises(ValueError, match="La longitud debe ser numerica"):
        Satelite("sat", 25544, 0, "cero", 400)


def test_longitud_menor_al_limite():
    with pytest.raises(ValueError, match="La longitud debe estar entre -180 y 180"):
        Satelite("sat", 25544, 0, -181, 400)


def test_longitud_mayor_al_limite():
    with pytest.raises(ValueError, match="La longitud debe estar entre -180 y 180"):
        Satelite("sat", 25544, 0, 181, 400)


def test_altitud_no_numerica():
    with pytest.raises(ValueError, match="La altitud debe ser numerica"):
        Satelite("sat", 25544, 0, 0, "400")


def test_altitud_menor_al_limite():
    with pytest.raises(ValueError, match="La altitud debe ser de al menos 100 km"):
        Satelite("sat", 25544, 0, 0, 99)


def test_altitud_igual_al_limite():
    satelite = Satelite("sat", 25544, 0, 0, 100)
    assert satelite.altitud == 100

def test_zona_dentro():
    satelite = Satelite("sat", 25544, 0, 0, 400)
    assert satelite.zona(-10, -10, 10, 10) == True


def test_zona_fuera_latitud():
    satelite = Satelite("sat", 25544, 20, 0, 400)
    assert satelite.zona(-10, -10, 10, 10) == False


def test_zona_fuera_longitud():
    satelite = Satelite("sat", 25544, 0, 20, 400)
    assert satelite.zona(-10, -10, 10, 10) == False


def test_zona_limite():
    satelite = Satelite("sat", 25544, 10, 10, 400)
    assert satelite.zona(-10, -10, 10, 10) == True


def test_zona_limite_negativo():
    satelite = Satelite("sat", 25544, -10, -10, 400)
    assert satelite.zona(-10, -10, 10, 10) == True
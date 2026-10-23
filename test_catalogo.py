
from catalogo import catalogo, resumen_orbita
from satelite import Satelite


def test_catalogo():
    datos = [
        {
        "OBJECT_NAME": "CALSPHERE 1",
        "OBJECT_ID": "1964-063C",
        "EPOCH": "2026-10-14T14:21:25.466688",
        "MEAN_MOTION": 13.76730837,
        "ECCENTRICITY": 0.00243553,
        "INCLINATION": 90.2208,
        "RA_OF_ASC_NODE": 74.5342,
        "ARG_OF_PERICENTER": 291.4443,
        "MEAN_ANOMALY": 198.023,
        "EPHEMERIS_TYPE": 0,
        "CLASSIFICATION_TYPE": "U",
        "NORAD_CAT_ID": 900,
        "ELEMENT_SET_NO": 999,
        "REV_AT_EPOCH": 8785,
        "BSTAR": 0.00056429819,
        "MEAN_MOTION_DOT": 5.64e-06,
        "MEAN_MOTION_DDOT": 0
        },
        {
        "OBJECT_NAME": "CALSPHERE 2",
        "OBJECT_ID": "1964-063E",
        "EPOCH": "2026-10-14T11:27:54.596736",
        "MEAN_MOTION": 13.52908228,
        "ECCENTRICITY": 0.00169509,
        "INCLINATION": 90.2317,
        "RA_OF_ASC_NODE": 78.5946,
        "ARG_OF_PERICENTER": 237.821,
        "MEAN_ANOMALY": 195.4493,
        "EPHEMERIS_TYPE": 0,
        "CLASSIFICATION_TYPE": "U",
        "NORAD_CAT_ID": 902,
        "ELEMENT_SET_NO": 999,
        "REV_AT_EPOCH": 87239,
        "BSTAR": 5.6971978e-05,
        "MEAN_MOTION_DOT": 4.7e-07,
        "MEAN_MOTION_DDOT": 0
        }]
    resultado = catalogo(datos)

    assert len(resultado) == 2
    assert resultado[0].nombre == "CALSPHERE 1"
    assert resultado[0].n_catalogo == 900
    assert resultado[1].nombre == "CALSPHERE 2"
    assert resultado[1].n_catalogo == 902

def test_resumen_orbita():
    satelites = [
        Satelite("1", 25544, 0, 0, 400),
        Satelite("2", 25545, 0, 0, 600),
        Satelite("3", 25546, 0, 0, 10000)
    ]

    resultado = resumen_orbita(satelites)

    assert resultado["LEO"]["cantidad"] == 2
    assert resultado["LEO"]["minimo"] == 400
    assert resultado["LEO"]["maximo"] == 600
    assert resultado["LEO"]["promedio"] == 500

    assert resultado["MEO"]["cantidad"] == 1

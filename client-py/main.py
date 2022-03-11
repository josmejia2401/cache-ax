import sys
from src.main.index import CacheAxClient

if __name__ == '__main__':
    client = CacheAxClient(63456, 'localhost')
    value = "Los clientes de Fairphone van desde programadores que se han sentido atraídos por las posibilidades del software de los teléfonos hasta consumidores que buscan un producto más sostenible.La empresa comenzó en 2013 y sigue cuatro principios: obtener materias primas de áreas mineras que no son de conflicto y fabricar productos que sean reciclables, duraderos y reparables.Según cifras de Naciones Unidas, en 2019 se generaron un récord de 53,6 millones de toneladas de desechos electrónicos en todo el mundo, un 21% más que hace cinco años, y los teléfonos móviles constituyen una parte importante de estos. Además, solo se recicló el 17% de los desechos electrónicos.Fairphone argumenta que, al hacer que los teléfonos sean fáciles de reparar, pueden tener una vida útil más larga, generar menos desechos y, por lo tanto, tener un impacto positivo en el medioambiente.Los clientes de Fairphone van desde programadores que se han sentido atraídos por las posibilidades del software de los teléfonos hasta consumidores que buscan un producto más sostenible.La empresa comenzó en 2013 y sigue cuatro principios: obtener materias primas de áreas mineras que no son de conflicto y fabricar productos que sean reciclables, duraderos y reparables.Según cifras de Naciones Unidas, en 2019 se generaron un récord de 53,6 millones de toneladas de desechos electrónicos en todo el mundo, un 21% más que hace cinco años, y los teléfonos móviles constituyen una parte importante de estos. Además, solo se recicló el 17% de los desechos electrónicos.Fairphone argumenta que, al hacer que los teléfonos sean fáciles de reparar, pueden tener una vida útil más larga, generar menos desechos y, por lo tanto, tener un impacto positivo en el medioambiente."
    key = "TG9zIGNsaWVudGVzIGRlIEZhaXJwaG9uZSB2YW4gZGVzZGUgcHJvZ3JhbWFkb3JlcyBxdWUgc2UgaGFuIHNlbnRpZG8gYXRyYcOtZG9zIHBvciBsYXMgcG9zaWJpbGlkYWRlcyBkZWwgc29mdHdhcmUgZGUgbG9zIHRlbMOpZm9ub3MgaGFzdGEgY29uc3VtaWRvcmVzIHF1ZSBidXNjYW4gdW4gcHJvZHVjdG8gbcOhcyBzb3N0ZW5pYmxlLkxhIGVtcHJlc2EgY29tZW56w7MgZW4gMjAxMyB5IHNpZ3VlIGN1YXRybyBwcmluY2lwaW9zOiBvYnRlbmVyIG1hdGVyaWFzIHByaW1hcyBkZSDDoXJlYXMgbWluZXJhcy4="
    try:
        maxTime = 0
        for i in range(50):
            output = client.set("{0}{1}".format(i, key), key)
            if output["responseTime"] > maxTime:
                maxTime = output["responseTime"]
        print("maxTime", maxTime)
    except KeyboardInterrupt:
        sys.exit(0)

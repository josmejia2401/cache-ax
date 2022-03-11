import { CacheAxClient } from '../src/main/index';
jest.setTimeout(300_000);
describe("Test Case CacheClient", () => {
    const value = "Los clientes de Fairphone van desde programadores que se han sentido atraídos por las posibilidades del software de los teléfonos hasta consumidores que buscan un producto más sostenible.La empresa comenzó en 2013 y sigue cuatro principios: obtener materias primas de áreas mineras que no son de conflicto y fabricar productos que sean reciclables, duraderos y reparables.Según cifras de Naciones Unidas, en 2019 se generaron un récord de 53,6 millones de toneladas de desechos electrónicos en todo el mundo, un 21% más que hace cinco años, y los teléfonos móviles constituyen una parte importante de estos. Además, solo se recicló el 17% de los desechos electrónicos.Fairphone argumenta que, al hacer que los teléfonos sean fáciles de reparar, pueden tener una vida útil más larga, generar menos desechos y, por lo tanto, tener un impacto positivo en el medioambiente.Los clientes de Fairphone van desde programadores que se han sentido atraídos por las posibilidades del software de los teléfonos hasta consumidores que buscan un producto más sostenible.La empresa comenzó en 2013 y sigue cuatro principios: obtener materias primas de áreas mineras que no son de conflicto y fabricar productos que sean reciclables, duraderos y reparables.Según cifras de Naciones Unidas, en 2019 se generaron un récord de 53,6 millones de toneladas de desechos electrónicos en todo el mundo, un 21% más que hace cinco años, y los teléfonos móviles constituyen una parte importante de estos. Además, solo se recicló el 17% de los desechos electrónicos.Fairphone argumenta que, al hacer que los teléfonos sean fáciles de reparar, pueden tener una vida útil más larga, generar menos desechos y, por lo tanto, tener un impacto positivo en el medioambiente.";
    const key = "TG9zIGNsaWVudGVzIGRlIEZhaXJwaG9uZSB2YW4gZGVzZGUgcHJvZ3JhbWFkb3JlcyBxdWUgc2UgaGFuIHNlbnRpZG8gYXRyYcOtZG9zIHBvciBsYXMgcG9zaWJpbGlkYWRlcyBkZWwgc29mdHdhcmUgZGUgbG9zIHRlbMOpZm9ub3MgaGFzdGEgY29uc3VtaWRvcmVzIHF1ZSBidXNjYW4gdW4gcHJvZHVjdG8gbcOhcyBzb3N0ZW5pYmxlLkxhIGVtcHJlc2EgY29tZW56w7MgZW4gMjAxMyB5IHNpZ3VlIGN1YXRybyBwcmluY2lwaW9zOiBvYnRlbmVyIG1hdGVyaWFzIHByaW1hcyBkZSDDoXJlYXMgbWluZXJhcy4=";

    beforeEach(() => { });
    afterEach(() => { });

    test("test SET", (done) => {
        try {
            [...Array(1)].forEach(async (_val, index) => {
                let maxTime = 0;
                const result = await Promise.all([...Array(5)].map((_value, ind) => new CacheAxClient(63456, undefined, {
                    timeAlive: 15000
                }).set(`${(index * ind) + ind}${key}`, value)));
                result.forEach((p: any) => {
                    if (p["responseTime"] > maxTime) {
                        maxTime = p["responseTime"];
                    }
                });
                console.log("maxTime", maxTime);
                expect(maxTime).toBeDefined();
                done();
            });
        } catch (error) {
            expect(error).toBeDefined();
        }
    });

    test("test GET", (done) => {
        try {
            [...Array(1)].forEach(async (_val, index) => {
                let maxTime = 0;
                const result = await Promise.all([...Array(5)].map((_value, _ind) => new CacheAxClient().get(`${index}${key}`)));
                result.forEach((p: any) => {
                    if (p["responseTime"] > maxTime) {
                        maxTime = p["responseTime"];
                    }
                });
                console.log("maxTime", maxTime);
                expect(maxTime).toBeDefined();
                done();
            });
        } catch (error) {
            expect(error).toBeDefined();
        }
    });

    test("test GET_ALL", (done) => {
        try {
            [...Array(1)].forEach(async (_val, _index) => {
                let maxTime = 0;
                const result = await Promise.all([...Array(5)].map((_value, _ind) => new CacheAxClient().getAll()));
                result.forEach((p: any) => {
                    if (p["responseTime"] > maxTime) {
                        maxTime = p["responseTime"];
                    }
                });
                console.log("maxTime", maxTime);
                expect(maxTime).toBeDefined();
                done();
            });
        } catch (error) {
            expect(error).toBeDefined();
        }
    });
    test("test SIZE", (done) => {
        try {
            [...Array(1)].forEach(async (_val, _index) => {
                let maxTime = 0;
                let size = 0;
                const result = await Promise.all([...Array(5)].map((_value, _ind) => new CacheAxClient().size()));
                result.forEach((p: any) => {
                    if (p["responseTime"] > maxTime) {
                        maxTime = p["responseTime"];
                    }
                    size = p["data"];
                });
                console.log("maxTime", maxTime);
                console.log("size", size);
                expect(maxTime).toBeDefined();
                done();
            });
        } catch (error) {
            expect(error).toBeDefined();
        }
    });

    /*
       test("test REMOVE", (done) => {
        try {
            [...Array(1)].forEach(async (_val, index) => {
                let maxTime = 0;
                const result = await Promise.all([...Array(5)].map((_value, _ind) => new CacheAxClient().remove(`${index}${key}`)));
                result.forEach((p: any) => {
                    if (p["responseTime"] > maxTime) {
                        maxTime = p["responseTime"];
                    }
                });
                console.log("maxTime", maxTime);
                expect(maxTime).toBeDefined();
                done();
            });
        } catch (error) {
            expect(error).toBeDefined();
        }
    });


    test("test CLEAN", (done) => {
        try {
            [...Array(1)].forEach(async (_val, _index) => {
                let maxTime = 0;
                const result = await Promise.all([...Array(5)].map((_value, _ind) => new CacheAxClient().clean()));
                result.forEach((p: any) => {
                    if (p["responseTime"] > maxTime) {
                        maxTime = p["responseTime"];
                    }
                });
                console.log("maxTime", maxTime);
                expect(maxTime).toBeDefined();
                done();
            });
        } catch (error) {
            expect(error).toBeDefined();
        }
    });
*/
});
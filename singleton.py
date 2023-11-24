# Ejemplo de Singleton para administrar una cola de impresión

class ColaImpresión:

    _instance_ = None

    def __init__(this):
        # Inicializar la cola de impresión
        this.cola = []

    # Métodos de instancia
    def agregarDocumento(this, documento):
        this.cola.append(documento)

    def imprimirDocumento(this):
        documento = this.cola.pop(0)
    # Imprimir el documento
        print(documento)


    # Método de clase para crear la instancia del singleton
    @classmethod
    def getInstance(this):
        if this._instance_ is None:
            this._instance_ = this()
        return this._instance_

# Ejemplo de uso del Singleton

colaImpresión = ColaImpresión.getInstance()

colaImpresión.agregarDocumento("Documento 1")
colaImpresión.agregarDocumento("Documento 2")
colaImpresión.agregarDocumento("Documento 3")

colaImpresión.imprimirDocumento()
colaImpresión.imprimirDocumento()
colaImpresión.imprimirDocumento()

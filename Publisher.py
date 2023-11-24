# Clase que publica mensajes a suscriptores
class Notificador:

    # Inicializar una lista de suscriptores
    def __init__(self):
        self._suscriptores = []

    # Agregar un suscriptor a la lista
    def agregar_suscriptor(self, suscriptor):
        self._suscriptores.append(suscriptor)

    # Eliminar un suscriptor de la lista
    def eliminar_suscriptor(self, suscriptor):
        self._suscriptores.remove(suscriptor)

    # Notificar a todos los suscriptores sobre un mensaje
    def notificar_suscriptores(self, mensaje):
        for suscriptor in self._suscriptores:
            suscriptor.actualizar(mensaje)


# Clase base para suscriptores
class Suscriptor:

    # Implementar el método actualizar para manejar mensajes
    def actualizar(self, mensaje):
        pass


# Clase de suscriptor concreta
class SuscriptorNotificaciones(Suscriptor):

    def actualizar(self, mensaje):
        print(f"Suscriptor de notificaciones recibió mensaje: {mensaje}")


# Clase de suscriptor concreta
class SuscriptorAlertas(Suscriptor):

    def actualizar(self, mensaje):
        print(f"Suscriptor de alertas recibió mensaje: {mensaje}")


# Programa principal
if __name__ == "__main__":
    # Crear una instancia del notificador
    notificador = Notificador()

    # Crear instancias de suscriptores
    suscriptor_notificaciones = SuscriptorNotificaciones()
    suscriptor_alertas = SuscriptorAlertas()

    # Agregar suscriptores al notificador
    notificador.agregar_suscriptor(suscriptor_notificaciones)
    notificador.agregar_suscriptor(suscriptor_alertas)

    # Notificar a los suscriptores sobre un mensaje
    notificador.notificar_suscriptores("Notificación: El clima está cambiando")
    notificador.notificar_suscriptores("Alerta: Se detectó un incendio")

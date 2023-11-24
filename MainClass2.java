import java.util.ArrayList;
import java.util.List;

public class MainClass2 {

    public static void main(String[] args) {
        // Crear una lista de tareas de estudio
        List<EstudioTask> tareasEstudio = new ArrayList<>();
        tareasEstudio.add(new EstudioTask("Revisar apuntes"));
        tareasEstudio.add(new EstudioTask("Resolver ejercicios"));
        tareasEstudio.add(new EstudioTask("Repasar conceptos"));

        // Crear 3 hilos que ejecuten las tareas de estudio
        Thread[] hilosEstudio = new Thread[3];
        for (int i = 0; i < hilosEstudio.length; i++) {
            final int tareaIndex = i; // Identificador para el hilo actual
            hilosEstudio[i] = new Thread(() -> {
                // Obtener y ejecutar la tarea asignada al hilo
                EstudioTask tarea = tareasEstudio.remove(0);
                System.out.println("¡Inicio de estudio! Preparándose para: " + tarea.getNombre() +
                        " en el hilo " + tareaIndex);
                tarea.run();
                System.out.println("¡Fin de estudio! ¡Se completó: " + tarea.getNombre() +
                        " en el hilo " + tareaIndex);
            });
            hilosEstudio[i].start(); // Iniciar cada hilo de estudio
        }

        // Esperar a que todos los hilos de estudio terminen
        for (Thread hilo : hilosEstudio) {
            try {
                hilo.join(); // Esperar a que cada hilo de estudio termine antes de continuar
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // Imprimir un mensaje de finalización
        System.out.println("¡Buen trabajo! Todas las tareas de estudio han sido completadas.");
    }
}

class EstudioTask {

    private String nombre;

    public EstudioTask(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void run() {
        System.out.println("¡En proceso de estudio! Realizando tarea: " + nombre);
        try {
            // Simular el tiempo de estudio
            for (int i = 0; i < 3; i++) {
                Thread.sleep(500); // Dormir durante 500 milisegundos
                System.out.println("Progreso de " + nombre + " en el hilo actual: " + (i + 1) + "/3");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}



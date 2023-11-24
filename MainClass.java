import java.util.ArrayList;
import java.util.List;

public class MainClass {

    public static void main(String[] args) {
        // Crear una lista de tareas
        List<Task> tareas = new ArrayList<>();
        tareas.add(new Task("Descargar archivos"));
        tareas.add(new Task("Procesar archivos"));
        tareas.add(new Task("Subir archivos"));

        // Crear 3 hilos que ejecuten las tareas
        Thread[] hilosTareas = new Thread[3];
        for (int i = 0; i < hilosTareas.length; i++) {
            final int tareaIndex = i; // Variable final para el lambda
            hilosTareas[i] = new Thread(() -> {
                Task tarea = tareas.remove(0);
                System.out.println("Iniciando tarea: " + tarea.getNombre() + " en el hilo " + tareaIndex);
                tarea.run();
                System.out.println("Tarea completada: " + tarea.getNombre() + " en el hilo " + tareaIndex);
            });
            hilosTareas[i].start();
        }

        // Esperar a que todos los hilos terminen
        for (Thread hilo : hilosTareas) {
            try {
                hilo.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // Imprimir un mensaje de finalización
        System.out.println("Todas las tareas completadas");
    }
}

class Task {

    private String nombre;

    public Task(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void run() {
        System.out.println("Ejecutando tarea: " + nombre);
        try {
            // Simulando el progreso de la tarea
            for (int i = 0; i < 5; i++) {
                Thread.sleep(200); // Dormir durante 200 milisegundos
                System.out.println("Progreso de " + nombre + " en el hilo actual: " + (i + 1) + "/5");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

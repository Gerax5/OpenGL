# Proyecto Final
* Gerardo Pineda 22880
# Video de muestra
<div style={{ textAlign: "center" }}>
  <video src="/videos/video1042113675.mp4" controls style={{width: "100%"}}></video>
</div>

# Controles

| **Dispositivo** | **Tecla/Acción**             | **Función**                                              |
|------------------|------------------------------|----------------------------------------------------------|
| **Teclado**      | **W**                        | Subir en el eje Y de la cámara                          |
|                  | **S**                        | Bajar en el eje Y de la cámara                          |
|                  | **A**                        | Girar a la izquierda en órbita                          |
|                  | **D**                        | Girar a la derecha en órbita                            |
|                  | **Espacio o Space bar**      | Cambiar de modelo                                       |
| **Mouse**        | **Click izquierdo**          | Mirar hacia arriba, abajo y a los lados (mantener clic) |
|                  | **Scroll bar**               | Acercar o alejar ( no estoy seguro porque no tengo mouse para probar 🫠 ) |


# Shaders Usados

| **Tipo de Shader** | **Nombre**                | **Descripción**                                                                               | **Video**       |
|---------------------|--------------------------|-----------------------------------------------------------------------------------------------|-----------------|
| **Vertex Shader**   | **wave_shader**          | Un vertex shader que hace ondulaciones de forma horizontal                                    | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/vertex/pygame%20window%202024-10-28%2019-59-40.gif)   |
| **Vertex Shader**   | **cut_shader**           | Parte el modelo a la mitad y mueve una parte hacia atrás y la otra hacia adelante             | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/vertex/pygame%20window%202024-10-28%2019-59-57.gif)   |
| **Vertex Shader**   | **anormal_shader**       | Hace que distintas partes del modelo cambien de tamaño al azar a gran velocidad               | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/vertex/pygame%20window%202024-10-28%2020-01-02.gif)   |
| **Vertex Shader**   | **ondulation_shader**    | Un shader que hace ondulaciones de forma vertical                                             | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/vertex/pygame%20window%202024-10-28%2020-01-15.gif)   |
| **Fragment Shader** | **pixel_shader**         | Hace que la textura parezca pixelada                                                         | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/fragment/pygame%20window%202024-10-28%2020-08-00.gif)   |
| **Fragment Shader** | **Fragment_noise**       | Hace que todo desaparezca con un efecto de ruido                                             | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/fragment/pygame%20window%202024-10-28%2020-08-18.gif)   |
| **Fragment Shader** | **fragment_dissolver**   | Crea un patrón que hace desaparecer y aparecer el modelo en círculos pequeños                | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/fragment/pygame%20window%202024-10-28%2020-09-53.gif)   |
| **Fragment Shader** | **fragment_hologram**    | Hace que el modelo parezca un holograma                                                      | ![Ver video](https://github.com/Gerax5/OpenGL/blob/main/videos/gifs/fragment/pygame%20window%202024-10-28%2020-10-09.gif)   |

# Modelos usados 

| **Nombre del Modelo** | **Archivo del Modelo**    | **Vertex Shader**      | **Fragment Shader**           |
|------------------------|---------------------------|-------------------------|--------------------------------|
| **Banana**            | OBJ/banan.obj            | anormal_shader          | fragment_dissolved_pattern    |
| **Shrek**             | OBJ/Shrek.obj            | ondulation_shader       | fragment_hologram             |
| **Planet**            | OBJ/sp.obj               | wave_shader             | fragment_hologram             |
| **Eugene**            | OBJ/Eugene.obj           | cut_shader              | pixel_shader                  |
| **Pengu**             | OBJ/Penguin.obj          | ondulation_shader       | fragment_noise                |




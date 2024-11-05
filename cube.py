from cubemap_splitter import split_cubemap

# Automatically determine format and create new directory with images at original image location
split_cubemap("C:/Users/Gerax/OneDrive/Desktop/UVGG/3-2/Graficas/Open/OpenGL/texture/skybox/mio/mio.jpg")

# Specify format and write to user defined directory
split_cubemap("C:/Users/Gerax/OneDrive/Desktop/UVGG/3-2/Graficas/Open/OpenGL/texture/skybox/mio/mio.jpg", format_type=1, output_directory="C:/Users/Gerax/OneDrive/Desktop/UVGG/3-2/Graficas/Open/OpenGL/texture/skybox/mio/")
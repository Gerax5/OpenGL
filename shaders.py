vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    outPosition = modelMatrix * vec4(position , 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}

'''

fat_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    outPosition = modelMatrix * vec4(position + normals * sin(time) /10 , 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}

'''

water_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    outPosition = modelMatrix * vec4(position + vec3(0,1,0) * sin(time * position.x * 10) / 10, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}

'''

fragment_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;
uniform vec3 pointLight;

out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, normalize(pointLight - outPosition.xyz));
    fragColor = texture(tex, outTexCoords) * intensity;
}


'''

negative_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;

out vec4 fragColor;

void main()
{
    fragColor = 1 - texture(tex, outTexCoords);
}


'''

pixel_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;
uniform vec3 pointLight;

out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, normalize(pointLight - outPosition.xyz));
    float pixelSize = 0.03;
    vec2 pixelatedCoords = vec2(
        floor(outTexCoords.x / pixelSize) * pixelSize,
        floor(outTexCoords.y / pixelSize) * pixelSize
    );
    fragColor = texture(tex, pixelatedCoords) * intensity;
}


'''

fragment_noise = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;
uniform vec3 pointLight;
uniform float time;

out vec4 fragColor;

float rand(vec2 co) {
    return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
}

void main()
{
    vec3 normal = normalize(outNormals);
    vec3 lightDir = normalize(pointLight - outPosition.xyz);
    float intensity = max(dot(normal, lightDir), 0.0);

    float noiseValue = rand(outTexCoords * 10.0 + time * 0.5);
    float threshold = fract(time * 0.5);

    if (noiseValue < threshold)
        discard; 

    fragColor = texture(tex, outTexCoords) * intensity;
}

'''

fragment_dissolved_pattern = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;
uniform vec3 pointLight;
uniform float time;

out vec4 fragColor;

void main()
{

    vec3 normal = normalize(outNormals);
    vec3 lightDir = normalize(pointLight - outPosition.xyz);
    float intensity = max(dot(normal, lightDir), 0.0);

    float pattern = sin(outPosition.y * 10.0 + time * 5.0) * cos(outPosition.x * 10.0 + time * 5.0);
    pattern = (pattern + 1.0) * 0.5;

    float velocidadUmbral = 0.2;
    float edge = 0.1;
    float exponencial = 2.0;

    float threshold = pow(sin(time * velocidadUmbral * 3.1416) * 0.5 + 0.5, exponencial);

    float alpha = smoothstep(threshold - edge, threshold + edge, pattern);

    if (alpha <= 0.0)
        discard;

    fragColor = texture(tex, outTexCoords) * intensity * alpha;
}
'''


wave_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float time;

void main()
{
    float displacement = sin(position.x * 10.0 + time * 5.0) * 0.02;
    vec3 newPosition = position;
    newPosition.y += displacement;

    outPosition = modelMatrix * vec4(newPosition, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}


'''



fragment_hologram = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;
uniform vec3 pointLight;

out vec4 fragColor;

void main()
{
    vec3 normal = normalize(outNormals);
    vec3 lightDir = normalize(pointLight - outPosition.xyz);
    float intensity = max(dot(normal, lightDir), 0.0);

    float scanline = sin((outPosition.y + 1 * 5.0) * 100.0) * 0.1;
    float brightness = intensity + scanline;

    float offset = 0.005;
    vec2 texCoordR = outTexCoords + vec2(offset, 0.0);
    vec2 texCoordG = outTexCoords;
    vec2 texCoordB = outTexCoords - vec2(offset, 0.0);

    vec4 colorR = texture(tex, texCoordR);
    vec4 colorG = texture(tex, texCoordG);
    vec4 colorB = texture(tex, texCoordB);

    vec4 color = vec4(colorR.r, colorG.g, colorB.b, colorG.a);

    vec3 hologramColor = vec3(0.0, 0.7, 1.0);
    color.rgb *= hologramColor;

    float alpha = 0.6 + sin(1 * 5.0) * 0.1;

    fragColor = color * brightness * vec4(1.0, 1.0, 1.0, alpha);
}

'''

cut_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main() {
    float amplitude = 0.3;
    float frequency = 2.0;
    float sector = mod(position.x + position.y, 2.0);

    float waveEffect = (sector * 2.0 - 1.0) * sin(position.z * frequency + time) * amplitude;

    vec3 displacedPosition = position + vec3(0.0, 0.0, waveEffect);

    outPosition = modelMatrix * vec4(displacedPosition, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}

'''

anormal_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}

void main() {
    float amplitude = 0.3;
    vec2 posXZ = position.xz;
    float scaleEffect = 1.0 + amplitude * random(posXZ + time);

    vec3 displacedPosition = position * scaleEffect;

    outPosition = modelMatrix * vec4(displacedPosition, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}


'''

ondulation_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main() {
    float amplitude = 0.1;
    float frequency = 2.0;

    float distance = length(position.xy); 
    float pulse = amplitude * sin(frequency * time + distance * 5.0);

    vec3 displacedPosition = position + position * pulse;

    outPosition = modelMatrix * vec4(displacedPosition, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}

'''


skybox_vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 inPosition;

uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec3 texCoords;

void main()
{
    texCoords = inPosition;
    gl_Position = projectionMatrix * viewMatrix * vec4(inPosition, 1.0);
}

'''

skybox_fragment_shader = '''
#version 450 core

uniform samplerCube skybox;

in vec3 texCoords;

out vec4 fragColor;

void main()
{
    fragColor = texture(skybox, texCoords);
}

'''
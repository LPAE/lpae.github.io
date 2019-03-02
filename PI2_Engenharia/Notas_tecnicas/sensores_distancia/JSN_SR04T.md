# **Módulo Sensor Ultrassônico JSN-SR04T a Prova D'água V2**

---

![Resultado de imagem para JSN-SR04t](https://cdn.awsli.com.br/600x700/78/78150/produto/24288369/1b26eec974.jpg)

O **Módulo Sensor Ultrassônico JSN-SR04T a Prova D'água V2** foi desenvolvido para atuar em ambientes úmidos, porém, **não deve em hipótese alguma ser submerso em água ou quarquer outro líquido**,
este sensor é capaz de realizar medições que vão de **25cm a 6m**, seu 
funcionamento ocorre com o princípio de envio de um sinal ultrassônico, 
reflexão em um obstáculo que é recebido pelo sensor, dessa forma, o 
sensor consegue calcular a distância até o obstáculo.



- Modelo: JSN-SR04T;
- Tensão: DC 3,3 - 5V;
- Corrente: 5mA;
- Corrente de trabalho: 30mA;
- Freqüência: 40KHz;
- Comprimento do cabo do sensor: 2.5 metros;
- Diâmetro do sensor: 22mm;
- Dimensões do módulo: 41.5x28.5x17mm.

[Datasheet](https://uamper.com/products/datasheet/JSN-SR04T-2.0.pdf)

---

**Código para Teste:**

Por meio da biblioteca [NewPing](https://bitbucket.org/teckel12/arduino-new-ping/wiki/Home) é possível operar o sensor uma vez que o projetista faça usa do framework Arduino. 

O Exemplo abaixo apresenta uma simples demostração de como utilizar a biblioteca:

```c++
#include <Arduino.h>
#include <NewPing.h>
#include <Wire.h>

#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.

#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.

#define MAX_DISTANCE 450 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.


NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.


void setup() {
  
  Serial.begin(115200); // Open serial monitor at 115200 baud to see ping results.
}

void loop() {
  
  delay(250);                      
  unsigned int o,uS = sonar.ping(); 

  o = uS;
  Serial.print("Distance: ");
  Serial.print( o / US_ROUNDTRIP_CM); // Convert ping time to distance in cm and print result (0 = outside set distance range)
  Serial.println("cm");
}
```



O resultado do código acima apresenta o seguinte resultado:

Distance: 33cm
Distance: 0cm
Distance: 33cm
Distance: 0cm
Distance: 33cm
Distance: 33cm
Distance: 0cm
Distance: 0cm
Distance: 33cm
Distance: 33cm
Distance: 0cm
Distance: 33cm
Distance: 35cm
Distance: 33cm
Distance: 33cm
Distance: 34cm
Distance: 0cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 35cm
Distance: 0cm
Distance: 33cm
Distance: 34cm
Distance: 35cm
Distance: 33cm
Distance: 34cm
Distance: 33cm
Distance: 33cm
Distance: 0cm
Distance: 0cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 0cm
Distance: 34cm
Distance: 34cm
Distance: 34cm
Distance: 34cm
Distance: 0cm
Distance: 34cm
Distance: 34cm
Distance: 34cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 0cm
Distance: 33cm
Distance: 34cm
Distance: 34cm
Distance: 34cm
Distance: 34cm
Distance: 0cm
Distance: 33cm
Distance: 34cm
Distance: 0cm
Distance: 0cm
Distance: 0cm
Distance: 34cm
Distance: 34cm
Distance: 34cm
Distance: 34cm
Distance: 33cm
Distance: 34cm
Distance: 34cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 34cm
Distance: 34cm
Distance: 0cm
Distance: 33cm
Distance: 33cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 34cm
Distance: 0cm
Distance: 0cm
Distance: 33cm
Distance: 34cm
Distance: 33cm
Distance: 33cm
Distance: 0cm
Distance: 33cm
Distance: 33cm
Distance: 33cm
Distance: 33cm

Como é possível observar no resultado acima, esse sensor pode acabar apresentado resultados com alguns valores zeros durante uma sequência de medições. Logo é necessário fazer tratamento do dado após a aquisição (como um filtro de média móvel).

[Voltar](https://lpae.github.io/)
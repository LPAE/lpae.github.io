# O Arducopter 
[Voltar](https://lpae.github.io/estudos/DRONE/)

O Arducopter é um APM (Arduino Pilot Meta), ou seja, um cotrolador de voo de código aberto semelhante a plataforma arduíno.

![Arducopter](https://github.com/LPAE/lpae.github.io/blob/master/estudos/DRONE/Informa%C3%A7%C3%B5es/imagens/arducopter.jpg?raw=true)

Este componente de nosso drone realiza altomáticamente a navegação, estabilização e a telemetria.   E pode ser controlado pelo controle ou diretamente por uma programação de waypoints configurada anteriormente.  Ele dará uma infinidade de recursos e modos de vôos, ao todo são 14 modos, dentre eles:

Stabilize - Drone fica na horizontal, estabilizado sem precisar de comandos para não cair;

Alt Hold - Sua aceleração é controlada automaticamente c/ finalidade de manter a mesma altura;

Headless Mode - O drone sempre terá a mesma frente e trás, não invertendo os comandos do rádio controle caso a traseira dele não esteja para você;

Loiter (MODO GPS) - Mantem a posição independente do vento ou qualquer outro fator;

Return to launch - Retorna sozinho para posição de decolagem;

Auto - Vôo autônomo, faz uma missão programa pelo computador;

Land - Pousa sozinho;

Failsafe - Caso seu drone perca sinal do rádio controle ou esteja acabando a bateria, ele retornará sozinho e pousará do local da decolagem.


 Exemplo de controle por waypoints 
 
![waypoints](https://github.com/LPAE/lpae.github.io/blob/master/estudos/DRONE/Informa%C3%A7%C3%B5es/imagens/localiza%C3%A7%C3%A3o.png?raw=true)

Este controle pode ser feito diretamente no Software do Arducopter disponível em [SOFTWARE](http://ardupilot.org/copter/docs/common-install-gcs.html), este programa tem de ser instalado em seu computador, qualquer dúvida vale dar uma olhada na página de configuração do aplicativo.

[Configurações do aplicativo](./configurações.md)

# Flame Well

![Flame Well](https://github.com/LPAE/lpae.github.io/blob/master/estudos/DRONE/IMAGENS/flame%20weel.png?raw=true) 

A armação foi usado um Flame Weel F450 com 4 braços proporcionando melhor resistência ao impacto e também conduz a eletricidade necessária para todos os componentes eletrônicos, minimizando o número de fios.

O design de quadro otimizado oferece muito espaço para um sistema de piloto automático.

Usando alta resistência placa de quadro PCB composto, o que torna a fiação de CES e bateria mais segura e mais fácil.

[Voltar](https://lpae.github.io/estudos/DRONE/)

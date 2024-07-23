
Detecção de Círculos em Imagens com OpenCV e Hough Transform
Este repositório contém um script Python para detectar círculos em imagens usando o OpenCV e a transformada de Hough.

Funcionalidades:

Carrega uma imagem colorida.
Converte a imagem para tons de cinza.
Aplica um filtro de suavização (opcional) para reduzir ruído na imagem.
Utiliza a transformada de Hough para detectar círculos na imagem em tons de cinza.
Desenha círculos detectados na imagem original (colorida).
Exibe a imagem resultante com os círculos.
Requisitos:

Python 3.6 ou superior
pip
OpenCV

Detalhes do Script:

O script carrega a imagem especificada no caminho image_path.
Em seguida, a imagem é convertida para tons de cinza, pois a transformada de Hough funciona melhor com imagens em tons de cinza.
A aplicação de um filtro de suavização (opcional) pode ajudar a reduzir ruído na imagem e melhorar a detecção de círculos.
A função cv2.HoughCircles é usada para detectar círculos na imagem. Os parâmetros da função como param1 e param2 controlam a sensibilidade da detecção e a resolução dos círculos.
O script verifica se a detecção de círculos foi bem-sucedida (ou seja, detected_circles não é None).
Se círculos forem encontrados, o script itera sobre cada círculo e extrai seu centro (coordenadas x e y) e raio.
As coordenadas e o raio são convertidos para inteiros antes de serem usados para desenhar os círculos na imagem original.
O script desenha dois círculos para cada círculo detectado:
Um círculo verde com a espessura de linha 2, representando o contorno do círculo.
Um pequeno círculo azul no centro do círculo verde, representando o centro do círculo detectado.
Finalmente, o script exibe a imagem com os círculos detectados e aguarda o pressionamento de uma tecla para fechar a janela.
Observações:

A precisão da detecção de círculos depende da qualidade da imagem e dos parâmetros utilizados na transformada de Hough.
Você pode ajustar os parâmetros da função cv2.HoughCircles para melhorar a detecção de círculos em diferentes tipos de imagens.
Este script é um exemplo básico e pode ser adaptado para detectar outros objetos usando diferentes técnicas de processamento de imagem.
Contribuições:

Sinta-se à vontade para contribuir com este projeto reportando bugs, sugerindo melhorias ou criando pull requests com suas próprias modificações.

Licença:

Este projeto está licenciado sob a licença MIT.

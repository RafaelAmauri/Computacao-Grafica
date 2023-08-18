# Trabalho de Computação Gráfica

## Como utilizar ?

O executável do programa já inclui todas as bibliotecas e dependências necessárias para rodar o programa!

Se você desejar rodar o programa a partir do código-fonte, instale o gerenciador de pacotes pip primeiro em https://pypi.org/project/pip/.

Em seguida, é fácil! Basta rodar:

```
pip3 install -r requirements.txt
```

Depois, para executar o programa, rode:

```
python3 main.py
```

## Dicas de utilização

* Se a sua figura ficar grande demais para ficar dentro do canvas, ela sairá da
área de renderização! Tenha isso em mente antes de aplicar transformações com fatores
muito altos!

* A origem do canvas é no canto inferior esquerdo! Para evitar que operações de escala muito grandes tirem sua figura do canvas, pensa em colocá-la próxima da origem!

* A borracha muda a cor do pincel para branco! Depois de selecionar a borracha, se quiser voltar a pintar, selecione uma cor diferente no menu de cores!
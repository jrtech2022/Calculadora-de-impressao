Calculadora de Impressão - Jr_Tech_OFC

Este é um projeto de uma calculadora de impressão simples, criada para calcular os custos de serviços como xerox, impressões em preto e branco, impressões coloridas e fotos 3x4. O sistema é composto por uma interface web para o cliente inserir os dados, além de um backend em Python para salvar os dados em arquivos de texto.

Funcionalidades

- Cálculo em tempo real: O preço de cada serviço é atualizado conforme o usuário digita a quantidade.
- Finalização e gravação de dados: Ao final do processo, os dados são gravados em um arquivo .txt para análise posterior.
- Tecnologias usadas:
  - Frontend: HTML, CSS, JavaScript
  - Backend: Python (usando Flask para o servidor e pyftpdlib para FTP)
  - Outros: Git, GitHub para controle de versão

Como rodar o projeto

Pré-requisitos

Certifique-se de ter o Python 3.x instalado no seu sistema. Além disso, instale as dependências necessárias com o comando:

pip install flask pyftpdlib

Como rodar o servidor

1. Clone o repositório ou faça o download do código.
2. Navegue até a pasta do projeto.
3. Inicie o servidor com o comando abaixo:

python server.py

O servidor estará disponível em http://localhost:5000, e você poderá acessá-lo diretamente no navegador.

Como usar a calculadora

1. Acesse o site http://localhost:5000 no seu navegador.
2. Preencha os campos com as quantidades de xerox, impressões e fotos 3x4 que deseja calcular.
3. O preço será atualizado automaticamente à medida que você digitar.
4. Clique em Finalizar para registrar os dados, e um arquivo .txt será gerado contendo as informações sobre o que foi calculado, juntamente com o total.

Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch com suas modificações: git checkout -b minha-modificacao.
3. Faça o commit das suas alterações: git commit -m 'Adicionando nova funcionalidade'.
4. Faça o push para a sua branch: git push origin minha-modificacao.
5. Abra um pull request no repositório original.

Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

---

Desenvolvido por Jr_Tech_OFC.

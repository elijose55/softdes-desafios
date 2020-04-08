# Guia para a API

## Commands

* `http://0.0.0.0/` 

      **[GET]** - Carrega o pop-up de login inicialmente e caso já esteja logado carrega a pagina inicial mostrando os desafios disponíveis e envios.
      * Parameters: ID (Id do desafio a ser exibido) - Não obrigatório.

      **[POST]** - Envia o desafio carregado pelo aluno para o lambda.
      * Parameters: ID (Id do desafio que foi enviado)
      * Files: Arquivo da solução ao desafio.

* `http://0.0.0.0/pass` 

    **[GET]** - Carrega o pop-up de login inicialmente e caso já esteja logado a pagina para a troca de senha.

    **[POST]** - Realiza a troca de senha do usuário.
     * Form['old'] - Senha antiga inserida pelo usuario.
     * Form['new'] - Senha nova inserida pelo usuario.
     * Form['again'] - Senha nova repetida inserida pelo usuario.

* `http://0.0.0.0/logout` 

    **[GET]** - Desloga o usuario e carrega o index.html.

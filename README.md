# Implementação de serviço web RESTful

## Cenário

Implemente um microsserviço para gestão de dados de restaurante, considerando operações para inserção, consulta, atualização e remoção como descrito a seguir.
> O tipo de dados referentes a restaurante deve conter as seguintes propriedades.
> 
>  Os nomes estão em inglês porque estamos nos baseando em propriedades indicadas pelo padrão para descrição de restaurantes definidos em _schema.org.¹_

As propriedades obrigatórias de restaurante são:
- id: inteiro, identificador do restaurante gerado pelo serviço;
- name: texto, representa o nome do restaurante;
- address: representa a localização física do restaurante sendo um tipo complexo com as propriedades de um endereço postal (_PostalAddress_):
> - _postalCode_: texto, representa o código postal;
> 
> - _streetAddress_: texto, representa, por exemplo, a rua e o número onde o restaurante se localiza;
> 
> - _addressLocality_: texto, representa a cidade onde o restaurante se localiza;
>
> - _addressRegion_: texto, representa o estado onde o restaurante se localiza;
> 
> - _addressCountry_: texto, representa o país onde o restaurante se localiza.

No caso de país, pode-se usar a sigla do país (por exemplo, “USA”) ou a representação ISO-3166-1² em código de duas letras.

Outros campos de restaurante não obrigatórios são:
- url: texto, página web do restaurante;
- menu: texto, a url completa para o menu do restaurante;
- telephone: texto,
- priceRange: texto, corresponde ao intervalo de preço relativo. Usualmente é representado uma quantidade de sinais de moeda (por exemplo, “$$$”) ou um intervalo numérico (por exemplo, “$10-15”).
_________________________________________________________
¹https://schema.org/Restaurant
>
²https://en.wikipedia.org/wiki/ISO_3166-1


## Considerando este cenário, execute as seguintes tarefas:

1. Modele a estrutura dos dados providos pelo serviço, por exemplo, um
modelo Entidade-Relacionamento ou um modelo de classes _UML_.

2. Implemente um serviço _Web RESTful_ com operações para:
> - inserir um restaurante;
> - retornar todos os restaurantes;
> - retornar um restaurante pelo _id_;
> - consultar restaurante pelos atributos do endereço, por exemplo, consultar pela cidade retornando os restaurantes existentes na cidade;
> - atualizar restaurante, por exemplo, atualizar o endereço do restaurante;
> - apagar um restaurante pelo seu _id_.
  
4. (Opcional) Utilize um banco de dados para armazenar os dados.
   
6. Implemente um cliente (por exemplo, um script em _Python_ usando a biblioteca _requests_) que invoque este serviço simulando operações para inserção, consulta, atualização e remoção.

Observe que não é necessário criar um banco de dados para a solução desta tarefa. Pode-se utilizar um _mock_, por exemplo, implementando uma lista em memória.

### Sugestões

Na parte prática, considere os itens a seguir na sua resposta:

> 1. Modelo da estrutura de dados providos pelo serviço.
> 2. Explicação das modularizações implementadas, isto é, divisão do código em pacotes, tanto para cliente como para serviço;
> 3. Explicação das estruturas de dados implementadas, tanto para cliente como para serviço;
> 4. Explicação de como o serviço foi implementado, isto é, as etapas realizadas na implementação e o código em si;
> 5. Explicação de como o cliente foi implementado, isto é, as etapas realizadas na implementação e o código em si;
> 6. Explicação de como cliente e serviço se comunicam;
> 7. Incluir no arquivo de entrega o código comentado;
> 8. Incluir printscreens demonstrando o código em execução ou gravar vídeo apresentando a execução do serviço e a execução do cliente invocando o serviço.

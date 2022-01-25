

# Instalação de dependências iniciais
def code_1_0():
    """ pip install Flask Flask-Restful """


# Importação de biblioteca para criação de aplicação
def code_1_1():
    """ from flask import Flask """


# Aplicação - var
def code_1_2():
    """ app = Flask(__name__) """


# Importação de biblioteca para criação da API
def code_1_3():
    """ from flask_restful import Api """


# API - var
def code_1_4():
    """ api = Api(app) """


# BDD protótipo - var
def code_1_5():
    """
    hotels = [
        {
            'hotel_id': 'lucas',
            'nome': 'Hotel Lucas',
            'estrelas': 4.5,
            'diaria': 450,
            'cidade': 'Piauí'
        },
        {
            'hotel_id': 'farias',
            'nome': 'Hotel Farias',
            'estrelas': 4.6,
            'diaria': 460,
            'cidade': 'Pernambuco'
        },
        {
            'hotel_id': 'santos',
            'nome': 'Hotel Santos',
            'estrelas': 4.7,
            'diaria': 470,
            'cidade': 'Paraíba'
        },
    ]
    """


# Importação de biblioteca para criação de recursos
def code_1_6():
    """ from flask_restful import Resource """


# TODO: Classe BDD (herança de recurso) - criação - função GET: retorno BDD protótipo
def code_1_7():
    """
    class Hotels(Resource):

        def get(self):
            return {'hotels': hotels}
    """


# Classe BDD - importação
def code_1_8():
    """ from resources.hotel import Hotels """


# Classe BDD - endpoint - definição
def code_1_9():
    """ api.add_resource(Hotels, '/hoteis') """


# Aplicação - configuração de execução
def code_1_10():
    """
    if __name__ == '__main__':
        app.run(debug=True)
    """


# Aplicação - execução
def code_1_11():
    """ python app.py """


# POSTMAN - Classe BDD - requisição GET - testar retorno de função GET
def code_1_12():
    """ POSTMAN - nova coleção - requisição GET - http://127.0.0.1:5000/hoteis """


# POSTMAN - Classe CRUD - 4 requisições=GET/POST/PUT/DELETE - testar retorno de cada função CRUD
def code_1_13():
    """ POSTMAN - nova coleção - requisições GET/POST/PUT/DELETE - http://127.0.0.1:5000/hoteis/{hotel_id} """


# TODO: Classe CRUD (herança de recurso) - criação - função auxiliadora: find_pk()
def code_1_14():
    """
    class Hotel(Resource):

    @staticmethod
    def find_pk(_json_inner_key, _database, _searched_key):

        for _index in _database:
            if _index[_json_inner_key] == _searched_key:
                return _index
        return None
    """


# Classe CRUD - função GET - criação - auxiliada por: find_pk()
def code_1_15():
    """
    # Se a chave pk existir, retornar dados de um objeto específico, caso contrário, retornar erro
    def get(self, hotel_id):
        not_found = {'message': 'Hotel de id={} não foi encontrado.'.format(hotel_id)}

        this_hotel_object = Hotel.find_pk(_json_inner_key='hotel_id',
                                          _database=hotels,
                                          _searched_key=hotel_id)

        if this_hotel_object:
            return this_hotel_object
        return not_found['message'], 404
    """


# Classe CRUD - importação
def code_1_16():
    """ from resources.hotel import Hotel """


# Classe CRUD - endpoint - definição
def code_1_17():
    """ api.add_resource(Hotel, '/hoteis/<string:hotel_id>') """


# TODO: Classe modelo - criação - função auxiliadora: json()
def code_1_18():
    """
    class HotelModelo:

        def __init__(self, hotel_id: str, name: str, stars: float, daily_charge: float, city: str) -> None:
            self.__hotel_id = hotel_id
            self.__name = name
            self.__stars = stars
            self.__daily_charge = daily_charge
            self.__city = city

        def json(self):
            return {
                'hotel_id': self.__hotel_id,
                'name': self.__name,
                'stars': float(self.__stars),
                'daily_charge': float(self.__daily_charge),
                'city': self.__city
            }
    """


# Classe modelo - importação
def code_1_19():
    """
    from models.hotel import HotelModel
    """


# Classe CRUD - função auxiliadora: pass_arguments()
def code_1_20():
    """
    @staticmethod
    def pass_arguments(box_arguments):
        from flask_restful import reqparse

        arguments = reqparse.RequestParser()

        for field in box_arguments:
            arguments.add_argument(field)

        return arguments
    """


# BDD - importação
def code_1_21():
    """
    from database_test import hotels
    """


# Classe CRUD - função POST - criação - auxíliada por: find_pk(), pass_arguments()
def code_1_22():
    """
    # Se a chave pk existir, impedir de criar objeto, caso contrário, criar novo objeto
    def post(self, hotel_id):

        # Mensagens de tratamento
        repeated_id = {'message': 'O hotel com id={} já existe. Ele não pode ser criado.'.format(hotel_id)}
        add_success = {'message': 'O hotel com id={} foi adicionado conforme a seguir: '.format(hotel_id)}

        # Se a chave pk existir, a var recebe o objeto completo, caso contrário, a var recebe 'None'
        this_hotel_object = Hotel.find_pk(_json_inner_key='hotel_id',
                                          _database=hotels,
                                          _searched_key=hotel_id)

        # Impossibilitar a criação
        if this_hotel_object:
            return repeated_id['message'], 404
        # Possibilitar a criação
        else:
            fields = ['name', 'stars', 'daily_charge', 'city']
            content = Hotel.pass_arguments(box_arguments=fields)
            content = content.parse_args()
            new_hotel_object = HotelModel(hotel_id, **content)
            new_hotel_object_json = new_hotel_object.json()
            hotels.append(new_hotel_object_json)
            object_created = (add_success['message'], new_hotel_object_json)
            return object_created, 200
    """


# POSTMAN - função POST - uso
def code_1_22_ex():
    """
    http://127.0.0.1:5000/hoteis/sousa
    {
        "name": "Hotel Sousa",
        "stars": 4.8,
        "daily_charge": 480,
        "city": "Acre"
    }
    Se o último endereço da url já existir no banco protótipo  || não criação do objeto e mensagem de erro
    Se o último endereço da url não existir no banco protótipo || objeto adicionado ao banco protótipo
    """


# Classe CRUD - função PUT - auxiliada por: pass_arguments(), find_pk()
def code_1_23():
    """
    # Se a chave pk existir, editar dados do objeto, caso contrário, adicionar dados como novo objeto
    def put(self, hotel_id):

        # Mensagens de tratamento
        hotel_changed = {'message': 'O hotel com id={} foi modificado.'.format(hotel_id)}
        hotel_added = {'message': 'O hotel com id={} abaixo foi adicionado: '.format(hotel_id)}

        # Configuração do objeto json
        fields = ['name', 'stars', 'daily_charge', 'city']
        content = Hotel.pass_arguments(box_arguments=fields)
        content = content.parse_args()
        new_hotel_object = HotelModel(hotel_id, **content)
        new_hotel_object_json = new_hotel_object.json()

        # Se a chave pk existir, a var recebe o objeto completo, caso contrário, a var recebe 'None'
        this_hotel_object = Hotel.find_pk(_json_inner_key='hotel_id',
                                          _database=hotels,
                                          _searched_key=hotel_id)

        # Se "this_hotel_exists" achou o objeto, este será substituído pelo objeto criado em "new_hotel_object_json"
        if this_hotel_object:
            this_hotel_object.update(new_hotel_object_json)
            object_updated = (hotel_changed['message'], new_hotel_object_json)
            return object_updated, 200
        # Caso contrário, "new_hotel_object_json" é entendido como um novo objeto a ser adicionado ao BDD protótipo
        else:
            hotels.append(new_hotel_object_json)
            object_new = (hotel_added['message'], new_hotel_object_json)
            return object_new, 201
    """


# Classe CRUD - função DELETE - auxiliada por: find_pk()
def code_1_24():
    """
    def delete(self, hotel_id):

        global hotels

        # Mensagens de tratamento
        msg_hotel_erased = {'message': 'Hotel {} foi deletado'}
        msg_hotel_not_found = {'message': f'Hotel de id={hotel_id} não encontrado.'}

        # Se a chave pk existir, a var recebe o objeto completo, caso contrário, a var recebe 'None'
        this_hotel_object = Hotel.find_pk(_json_inner_key='hotel_id',
                                          _database=hotels,
                                          _searched_key=hotel_id)

        # Se a chave pk foi encontrada, criar 2 vars: mostrar o que foi deletado, recriar o banco sem o que foi deletado
        if this_hotel_object:
            hotel_deleted = [hotel for hotel in hotels if hotel['hotel_id'] == hotel_id]
            hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
            return msg_hotel_erased['message'].format(*hotel_deleted)
        else:
            return msg_hotel_not_found['message'], 404
    """

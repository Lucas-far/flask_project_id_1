

from flask_restful import Resource
from database_test import hotels
from models.hotel import HotelModel


class Hotels(Resource):

    def get(self):
        return {'hotels': hotels}


class Hotel(Resource):

    @staticmethod
    def pass_arguments(box_arguments):
        from flask_restful import reqparse

        arguments = reqparse.RequestParser()

        for field in box_arguments:
            arguments.add_argument(field)

        return arguments

    @staticmethod
    def find_pk(_json_inner_key, _database, _searched_key):

        for _index in _database:
            if _index[_json_inner_key] == _searched_key:
                return _index
        return None

    # Se a chave pk existir, retornar dados de um objeto específico, caso contrário, retornar erro
    def get(self, hotel_id):
        not_found = {'message': 'Hotel de id={} não foi encontrado.'.format(hotel_id)}

        this_hotel_object = Hotel.find_pk(_json_inner_key='hotel_id',
                                          _database=hotels,
                                          _searched_key=hotel_id)

        if this_hotel_object:
            return this_hotel_object
        return not_found['message'], 404

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

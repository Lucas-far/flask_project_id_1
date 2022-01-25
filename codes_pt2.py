

# SQLite3 - função: database_sqlite3_init - criação
def code_1_0():
    """
    def database_sqlite3_init(database_file_name: str):
        import sqlite3

        instance_ = sqlite3.connect(database_file_name)
        command_ = instance_.cursor()
        return instance_, command_
    """


# SQLite3 - função: create_sqlite3_database - criação
def code_1_1():
    """
    def create_sqlite3_database(database_name: str,
                            name_pk: str,
                            pk_type: str,
                            fields_list: list,
                            fields_list_len: int,
                            exec_,
                            instance_):

        invalid_table_size = 'Limite de campos para uma tabela excedidos: 10'
        table_created_success = '---------- TABELA CRIADA ----------\n{}'
        syntax_create_dtb = "CREATE TABLE IF NOT EXISTS {}({} {} PRIMARY KEY, ".format(database_name, name_pk, pk_type)
        closure = ")"
        fields = None

        if fields_list_len == 1:
            fields = "{}".format(fields_list)
        elif fields_list_len == 2:
            fields = "{} {}".format(*fields_list)
        elif fields_list_len == 3:
            fields = "{} {} {}".format(*fields_list)
        elif fields_list_len == 4:
            fields = "{} {} {} {}".format(*fields_list)
        elif fields_list_len == 5:
            fields = "{} {} {} {} {}".format(*fields_list)
        elif fields_list_len == 6:
            fields = "{} {} {} {} {} {}".format(*fields_list)
        elif fields_list_len == 7:
            fields = "{} {} {} {} {} {} {}".format(*fields_list)
        elif fields_list_len == 8:
            fields = "{} {} {} {} {} {} {} {}".format(*fields_list)
        elif fields_list_len == 9:
            fields = "{} {} {} {} {} {} {} {} {}".format(*fields_list)
        elif fields_list_len == 10:
            fields = "{} {} {} {} {} {} {} {} {} {}".format(*fields_list)
        else:
            print(invalid_table_size)

        syntax_create_dtb = syntax_create_dtb + fields + closure
        print(table_created_success.format(syntax_create_dtb))

        exec_.execute(syntax_create_dtb)
        instance_.commit()
        instance_.close()
    """


def code_1_1_ex():
    """
    if __name__ == '__main__':
        sqlite3_instance, sqlite3_command = database_sqlite3_init(database_file_name='sqlite3_database_1st.db')

        # Sintaxe para [fields_list]: nome + espaço + tipo + vírgula + espaço
            create_sqlite3_database(database_name='sqlite3_database_1st_hoteis',
                                    name_pk='hotel_id',
                                    pk_type='text',
                                    fields_list=['name text, ', 'stars real, ', 'daily_charge real, ', 'city text'],
                                    fields_list_len=4,
                                    exec_=sqlite3_command,
                                    instance_=sqlite3_instance)
    """


# SQLite3 - função: create_sqlite3_table_object - criação
def code_1_2():
    """
    def create_sqlite3_table_object(database_name: str, fields_list: list, fields_list_len: int, exec_, instance_):

        invalid_table_size = 'Limite de campos para uma tabela excedidos: 10'
        table_object_created_success = '---------- OBJETO DE TABELA CRIADO ----------\n{}'
        syntax_add = "INSERT INTO {} VALUES (".format(database_name)
        closure = ")"
        fields = None

        if fields_list_len == 1:
            fields = "'{}'".format(fields_list)
        elif fields_list_len == 2:
            fields = "'{}', '{}'".format(*fields_list)
        elif fields_list_len == 3:
            fields = "'{}', '{}', '{}'".format(*fields_list)
        elif fields_list_len == 4:
            fields = "'{}', '{}', '{}', '{}'".format(*fields_list)
        elif fields_list_len == 5:
            fields = "'{}', '{}', '{}', '{}', '{}'".format(*fields_list)
        elif fields_list_len == 6:
            fields = "'{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
        elif fields_list_len == 7:
            fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
        elif fields_list_len == 8:
            fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
        elif fields_list_len == 9:
            fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
        elif fields_list_len == 10:
            fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
        else:
            print(invalid_table_size)

        create_this_object = syntax_add + fields + closure
        print(table_object_created_success.format(create_this_object))

        exec_.execute(create_this_object)
        instance_.commit()
        instance_.close()
    """


def code_1_2_ex():
    """
    if __name__ == '__main__':
        # Sintaxe para [fields_list]: nome
        create_sqlite3_table_object(database_name='sqlite3_database_1st_hoteis',
                                    fields_list=['legado', 'hotel legado', '4.9', '344', 'Uruçuí'],
                                    fields_list_len=5,
                                    exec_=sqlite3_command,
                                    instance_=sqlite3_instance)
    """

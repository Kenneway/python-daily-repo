class Column:

    def __init__(self,
                 column_name,
                 column_type,
                 default=None,
                 not_null=False,
                 auto_inc=False,
                 unique=False,
                 primary_key=False):
        self.column_name = column_name
        self.column_type = column_type
        self.default = default
        self.not_null = not_null
        self.auto_inc = auto_inc
        self.unique = unique
        self.primary_key = primary_key


class Table:

    def __init__(self,
               table_name,
               column_list,
               engine='InnoDB',
               auto_increment=1,
               default_charset='utf8'):
        self.table_name = table_name
        self.column_list = column_list
        self.engine = engine
        self.auto_increment = auto_increment
        self.default_charset = default_charset

















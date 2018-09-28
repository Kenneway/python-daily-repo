import sql_utils
from table_entity import Table
from table_entity import Column


def create_table(table_name, column_list):
    column_entries = ""
    if column_list is None or len(column_list) == 0:
        return
    else:
        for column in column_list:
            column_clause = column.column_name + " " + column.column_type
            if column.not_null is True:
                column_clause += " NOT NULL"
            if column.auto_inc is True:
                column_clause += " AUTO_INCREMENT"
            if column.primary_key is True:
                column_clause += " PRIMARY KEY"
            if column.default is not None:
                column_default = sql_utils.sql_value_format(column.default)
                column_clause += " DEFAULT " + column_default
            column_entries += column_clause + ","
        print column_entries
        column_entries = column_entries.strip(",")
        print column_entries
    sql = "CREATE TABLE %s(%s) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8" % (table_name, column_entries)
    sql_utils.exe(sql)


def drop_table(table_name):
    sql = "drop table %s" % table_name
    sql_utils.exe(sql)


if __name__ == "__main__":
    # column_list = []
    # column_list.append(Column("id", "INT(13)", None, False, True, False, True))
    # column_list.append(Column("name", "VARCHAR(50)", None, True, False, False, False))
    # create_table("test", column_list)

    # c = Column("id", "INT(13)", None, False, True, False, True)
    # print c.column_name

    drop_table("test")





import sql_utils


def insert(table_name, columns):
    if columns is None or len(columns) == 0:
        print("Columns is None or len(columns) == 0")
        return
    keys = ""
    values = ""
    for key, value in columns.iteritems():
        keys = keys + key + ","
        if isinstance(value, str):
            values += "\'" + value + "\',"
        elif sql_utils.is_number(str(value)):
            values += str(value) + ","
        else:
            print("Input is not valid")
            return
    keys = keys.strip(',')
    values = values.strip(',')

    sql = "insert into %s(%s) value(%s)" % (table_name, keys, values)
    sql_utils.exe(sql)


def update_by_id(table_name, columns, id):
    # deal with columns to update
    if columns is None or len(columns) == 0:
        print("Columns is None or len(columns) <= 1")
        return
    update_columns = ""
    for key, value in columns.iteritems():
        update_columns += key + "=" + sql_utils.sql_value_format(value) + ","
    update_columns = update_columns.strip(',')
    # deal with sql
    sql = "update %s set %s where id=%s" % (table_name, update_columns, id)
    sql_utils.exe(sql)


def update_where_condition(table_name, columns, where_conditions=None):
    # deal with columns to update
    update_columns = ""
    if columns is None or len(columns) == 0:
        print("Columns is None or len(columns) == 0")
        return
    else:
        for key, value in columns.iteritems():
            update_columns += key + "=" + sql_utils.sql_value_format(value) + ","
        update_columns = update_columns.strip(',')
    # deal with where condition
    where_clause = ""
    if where_conditions is not None and len(where_conditions) >= 1:
        where_clause = "where " + where_conditions[0]
        for i in range(1, len(where_conditions)):
            where_clause += " and " + where_conditions[i]
    # deal with sql
    sql = "update %s set %s %s" % (table_name, update_columns, where_clause)
    sql = sql.strip()
    sql_utils.exe(sql)


def select_all(table_name):
    sql = "select * from %s" % table_name
    return sql_utils.exe(sql)


def select_by_id(table_name, id):
    sql = "select * from %s where id=%s" % (table_name, id)
    return sql_utils.exe(sql)


if __name__ == "__main__":
    pass
    # column_list = []
    # column_list.append(Column("id", "INT(13)", None, False, True, False, True))
    # column_list.append(Column("name", "VARCHAR(50)", None, True, False, False, False))
    # create_table("test", column_list)

    # c = Column("id", "INT(13)", None, False, True, False, True)
    # print c.column_name







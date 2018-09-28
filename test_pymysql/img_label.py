import math
import sql_utils
import table_ops
import data_ops
from table_entity import Column


# arrange theme class
def arrange_theme_class():
    for theme_id in range(1, 41):
        sample_label_table = "sample_" + str(theme_id) + "_label"
    rows = data_ops.select_all(sample_label_table)
    for row in rows:
        class_id = row["class_id"]
        print theme_id, class_id
        columns = {}
        columns["theme_id"] = theme_id
        columns["class_id"] = class_id
        data_ops.insert("img_theme_class", columns)


# clean sample_n
def clean_sample_n():
    for theme_id in range(2, 41):
        table_name = "sample_%d" % theme_id
    columns = {}
    columns["sample_label"] = ""
    data_ops.update_where_condition(table_name, columns)


# drop sample_n_label
def clean_sample_n_label():
    for theme_id in range(1, 41):
        table_name = 'sample_%s_label' % theme_id
        table_ops.drop_table(table_name)


# create sample_n_label
def create_sample_n_label():

    column_list = []
    column_list.append(Column("id", "INT(13)", None, False, True, False, True))
    column_list.append(Column("sample_id", "INT(13)", None, True, False, False, False))
    column_list.append(Column("class_id", "INT(13)", None, True, False, False, False))
    column_list.append(Column("label_user_id", "INT(13)", 0, True, False, False, False))
    column_list.append(Column("label_data", "LONGTEXT", None, False, False, False, False))
    column_list.append(Column("check_user_id", "INT(13)", 0, True, False, False, False))
    column_list.append(Column("check_data", "LONGTEXT", None, False, False, False, False))
    column_list.append(Column("status", "INT(10)", 0, True, False, False, False))
    column_list.append(Column("update_time", "INT(13)", 0, True, False, False, False))

    for theme_id in range(1, 41):
        table_name = 'sample_%s_label' % theme_id
        table_ops.create_table(table_name, column_list)


# alter sample_n
def alter_sample_n():

    for theme_id in range(1, 41):
        table_name = "sample_%d" % theme_id
        sql1 = "ALTER TABLE %s CHANGE sample_id id INT(10) unsigned AUTO_INCREMENT" % table_name
        print sql1
        sql_utils.exe(sql1)
        sql2 = "ALTER TABLE %s CHANGE sample_path path VARCHAR(500) NOT NULL" % table_name
        print sql2
        sql_utils.exe(sql2)
        sql3 = "ALTER TABLE %s CHANGE sample_label label LONGTEXT" % table_name
        print sql3
        sql_utils.exe(sql3)


# truncate sample_1_label
def truncate_sample_n_label():
    sql = "truncate table sample_1_label"
    sql_utils.exe(sql)


# fill sample_n_label
def fill_sample_n_label():

    for theme_id in range(1, 41):
        # deal with sample_n_table
        sample_n_table = "sample_%d" % theme_id
        sql1= "select id from %s" % sample_n_table
        sample_id_list = sql_utils.exe(sql1)
        # print sample_id_list

        # deal with img_theme_class
        sql2= "select class_id from img_theme_class where theme_id = %d" % theme_id
        class_id_list = sql_utils.exe(sql2)
        # print class_id_list

        # deal with sample_n_label_table
        sample_n_label_table = "sample_%d_label" % theme_id
        sql3 = "insert into " + sample_n_label_table + "(sample_id, class_id) value(%s, %s)"
        params_all = []
        for sample_id_dict in sample_id_list:
            for class_id_dict in class_id_list:
                sample_id = sample_id_dict["id"]
                class_id = class_id_dict["class_id"]
                params_all.append( (sample_id, class_id) )
        size = len(params_all)
        batch = 10000
        batch_num = int(math.ceil(float(size)/batch))
        for i in range(batch_num):
            params = params_all[i*batch: min((i+1)*batch, size)]
            # print params
            sql_utils.exe_many(sql3, params)


# check sample_n_label
def check_sample_n_label():

    for theme_id in range(1, 41):
        # deal with sample_n_table
        sample_n_table = "sample_%d" % theme_id
        sql1= "select id from %s" % sample_n_table
        sample_id_list = sql_utils.exe(sql1)

        # deal with img_theme_class
        sql2= "select class_id from img_theme_class where theme_id = %d" % theme_id
        class_id_list = sql_utils.exe(sql2)
        # print class_id_list

        # deal with sample_n_label_table
        sample_n_label_table = "sample_%d_label" % theme_id
        sql3 = "select id from %s" % sample_n_label_table
        label_id_list = sql_utils.exe(sql3)

        if len(sample_id_list) * len(class_id_list) == len(label_id_list):
            print "===========", True
        else:
            print "===========", False

# ALTER TABLE sample_2_label MODIFY update_time BIGINT NOT NULL DEFAULT '0';
def alter_int_to_bigint():

    for theme_id in range(2, 41):
        table_name = "sample_%d_label" % theme_id
        sql1 = "ALTER TABLE %s MODIFY update_time BIGINT NOT NULL DEFAULT '0'" % table_name
        sql_utils.exe(sql1)


def clean_sample_n_label_last():

    for theme_id in range(1, 41):
        table_name = "sample_%d_label" % theme_id
        sql1 = "update %s set label_user_id=0,label_data='',check_user_id=0,check_data='',status=0,update_time=0" % table_name
        sql_utils.exe(sql1)




if __name__ == '__main__':

    # pass
    # create_sample_n_label()
    # alter_sample_n()
    # fill_sample_n_label()
    # truncate_sample_n_label()
    # print int(math.ceil(float(5)/ 2))
    # print 5/2 + 1
    # check_sample_n_label()
    # alter_int_to_bigint()
    clean_sample_n_label_last()

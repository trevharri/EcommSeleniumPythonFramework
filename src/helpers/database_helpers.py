import pymysql
from ssqatest.src.helpers.config_helpers import get_database_credentials
from ssqatest.src.configs.generic_configs import GenericConfigs

def read_from_db(sql):
    db_info = get_database_credentials()
    connection = pymysql.connect(host=db_info['db_host'], port=db_info['db_port'], user=db_info["db_user"],
                                 password=db_info['db_password'])

    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return db_data


def get_order_from_db_by_order_no(order_no):
    schema = GenericConfigs.DATABASE_SCHEMA
    sql = f"SELECT * FROM {schema}.wp_posts WHERE ID = {order_no} AND post_type = 'shop_order';"
    row = read_from_db(sql)
    return row


def get_item_from_db_by_order_no(order_no):
    schema = GenericConfigs.DATABASE_SCHEMA
    sql = f"SELECT * FROM {schema}.wp_woocommerce_order_items WHERE order_id={order_no} AND order_item_type" \
          f"='line_item';"
    row = read_from_db(sql)
    item_name = row[0]['order_item_name']
    return item_name

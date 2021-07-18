from sql_connection import get_sql_connection

def get_all_products(connection):



    cursor=connection.cursor()

    query = ("SELECT products.product_id, products.namel, products.uom_id, products.location, uom.uom_name "
    "FROM products inner join uom on products.uom_id=uom.uom_id;")

    cursor.execute(query)

    response = []
    for(product_id, namel, uom_id, location,uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': namel,
                'uom_id': uom_id,
                'uom_name': uom_name
            }
        )


    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(namel, uom_id, location)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['location'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 9))
from connection import db


def get_conditions():
    # sql = ("SELECT upk.user_id, upk.id, p.product_url, p.product_name, k.keyword "
    #        "FROM user_product_keyword as upk "
    #        "JOIN product_keyword pk ON upk.product_keyword_id = pk.id "
    #        "JOIN product p ON pk.product_id = p.id "
    #        "JOIN keyword k ON pk.keyword_id = k.id "
    #        "ORDER BY upk.user_id ASC;")

    sql = ("SELECT upk.user_id, upk.id, p.product_url, p.product_name, k.keyword "
           "FROM user_product_keyword as upk "
           "JOIN product_keyword pk ON upk.product_keyword_id = pk.id "
           "JOIN product p ON pk.product_id = p.id "
           "JOIN keyword k ON pk.keyword_id = k.id "
           "WHERE upk.user_id = 1 "
           "ORDER BY upk.user_id ASC;")
    cursor = db.cursor()
    cursor.execute(sql)
    p_list = cursor.fetchall()

    product_list = []
    for item in p_list:
        data = {
            "user_id": item[0],
            "upk_id": item[1],
            "p_url": item[2],
            "p_user_name": item[3],
            "keyword": item[4],
            "m_url": "",
            "m_name": "",
            "p_name": "",
            "result": "",
        }
        product_list.append(data)
    return product_list


# ===========================================================================================

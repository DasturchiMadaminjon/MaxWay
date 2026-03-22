from django.db import connection
from contextlib import closing

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM dashboard_category")
        return dictfetchall(cursor)

def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT p.*, c.name as category_name 
            FROM dashboard_product p 
            JOIN dashboard_category c ON p.category_id = c.id
        """)
        return dictfetchall(cursor)

def get_orders():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT o.*, cust.name as customer_name, t.name as table_name
            FROM dashboard_order o
            JOIN dashboard_customer cust ON o.customer_id = cust.id
            LEFT JOIN dashboard_tableitem t ON o.table_id = t.id
            ORDER BY o.created_at DESC
        """)
        return dictfetchall(cursor)

def get_branches():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM dashboard_branch")
        return dictfetchall(cursor)

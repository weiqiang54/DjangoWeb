import pymysql
from django.db.backends.mysql.operations import DatabaseOperations


def last_executed_query(self, cursor, sql, params):
    # With MySQLdb, cursor objects have an (undocumented) "_executed"
    # attribute where the exact query sent to the database is saved.
    # See MySQLdb/cursors.py in the source distribution.
    query = getattr(cursor, '_executed', None)
    if query is not None:
        query = query.encode(errors='replace')
    return query


def install_pymysql():
    pymysql.version_info = (1, 3, 15, "final", 0)
    pymysql.install_as_MySQLdb()
    DatabaseOperations.last_executed_query = last_executed_query


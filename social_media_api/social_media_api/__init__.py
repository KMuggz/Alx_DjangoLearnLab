import pymysql
import sys

# this line is non-negotiable for PyMySQL to work with Django
pymysql.version_info = (2, 2, 7, "final", 0)
pymysql.install_as_MySQLdb()

try:
    from MySQLdb.constants import CLIENT

    if not hasattr(CLIENT, "LONG_PASSWORD"):
        CLIENT.LONG_PASSWORD = 1
except ImportError:
    pass
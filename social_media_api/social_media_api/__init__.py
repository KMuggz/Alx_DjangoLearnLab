import pymysql

# this line is non-negotiable for PyMySQL to work with Django
pymysql.install_as_MySQLdb()
import torndb

from tornado.options import define, options

# Database connection setup
define("mysql_host", default="127.0.0.1:3306", help="application database host")
define("mysql_database", default="text_analyzer", help="application database name")
define("mysql_user", default="text_analyzer", help="application database user")
define("mysql_password", default="text_analyzer", help="database password")

db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password
    )

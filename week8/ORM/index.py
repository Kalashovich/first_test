# ORM (Object Realitional Mapping, Объектно-реализационное отображение) - технология программирования, благодаря которой разработкчики могут использовать язык программирования, с которым им удобно работать с базой данных вместо написания операторов SQL, это очень сильно ускоряет разаработку приложения и ОД, особенно на начальных этапах.


from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm',
    user = 'kalashovich',
    password = '1',
    host = 'localhost',
    port = 5432
      
)
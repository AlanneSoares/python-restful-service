import

connection = mysql.connector.connect(host='localhost', user='usuário do mysql', password='senha do mysql', database='nome da base do mysql')
cursor = connection.cursor()

### crud ###

## create - fetchall
product = "Chocolate"
value = 15
insertSql = f'INSERT INTO TABLE(product, value) VALUES({product}, {value})'
cursor.execute(insertSql)
cursor.close()
connection.commit()

## read
selectSql = f'SELECT * FROM TABLE'
cursor.execute(selectSql)
result = cursor.fetchall()
print(result)
cursor.close()
connection.close()

## update - commit
updateSql = f'UPDATE TABLE SET VALUE = {value} WHERE PRODUCT = "{product}"'
cursor.execute(updateSql)
connection.commit()
cursor.close()
connection.close()

## delete
deleteSql = f'DELETE FROM TABLE WHERE PRODUCT = "{product}"'
cursor.execute(deleteSql)
connection.commit()
cursor.close()
connection.close()
import glob
import csv
import mysql.connector
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

db_config = {
    'host': '34.125.100.233',
    'user': 'bf',
    'passwd': 'bfa1b2c3d4*',
    'database': 'BolsaFamilia'
}

# Template HTML para a página
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Consulta SQL</title>
</head>
<body>
    <h2>Executar Consulta SQL</h2>
    <form method="POST">
        <textarea name="sql_query" rows="21" cols="150">{{ sql_query if sql_query else '' }}</textarea><br>
        <input type="submit" value="Executar">
    </form>
    {% if result %}
        <h3>Resultados:</h3>
        <table border="1">
        {% for row in result %}
            <tr>
            {% for item in row %}
                <td>{{ item }}</td>
            {% endfor %}
            </tr>
        {% endfor %}
        </table>
    {% endif %}
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def query_interface():
    result = None
    sql_query = ""

    if request.method == 'POST':
        sql_query = request.form['sql_query']
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchmany(100)  # Limita a 100 resultados
            cursor.close()
            conn.close()
        except Exception as e:
            result = [("Erro:", str(e))]

    return render_template_string(HTML_TEMPLATE, result=result, sql_query=sql_query)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001) 
    
    
    
    
# exemplos de consultas Mysql/Mariadb

'' '''
SELECT NomeMunicipioSIAFI, COUNT(DISTINCT CPFBeneficiario) AS NumeroBeneficiarios
FROM Saques
GROUP BY NomeMunicipioSIAFI;

# informações sobre o banco 

SELECT 
    TABLES.TABLE_NAME AS 'Table',
    COLUMNS.COLUMN_NAME AS 'Column',
    COLUMNS.COLUMN_TYPE AS 'Data Type',
    COLUMNS.IS_NULLABLE AS 'Is Nullable',
    CASE
        WHEN KEY_COLUMN_USAGE.CONSTRAINT_NAME = 'PRIMARY' THEN 'YES'
        ELSE 'NO'
    END AS 'Primary Key'
FROM 
    INFORMATION_SCHEMA.TABLES
JOIN 
    INFORMATION_SCHEMA.COLUMNS ON TABLES.TABLE_NAME = COLUMNS.TABLE_NAME
LEFT JOIN 
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE ON TABLES.TABLE_NAME = KEY_COLUMN_USAGE.TABLE_NAME
    AND COLUMNS.COLUMN_NAME = KEY_COLUMN_USAGE.COLUMN_NAME
WHERE 
    TABLES.TABLE_SCHEMA = 'BolsaFamilia' AND COLUMNS.TABLE_SCHEMA = 'BolsaFamilia'
ORDER BY 
    TABLES.TABLE_NAME, COLUMNS.ORDINAL_POSITION;



#Total de Pagamentos por Estado:

SELECT UF, SUM(ValorParcela) AS TotalSaques
FROM Saques
GROUP BY UF
ORDER BY SUM(ValorParcela) DESC
LIMIT 100000;





''' ''


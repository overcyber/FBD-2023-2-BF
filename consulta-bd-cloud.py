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
        <textarea name="sql_query" rows="20" cols="150">{{ sql_query if sql_query else '' }}</textarea><br>
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

    return render_template_string(HTML_TEMPLATE, result=result)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001) 
    
    
    
    
# exemplos de consultas 

'' '''
SELECT NomeMunicipioSIAFI, COUNT(DISTINCT CPFBeneficiario) AS NumeroBeneficiarios
FROM Saques
GROUP BY NomeMunicipioSIAFI;
''' ''
 

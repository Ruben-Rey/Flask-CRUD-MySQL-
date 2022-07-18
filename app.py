
from crypt import methods
from math import prod
from pickletools import markobject
from pydoc import describe
from sqlite3 import Cursor
from flask import Flask, render_template,request,redirect,url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactosdb'
mysql = MySQL(app)




app.secret_key="silabuz123"

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contactos")
    data = cursor.fetchall()
    return render_template('index.html', contactos=data)



@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nom = request.form['nombres']
        tel = request.form['telefono']
        email = request.form['email']


        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO contactos (nombres,telefono,email) VALUES ('{nom}','{tel}','{email}')")
        cursor.connection.commit()
        flash('Contacto agregado exitosamente')
        return redirect(url_for('index'))


@app.route('/edit/<id>')
def edit_contact(id):

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM contactos WHERE id={id}")
    data = cursor.fetchall()

    return render_template('edit.html', contacto=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        nom = request.form['nombres']
        tel = request.form['telefono']
        email = request.form['email']

        cursor = mysql.connection.cursor()    
        cursor.execute(f"UPDATE contactos SET nombres=\"{nom}\", telefono=\"{tel}\", email=\"{email}\" WHERE id=\"{id}\"")
        cursor.connection.commit()

        return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
         
        cursor = mysql.connection.cursor()
        cursor.execute(f"DELETE FROM contactos WHERE id={id}")
        cursor.connection.commit()
        flash('Contacto Eliminado exitosamente')
        return redirect(url_for('index'))




@app.route('/productos')  
def productos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos")
    data = cursor.fetchall()
    return render_template('productos.html', productos=data)


@app.route('/form_add_product')
def form_add_product():

    return render_template('form_add_product.html')


@app.route('/add_product', methods=['POST'])
def add_product():

    if request.method == 'POST':
        prod = request.form['producto']
        des = request.form['descripcion']
        mar = request.form['marca']
        pre = request.form['precio']
        sto = request.form['stock']

        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO productos (producto,description,marca,precio,stock) VALUES ('{prod}', '{des}','{mar}','{pre}','{sto}')")
        cursor.connection.commit()
        return redirect(url_for('productos'))

@app.route('/edit_product/<id>')
def edit_product(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM productos WHERE id={id}")
    data = cursor.fetchall()

    return render_template('edit_product.html', producto=data[0])


@app.route('/update_product/<id>', methods=['POST'])
def update_product(id):
    if request.method == 'POST':
        prod = request.form['producto']
        des = request.form['descripcion']
        mar = request.form['marca']
        pre = request.form['precio']
        sto = request.form['stock']

        cursor = mysql.connection.cursor()
        cursor.execute(f"UPDATE productos SET producto=\"{prod}\", description=\"{des}\", marca=\"{mar}\", precio=\"{pre}\", stock=\"{sto}\" WHERE id=\"{id}\"")
        flash('La actualizacion de registro fue exitosa')
        cursor.connection.commit()

        return redirect(url_for('productos'))


@app.route('/delete_product/<id>')
def delete_product(id):

    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM productos WHERE id={id}")
    cursor.connection.commit()
    flash('Eliminaciòn exitosa')
    return redirect(url_for('productos'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)



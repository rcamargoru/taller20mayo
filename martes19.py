import sqlite3
c=0
#conexion db
def conectar_db():
    return sqlite3.connect('uninpahu.db')

#Nuevo usuario
def nuevou(cod, nom):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO usuarios (cod, nom)
    VALUES (?, ?)
    ''', (cod, nom))
    conn.commit()
    conn.close()

#Consultar todos
def consultar_todos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

#Consultar un usuario
def consultar_x_cod(cod):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE cod = ?', (cod,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

#Actualizar nombre de usuario
def modif_usuario(cod, nuevo_nom):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE usuarios
    SET nom = ?
    WHERE cod = ?
    ''', (nuevo_nom, cod))
    conn.commit()
    conn.close()

#Eliminar usuario
def elim_usuario(cod):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE cod = ?', (cod,))
    conn.commit()
    conn.close()

def menu(c):
        while c!=6:
            match c:
                case 1:
                    print("Consultando todos los usuarios:")
                    usuarios = consultar_todos()
                    if usuarios:
                        for usuario in usuarios:
                            print(usuario)
                    else:
                        print("No hay usuarios en la base de datos.")
                case 2:
                    cod = int(input("Digite el código del usuario a consultar: "))
                    usuario = consultar_x_cod(cod)
                    if usuario:
                        print(f"Usuario encontrado: {usuario}")
                    else:
                        print(f"No se encontró un usuario con el código {cod}.")
                case 3:
                    cod = int(input("Digite el código del nuevo usuario: "))
                    nom = input("Digite el nombre del nuevo usuario: ")
                    nuevou(cod, nom)
                    print(f"Usuario con código {cod} y nombre {nom} ha sido creado.")
                case 4:
                    cod = int(input("Digite el código del usuario a modificar: "))
                    nuevo_nom = input("Digite el nuevo nombre del usuario: ")
                    modif_usuario(cod, nuevo_nom)
                    print(f"Usuario con código {cod} ha sido actualizado.")
                case 5:
                    cod = int(input("Digite el código del usuario a eliminar: "))
                    elim_usuario(cod)
                    print(f"Usuario con código {cod} ha sido eliminado.")
                case 6:
                    print("Saliendo del programa...")
                    break
            c = int(input(
                "Digite 1 para Consultar todos los usuarios\n"
                "Digite 2 para consultar un usuario\n"
                "Digite 3 para crear un usuario\n"
                "Digite 4 para modificar un usuario\n"
                "Digite 5 para eliminar un usuario\n"
                "Digite 6 para salir\n"))




c = int(input(
    "Digite 1 para Consultar todos los usuarios\n"
    "Digite 2 para consultar un usuario\n"
    "Digite 3 para crear un usuario\n"
    "Digite 4 para modificar un usuario\n"
    "Digite 5 para eliminar un usuario\n"
    "Digite 6 para salir\n"))
menu(c)

from flask import Flask,Response
app = Flask(__name__)

@app.route("/")
def html():
	return """
	<html>
	<head>
	</head>
	<body>
	<p>Esto es una pagina estática con una imagen</p>
	<p><img SRC="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Sasso_lungo_da_passo_pordoi.jpg/270px-Sasso_lungo_da_passo_pordoi.jpg"</p>
	</body>
	</html>
	"""

@app.route('/user/<username>')
def mostrarPerfilUsuario(username):
    # Mostrar el perfil de usuario
    return 'Hola %s' % username

@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)

from django.shortcuts import HttpResponse, redirect # agrega redirección a la declaración de importación
def some_method(request):
	return redirect("/") 
#/blogs - muestra el string "placeholder para luego mostrar una lista de todos los blogs" con un método llamado "index"
def root(request):
    return redirect("/blogs")
#/blogs/new - muestra el string "placeholder para mostrar un nuevo formulario para crear un nuevo blog" con un método llamado "new"
def index(request):
    return HttpResponse(f'<h2>placeholder para luego mostrar una lista de todos los blogs<h2>')
#/blogs/new - muestra el string "placeholder para mostrar un nuevo formulario para crear un nuevo blog" con un método llamado "new"
def new(request):
    return HttpResponse(f'<p>placeholder para mostrar un nuevo formulario para crear un nuevo blog con un método llamado "new"<p>')
#/blogs/create - redirige a la ruta "/" con un método llamado "create"
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f'<h1>placeholder para mostrar el blog numero {number}</h1>')
def edit(request, number):
    return HttpResponse(f'<h1>placeholder para editar el blog {number}" con un método llamado "edit"</h1>')
def destroy(request, number):
    return redirect('/blogs')
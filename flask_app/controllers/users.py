from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def dashboard():
    return render_template('dashboard.html', users=User.get_all())

@app.route('/users/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect("/")

@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    return render_template('show_user.html', user=User.get_one(data))

#Show edit form
@app.route('/users/<int:id>/edit')
def show_edit_form(id):
    data = {
        "id": id
    }
    return render_template('edit_user.html', user=User.get_one(data))

#Executes the edit form
@app.route('/users/<int:id>/update', methods=['POST'])
def update_user():
    User.update(request.form)
    redirect('/')

#Show delete form
@app.route('/users/<int:id>/delete')
def show_delete_form(id):
    data = {
        "id": id
    }
    return render_template('delete_user.html', user=User.get_one(data))

#Executes the delete form
@app.route('/users/<int:id>/destroy', methods=['POST'])
def delete_user(id):
    User.delete(request.form)
    return redirect('/')

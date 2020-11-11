from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import TodoForm, OrderingForm
from application.models import Todos


@app.route('/', methods=['POST', 'GET'])
def index():
    form = OrderingForm()
    total = {
        'complete': Todos.query.filter_by(completed=True).count(),
        'all': Todos.query.count()
    }
    todos = []
    if form.order.data == 'new':
        todos = Todos.query.order_by(Todos.id.desc()).all()
    elif form.order.data == 'completed':
        todos = Todos.query.order_by(Todos.completed.desc()).all()
    elif form.order.data == 'incomplete':
        todos = Todos.query.order_by(Todos.completed.asc()).all()
    elif form.order.data == 'old':
        todos = Todos.query.order_by(Todos.id.asc()).all()
    else:
        todos = Todos.query.all()

    return render_template('list.html', todos=todos, form=form, total=total)


@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = TodoForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            todo = Todos(name=name)
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    form = TodoForm()
    current = Todos.query.get(id)
    if request.method == 'GET':
        form.name.data = current.name
    if request.method == 'POST':
        current.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


@app.route('/complete/<int:id>')
def complete(id):
    current = Todos.query.get(id)
    current.completed = True
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/incomplete/<int:id>')
def incomplete(id):
    current = Todos.query.get(id)
    current.completed = False
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/delete/<int:id>')
def delete(id):
    current = Todos.query.get(id)
    group = Groups.query.get(event_id=id)
    db.session.delete(current)
    db.session.commit()
    return(redirect(url_for('index')))

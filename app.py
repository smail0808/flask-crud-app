from flask import Flask, render_template, url_for, request, redirect
from snacks import Snacks
from flask_modus import Modus

app = Flask(__name__)

modus = Modus(app)

vimper = Snacks('viapper', 'animal')
snacks = [vimper]


def find_snak(snack_id):
    return [snack for snack in snacks if snack.id == snack_id][0]


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/snacks', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_snack = Snacks(request.form['name'], request.form['kind'])
        snacks.append(new_snack)
        return redirect(url_for('index'))
    return render_template('index.html', snacks=snacks)


@app.route('/snacks/new')
def new():
    return render_template('new.html')


@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    fn_snack = find_snak(id)
    if request.method == b'PATCH':
        fn_snack.name = request.form['name']
        fn_snack.kind = request.form['kind']
        return redirect(url_for('index'))

    if request.method == b'DELETE':
        snacks.remove(fn_snack)
        return redirect('/')

    return render_template('show.html', snack=fn_snack)


@app.route('/snacks/<int:id>/edit')
def edit(id):
    fn_snack = find_snak(id)
    return render_template('edit.html', snack=fn_snack)


if __name__ == '__main__':
    app.run(debug=True)

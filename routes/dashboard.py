from flask import Blueprint, render_template

dashboardBp = Blueprint('dashboard', __name__)
questionReviserBP = Blueprint('questionReviser',__name__)
statisticsBP = Blueprint('statistics',__name__)



@dashboardBp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@questionReviserBP.route('/questionReviser')
def questionReviser():
    return render_template('questionReviser.html')

@statisticsBP.route('/statistics')
def statistics():
    return render_template('statistics.html')
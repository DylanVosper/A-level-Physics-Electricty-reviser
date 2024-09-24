from flask import Blueprint, render_template

dashboardBp = Blueprint('dashbaord', __name__)

@dashboardBp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
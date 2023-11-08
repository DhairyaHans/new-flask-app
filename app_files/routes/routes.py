from flask import render_template, flash, request,redirect,url_for
from app_files.forms.app_login_form import LoginForm
from app_files.forms.app_register_form import RegisterForm
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import text
import os
from app_files.models.models import Login, Register
from app_files import app, db



# Login page
@app.route('/', methods=['GET','POST'])
def login():
    if current_user.is_authenticated==False:
        form = LoginForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                username = form.username.data
                password = form.password.data

                result = Login.query.filter_by(username=username).first()


                if result :
                    if result.username == username and result.password == password :
                        if result.designation == 'admin' :
                            login_user(result)
                            return redirect(url_for('details_of_admin'))
                        elif result.designation == 'emp' :
                            login_user(result)
                            return redirect(url_for('details_of_employee'))
                    else :
                            flash(f"There was an error with login: ['Username or Password does not exist'] ")
                else :
                    flash(f"There was an error with login: ['Username or Password does not exist'] ")
                

            # Catching Errors and showing themin flash warnings
            if form.errors != {} :
                for err_msg in form.errors.values() :
                    flash(f'There was an error with login: {err_msg} ')
    

        return render_template('login_screen.html',form=form)
    else:
        return render_template('invalid_page.html')

        

# Registration Page
@app.route('/register', methods=['GET','POST'])
@login_required
def register_employee():
    if current_user.designation=='admin':
        register_form = RegisterForm()
        if request.method == 'POST' :
            if register_form.validate_on_submit():
                firstname = register_form.firstname.data
                lastname = register_form.lastname.data
                dob = request.form['birthday']
                gender = request.form.get('gender')
                email = register_form.email.data
                phone = register_form.phone.data
                address = register_form.address.data

                res1 = Login.query.filter_by(username=email).first()
                res2 = Register.query.filter_by(email=email).first()

                if request.form['birthday'] == '' :
                    flash(f"There was an error with registration: ['Invalid Date'] ")
                else:
                    if not res1 and not res2 :
                        entry = Register(firstname=firstname, lastname=lastname, dob=dob, gender=gender, email=email, ph_no=phone, address=address)
                        db.session.add(entry)
                        db.session.commit()

                        #  PASSWORD GENERATION           
                        password = os.urandom(5).hex()

                        loginEntry = Login(username=email,password=password,designation='emp')
                        db.session.add(loginEntry)
                        db.session.commit()
                        flash(f"Success !!! USERNAME : {email} and PASSWORD : {password}")

                    
                    else :
                        flash(f"There was an error with Registeration: ['Username exists'] ")
                    

            

            # Catching Errors and showing themin flash warnings
            if register_form.errors != {} :
                for err_msg in register_form.errors.values() :
                    flash(f'There was an error with registration: {err_msg} ')

        return render_template('register_employee_screen.html',form=register_form)
    else:
        return render_template('invalid_page.html')

# Details of User(admin)
@app.route('/detailsAdmin')
@login_required
def details_of_admin():
    if current_user.designation=='admin':
        details = Register.query.filter_by(email=current_user.username).first()
        return render_template('my_details_admin.html', details=details)
    else:
        return render_template('invalid_page.html')

# Details of user(employee)
@app.route('/detailsEmp')
@login_required
def details_of_employee():
    if current_user.designation=='emp':
        details = Register.query.filter_by(email=current_user.username).first()
        return render_template('my_details_emp.html', details=details)
    else:
        return render_template('invalid_page.html')

# Details of All Employees
@app.route('/employee', methods=['GET','POST'])
@login_required
def employee_master_screen():
    if current_user.designation=='admin':
        result = Register.query.all()

        if request.method == 'POST' :
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            email = request.form.get('email')
            # print(firstname,lastname,email)

            q = ["SELECT * FROM register "]
            vals = dict()
            if firstname:
                q+=["firstname = :firstname "]
                vals['firstname'] = firstname
            if lastname:
                q+=[" lastname = :lastname "]
                vals['lastname'] = lastname
            if email:
                q+=[" email = :email "]
                vals['email'] = email

            if len(q)>1:
                q[0]+="WHERE "
                q = q[0] + ' AND '.join(q[1:])
                q = text(q)
                result = db.session.execute(q, vals)
            else:
                q = text(q[0])
                result = db.session.execute(q)

        return render_template('employee_master_screen.html',details=result)
    else:
        return render_template('invalid_page.html')
    

# Logout 
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

import time
from flask import request, redirect, render_template, url_for
from . import auto_test
from public.jenkins import JenkinsServer


@auto_test.route('/')
def index():
    project_name = 'ddd'
    return render_template('auto_test.html', project_name=project_name)


@auto_test.route('/build', methods=['GET', 'POST'])
def build():

    if request.method == 'GET':
        return render_template('auto_test_build.html')
    else:
        project_name = request.form.get('singleSelect')
        account = request.form.get('account')
        password = request.form.get('password')
        print(project_name)
        print(account)
        print(password)

        jenkins = JenkinsServer("http://192.168.9.174:8080/", 'zhuwb', '111111')
        jenkins.start_build(project_name)
        # return redirect(url_for('auto_test.index'))
        return redirect(url_for('auto_test.index'))


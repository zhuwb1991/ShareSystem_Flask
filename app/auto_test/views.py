import time
from flask import request, redirect, render_template, url_for
from . import auto_test
from public.jenkins import JenkinsServer


jenkins = JenkinsServer("http://192.168.9.174:8080/", 'zhuwb', '111111')


@auto_test.route('/')
def index():
    jenkins_running_jobs = jenkins.get_running_jobs()
    return render_template('auto_test.html', running_jobs=jenkins_running_jobs)


@auto_test.route('/build', methods=['GET', 'POST'])
def build():

    if request.method == 'GET':
        return render_template('auto_test_build.html')
    else:
        project_name = request.form.get('singleSelect')
        account = request.form.get('account')
        password = request.form.get('password')

        jenkins.start_build(project_name)
        return redirect(url_for('auto_test.index'))


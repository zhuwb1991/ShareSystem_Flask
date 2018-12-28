import time
import os
from werkzeug.utils import secure_filename
from flask import request, redirect, render_template, url_for, jsonify
from . import auto_test
from public.jenkins import JenkinsServer
from config import UPLOAD_FOLDER


@auto_test.route('/')
def index():
    # jenkins_running_jobs = jenkins.get_running_jobs()
    jenkins_running_jobs = [{"Android_CC": 17}]
    return render_template('auto_test.html', running_jobs=jenkins_running_jobs)


@auto_test.route('/build', methods=['GET', 'POST'])
def build():

    if request.method == 'GET':
        return render_template('auto_test_build.html')
    else:
        project_name = request.form.get('singleSelect')
        account = request.form.get('account')
        password = request.form.get('password')

        # jenkins = JenkinsServer("http://192.168.24.13:8080/", 'zhuwb', '111111')
        # jenkins.start_build(project_name)
        return redirect(url_for('auto_test.index'))


@auto_test.route('/get_apps/<select_value>')
def get_apps(select_value):

    path = os.path.join(UPLOAD_FOLDER, select_value)
    print(path)
    app_list = os.listdir(path)
    app_list.sort(key=lambda fn: os.path.getmtime(path + "\\" + fn))

    return jsonify({'apps': app_list})


@auto_test.route('/upgrade', methods=['GET', 'POST'])
def upgrade():

    if request.method == 'GET':

        path = os.path.join(UPLOAD_FOLDER, 'CC_Android')
        app_list = os.listdir(path)
        app_list.sort(key=lambda fn: os.path.getmtime(path + "\\" + fn))

        return render_template('auto_test_upgrade.html', apps=app_list)
    else:
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        # return render_template('auto_test_upgrade.html')
        return jsonify({'code': 0, 'msg': '上传成功'})

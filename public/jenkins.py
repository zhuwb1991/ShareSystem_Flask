from jenkinsapi.jenkins import Jenkins


class JenkinsServer:

    def __init__(self, url, username, password):

        self.J = Jenkins(url, username=username, password=password)

    def get_job(self):
        pass

    def start_build(self, job_name):

        if job_name in self.J.keys():
            self.J.build_job(job_name)
            return True
        else:
            return False

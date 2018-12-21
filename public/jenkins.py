from jenkinsapi.jenkins import Jenkins


class JenkinsServer:

    def __init__(self, url, username, password):

        self.J = Jenkins(url, username=username, password=password)

    def start_build(self, job_name):

        if job_name in self.J.keys():
            self.J.build_job(job_name)
            return True
        else:
            return False

    def get_running_jobs(self):

        jobs = self.J.get_jobs()
        running = []

        for job, job_instance in jobs:
            if job_instance.is_running():
                n = self.J[job].get_next_build_number()
                job_info = {job: n-1}
                running.append(job_info)
        return running


if __name__ == '__main__':
    J = JenkinsServer("http://192.168.9.174:8080/", 'zhuwb', '111111')
    print(J.get_running_jobs())

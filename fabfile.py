from fabric.api import local, lcd

def prepare_deployment(branch_name):
    local('python3 manage.py test backandpain')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

def deploy():
    with lcd('/path/to/my/prod/area/'):
        local('git pull')
        local('python manage.py migrate backandpain')
        local('python manage.py test backandpain')

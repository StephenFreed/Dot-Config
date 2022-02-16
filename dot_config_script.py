#!/Users/stephenfreed/.config/Dot-Config-Script-Py/bin/python3

from git.repo import Repo  # type: ignore
import time
from datetime import datetime

# GitPython will add/commit/push if directory has changed
PATH_OF_GIT_REPO = r'/Users/stephenfreed/.config/.git'
dt = datetime.now().strftime('%d-%m-%y %H:%M:%S')
COMMIT_MESSAGE = 'script auto push '
repo = Repo(PATH_OF_GIT_REPO)


def git_push():
    try:
        repo.git.add(A=True)
        time.sleep(1)
        repo.index.commit(COMMIT_MESSAGE + dt)
        time.sleep(1)
        origin = repo.remote(name='origin')
        origin.push(refspec='{}:{}'.format('main', 'main'))
    except:  # noqa
        with open('/Users/stephenfreed/.config/script_log_file.txt', 'a') as my_file:
            my_file.write('ERROR While Pushing Code ' + dt + '\n')


if repo.is_dirty(untracked_files=True):
    git_push()

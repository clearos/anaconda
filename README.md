# anaconda

Forked version of anaconda with ClearOS changes applied

* git clone git+ssh://git@github.com/clearos/anaconda.git
* cd anaconda
* git checkout c7
* git remote add upstream git://git.centos.org/rpms/anaconda.git
* git pull upstream c7
* git checkout clear7
* git merge --no-commit c7
* git commit

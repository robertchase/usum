# use docker to run tests
#
# to override default tests, supply cmdline arguments, which will be passed to pytest
#
# to override default directories and names, set env variables:
#     TEST_GIT - location of git directory where usum is cloned ($HOME/git)
#     TEST_IMAGE - name of python docker image (bob/pythondev)
#
# assumes: 1. docker is running
#          2. a python image is available ($TEST_IMAGE below)
#             with pytest installed
#
TEST_GIT=${TEST_GIT:-$HOME/git}
TEST_IMAGE=${TEST_IMAGE:-bob/pythondev}

CMD=${*:-tests}
GIT=/opt/git

docker run --rm -v=$TEST_GIT:$GIT -w $GIT/usum -e PYTHONPATH=$GIT/usum $TEST_IMAGE pytest $CMD

from fabric.api import local, run, abort, lcd

def deploy():
    if local("nosetests sample/tests").failed:
        print "Tests failed!"
    else:
        run("touch /tmp/foo.bar")

def tests():
    if local("pwd").succeeded:
        with lcd("sample/tests"):
            if local("nosetests").succeeded:
                local("echo Success!")

    with lcd("sample/expected_failures"):
        if local("nosetests").succeeded:
            print "This won't be printed"

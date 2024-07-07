from invoke.tasks import task


@task
def service(c):
    """Run the Marine Animal Predictor Service"""
    c.run("docker compose up")


@task
def format(c):
    """Format code"""
    c.run("black .")
    c.run("isort .")


@task
def validate(c):
    """Perform code validations"""
    c.run("pylint oi")


@task
def tests(c):
    """Perform python tests"""
    c.run("pytest .")

from invoke.tasks import task


@task
def service(c):
    """Run the Marine Animal Predictor Service"""
    c.run("docker compose up")

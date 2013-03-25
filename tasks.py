from celery import task


@task
def reset_in_use(machine):
    print "resetting machine", machine
    if machine.state != 'u':
        return
    machine.state = 'f'
    machine.save()

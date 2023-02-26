import docker
import time


def check():
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    for event in client.events(decode=True):
        if event['Type'] == 'container':
            if event['status'] == 'health_status: unhealthy':
                print(event)
                print("The container is detected to be unhealthy, try to restart")
                container = client.containers.get(event['id'])
                container.restart()
            else:
                print("风平浪静")
    print("just in working")
    time.sleep(5)


if __name__ == '__main__':
    check()

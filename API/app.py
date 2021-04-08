import camera_api, movement_api
from settings import camera_port, movement_port, cameram_port

if __name__=='__main__':
    camera_api.app.run(port=camera_port)
    movement_api.app.run(port=movement_api)
    
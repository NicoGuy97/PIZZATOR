#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/nicolas/ws_servomotor/src/dynamixel_motor/dynamixel_driver"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/nicolas/ws_servomotor/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/nicolas/ws_servomotor/install/lib/python2.7/dist-packages:/home/nicolas/ws_servomotor/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/nicolas/ws_servomotor/build" \
    "/usr/bin/python2" \
    "/home/nicolas/ws_servomotor/src/dynamixel_motor/dynamixel_driver/setup.py" \
    build --build-base "/home/nicolas/ws_servomotor/build/dynamixel_motor/dynamixel_driver" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/nicolas/ws_servomotor/install" --install-scripts="/home/nicolas/ws_servomotor/install/bin"

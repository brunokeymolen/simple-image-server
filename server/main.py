"""Simple imager server"""
import csv
import os
from pyramid.renderers import render_to_response

PORT = 8999
USER = 'user'
PASSWD = 'password'

PUBLIC_DIR = None

def _disp_login(request, error='', del_cookies=[]):
    """Display login interface."""
    params = {}
    params['error'] = error
    response = render_to_response(
        'login.mak',
        params,
        request=request)
    if del_cookies:
        for c in del_cookies:
            response.delete_cookie(c)
    return response

def _disp_root(request):
    return _disp_images(request)


def _disp_dirs(request):
    directories = []

    # os.walk() generates a 3-tuple (dirpath, dirnames, filenames) for each directory
    for root, dirs, files in os.walk(PUBLIC_DIR+"/thumbs_positive"):

        # We are interested in the directories at the current level only
        full_dir = PUBLIC_DIR+"/thumbs_positive"
        directories = [os.path.join(root, d) for d in dirs]
        directories = [d.replace(full_dir, '').lstrip('/') for d in directories]
        break  # Stop recursion after the first level

    directories.sort(reverse=True)

    params = {}
    params['directories'] = directories
    response = render_to_response(
        'directories.mak',
        params,
        request=request)

    return response


def _disp_images_dir(request):
    subpath = request.matchdict.get('path', '')
    print("subpath",subpath)

    if (len(subpath) == 0):
        return _disp_dirs(request)

    image_paths = []
    for r, d, fs in os.walk(PUBLIC_DIR+"/thumbs_positive"+"/" + subpath):
        for f in fs:
            _p = os.path.join(r, f)
            _f = _p.replace(PUBLIC_DIR, '').lstrip('/')

            print("r", r, "f", f, "_p", _p, "_f", _f, "PUBLIC_DIR", PUBLIC_DIR)
            full = os.path.join('../images', _f.replace("thumbs_positive", "positive"))
            thumb = os.path.join('../images', _f)

            print("full", full, "thumb", thumb)
            #image_paths.append(os.path.join('images', _f))
            image_paths.append({'thumb': thumb, 'full': full})

    #image_paths = dict(sorted(image_paths.items(), key=lambda item: item[0], reverse=True))
    image_paths =  sorted(image_paths, key=lambda image: image['thumb'], reverse=True)

    #image_paths.sort(reverse=True)
    params = {}
    params['images'] = image_paths
    response = render_to_response(
        'images.mak',
        params,
        request=request)
    #response.set_cookie('sid', 'iv')
    return response



def _disp_images(request):
    """Display images."""
    params = request.POST
    is_login = True
    #if 'username' in params and 'userpass' in params:
    #    username = params['username']
    #    userpass = params['userpass']
    #    is_login = _can_login(username, userpass)
    #if 'sid' in request.cookies:
    #    sid = request.cookies['sid']
    #    is_login = _has_valid_cookie(sid)
    #if not is_login:
    #    return _disp_login(request, u'Failure in login!!!')
    image_paths = []
    for r, d, fs in os.walk(PUBLIC_DIR+"/thumbs_positive"):
        for f in fs:
            _p = os.path.join(r, f)
            _f = _p.replace(PUBLIC_DIR, '').lstrip('/')

            print("r", r, "f", f, "_p", _p, "_f", _f, "PUBLIC_DIR", PUBLIC_DIR)
            full = os.path.join('images', _f.replace("thumbs_positive", "positive"))
            thumb = os.path.join('images', _f)
            print("full", full, "thumb", thumb)
            #image_paths.append(os.path.join('images', _f))
            image_paths.append({'thumb': thumb, 'full': full})

    #image_paths = dict(sorted(image_paths.items(), key=lambda item: item[0], reverse=True))
    image_paths =  sorted(image_paths, key=lambda image: image['thumb'], reverse=True)

    #image_paths.sort(reverse=True)
    params = {}
    params['images'] = image_paths
    response = render_to_response(
        'images.mak',
        params,
        request=request)
    #response.set_cookie('sid', 'iv')
    return response


def _logout(request):
    """Delete cookie for logout."""
    return _disp_login(request, del_cookies=['sid'])


def _can_login(username, userpass):
    """Check user name and password."""
    return username == USER and userpass == PASSWD


def _has_valid_cookie(cookie):
    """Check cookie value."""
    return cookie == 'iv'


def _add_routes(config):
    """Add Root information."""
    config.add_route('login', '/login')
    config.add_view(_disp_login, route_name='login')
    config.add_route('root', '/')
    config.add_view(_disp_dirs, route_name='root')

    config.add_route('images', '/images')
    config.add_view(_disp_images, route_name='images')
    config.add_route('logout', '/logout')
    config.add_view(_logout, route_name='logout')
    config.add_static_view('static', 'static')
    config.add_static_view('images', PUBLIC_DIR)

    config.add_route('days', '/days')
    config.add_view(_disp_dirs, route_name='days')

    config.add_route('dir', '/dir/{path}')
    config.add_view(_disp_images_dir, route_name='dir')
    #, renderer='string')




def execute():
    """Execute this application."""
    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    config = Configurator()
    config.include('pyramid_mako')
    _add_routes(config)
    app = config.make_wsgi_app()
    print('Access to http://localhost:{}/login'.format(PORT))
    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description='Simple image viewer.')
    p_h = 'Public image directory. If you want to see sample, input `images/sample`'
    p.add_argument('public_dir', help=p_h)
    args = p.parse_args()
    PUBLIC_DIR = os.path.abspath(args.public_dir)
    if not os.path.isdir(PUBLIC_DIR):
        print('public_dir doesn\'t exist!')
        quit()

    here = os.path.dirname(__file__)
    settings = {
        'mako.directories': [
            os.path.abspath(os.path.join(here, 'templates')),
        ],
        }
    execute()

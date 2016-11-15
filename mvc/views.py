from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from mvc.models import User, Area
from utils.comm import md5_encode,get_ref_url
from django.shortcuts import render


# Create your views here.
def index(request):
    isLogin = is_login(request)
    if isLogin(request):
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/signup/')


def index_page(request):
    return None


def index_user_self(request):
    return None


def index_user(request):
    return None


def index_user_page(request):
    return None


def users_index(request):
    return None


# 是否登陆
def check_login(userName, password):
    state = {
        'success': True,
        'message': 'none',
        'userId': -1,
        'realName': '',
    }
    try:
        user = User.objects.get(userName=userName)
        if user.password == md5_encode(password):
            state['success'] = True
            state['userId'] = user.id
            state['realName'] = user.realName
        else:
            state['success'] = False
            state['message'] = _('PassWord incorrect')
    except User.DoesNotExist:
        state['success'] = False
        state['message'] = _('User does not exist.')
    return state


def do_login(request, userName, password):
    state = check_login(userName, password)
    if state['success']:
        request.session['isLogin'] = True
        request.session['userId'] = state['userId']
        request.session['userName'] = state['userName']
        request.session['realName'] = state['realName']
    return state


# 登陆
def result_message(request, title=_('Message'), message=_('Unknow error,processing'), go_back_url=''):
    isLogin = is_login(request)
    if go_back_url=='':
        go_back_url=get_ref_url(request)
    context={
        'page_title':title,
        'message':message,
        'go_back_url':go_back_url,
        'isLogin':isLogin
    }
    return render(request,'result_message.html',locals())

def sigNin(request):
    isLogin = is_login(request)
    if isLogin:
        return HttpResponseRedirect('/')
    try:
        userName = request.POST['userName']
        password = request.POST['password']
        is_post = True
    except Exception:
        is_post = False
    if is_post:
        state = do_login(request, userName, password)
        if state['success']:
            return result_message()
    context = {
        'page_title': _('SigNin'),
        'state': state,
    }
    return render(request, 'signup.html', locals())


def signOut(request):
    return None


# 是否登陆
def is_login(request):
    return request.session.get('isLogin', False)


# 检查用户名是否存在
def check_userName_exist(userName):
    if User.objects.filter(userName=userName) == None:
        return False
    else:
        return True


# 检查注册用户
def do_signup(request, userInfo):
    state = {
        'success': False,
        'message': '',
    }
    if userInfo['userName'] == '':
        state['success'] = False
        state['message'] = _('"userName" have not input.')
        return state
    if userInfo['password'] == '':
        state['success'] = False
        state['message'] = _('"PassWord" have not input.')
        return state
    if userInfo['email'] == '':
        state['success'] = False
        state['message'] = _('"Email" have not input.')
        return state
    if check_userName_exist(userInfo['userName']):
        state['success'] = False
        state['message'] = _('"userName" have existed.')
        return state
    if userInfo['password'] != userInfo['confirm']:
        state['success'] = False
        state['message'] = _('"Confirm PassWord" have not match.')
        return state
    user = User(
        userName=userInfo['userName'],
        realName=userInfo['realName'],
        password=userInfo['password'],
        email=userInfo['email'],
        area=Area.objects.get(id=1)
    )
    user.save()
    return state


# 注册页面
def signup(request):
    isLogin = is_login(request)
    if is_login:
        return HttpResponseRedirect('/')
    userInfo = {
        'userName': '',
        'password': '',
        'confirm': '',
        'realName': '',
        'email': '',
    }
    try:
        userInfo = {
            'userName': request.POST['userName'],
            'password': request.POST['password'],
            'confirm': request.POST['confirm'],
            'realName': request.POST['realName'],
            'email': request.POST['email'],
        }
        is_post = True
    except Exception:
        is_post = False
    if is_post:
        state = do_signup(request, userInfo)
    else:
        state = {
            'success': False,
            'message': _('Signup')
        }
    if state['success']:
        pass
    result = {
        'success': state['success'],
        'message': state['message'],
        'form': {
            'userName': userInfo['userName'],
            'realName': userInfo['realName'],
            'email': userInfo['email'],
        }
    }
    return render(request, 'signup.html', locals())


def settings(request):
    return None


def detail(request):
    return None


def detail_delete(request):
    return None


def friend_add(request):
    return None


def friend_remove(request):
    return None


def api_note_add(request):
    return None

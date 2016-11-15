import hashlib

def md5_encode(str):
    return hashlib.md5(str).hexdigest()

def get_ref_url(request):
    return  request.META.get('HTTP_REFERER','/')
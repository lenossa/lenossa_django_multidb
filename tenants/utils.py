def hostname_from_request(request):
    hostname = request.get_host().split(':')[0].lower()
    return hostname


def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()

    if tenants_map.get(hostname, False):
        return tenants_map.get(hostname)
    else:
        return False


def get_tenants_map():
    return {
        'joilton.localhost': 'joilton',
        'vand.localhost': 'vand'
    }
from textInfo.models import HeaderInfo, FooterInfo

def header_info(request):
    header_info = HeaderInfo.objects.first()
    return {'header_info': header_info}

def footer_info(request):
    footer_info = FooterInfo.objects.first()
    return {'footer_info': footer_info}

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def make_pagination_view(response, page):
    paginator = Paginator(response, 10)

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return response

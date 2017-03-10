class PagePaginator:

    def paginate(self, queryset, page_size, req):
        page_num = req.get_param_as_int('page') or 1
        limit, offset = (page_num - 1) * page_size, page_num * page_size
        return queryset[limit:offset]

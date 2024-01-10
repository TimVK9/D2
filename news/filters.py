from django_filters import (FilterSet,
                            ModelChoiceFilter,
                            DateFromToRangeFilter,
                            ChoiceFilter)

from .models import Post


class PostFilter(FilterSet):
    dateCreation = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = {'categoryType',
                  'title',
                  'author',
                  }





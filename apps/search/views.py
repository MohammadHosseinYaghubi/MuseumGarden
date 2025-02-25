from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Q
from apps.memories.models import Memory
from apps.workshops.models import Workshop

#------------------------------------------------------------------------------------
class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        memories = Memory.objects.filter(
            Q(memory_title__icontains=query)
            # | Q(memory_text__icontains=query)
        )
        workshops = Workshop.objects.filter(
            Q(title__icontains=query)
        )
        context = {
            "memories":memories,
            "workshops":workshops
        }
        return render(request, 'search_app/search_results.html', context)
    
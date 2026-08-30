from django.http import JsonResponse
from django.shortcuts import render

SECTIONS = [
    "Aim", "Learning Objectives", "Overview", "Recap", "Pretest",
    "Git Branching", "Interactive Demo", "Merging", "Merge Practice",
    "Conflict Resolution", "Hands-on Lab", "Procedure", "Command Lab",
    "Quiz", "Exercise", "Further Readings",
]

def experiment(request):
    return render(request, "index.html", {"experiment_title": "Git Branching, Merging and Conflict Resolution"})

def experiment_api(request):
    return JsonResponse({
        "title": "Git Branching, Merging and Conflict Resolution",
        "delivery": "Django + client-side interactive laboratory",
        "section_count": len(SECTIONS),
        "sections": SECTIONS,
        "features": ["branch simulator", "merge simulator", "conflict editor", "guided command lab", "graded quiz"],
    })

def health(request):
    return JsonResponse({"status": "ok", "framework": "Django"})

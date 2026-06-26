from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import TaskSerializer
from groups.models import Group


# =========================
# TASK LIST + CREATE
# =========================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tasks(request):

    # =========================
    # GET TASKS (ROLE BASED)
    # =========================
    if request.method == 'GET':

        user = request.user

        # Lecturer / Rep → see everything
        if user.role in ['lecturer', 'rep']:
            tasks = Task.objects.all()

        # Leader → only tasks in groups they lead
        elif user.role == 'leader':
            tasks = Task.objects.filter(group__leader=user)

        # Student → only tasks assigned to them
        else:
            tasks = Task.objects.filter(assigned_to=user)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


    # =========================
    # CREATE TASK (LEADER ONLY + GROUP RULES)
    # =========================
    if request.method == 'POST':

        if request.user.role != 'leader':
            return Response(
                {"error": "Only group leaders can create tasks"},
                status=403
            )

        group_id = request.data.get('group')
        assigned_to_id = request.data.get('assigned_to')

        group = get_object_or_404(Group, id=group_id)

        # -------------------------
        # RULE 1: Leader must own group
        # -------------------------
        if group.leader != request.user:
            return Response(
                {"error": "You can only create tasks for your own group"},
                status=403
            )

        # -------------------------
        # RULE 2: Assigned user must be group member
        # -------------------------
        if assigned_to_id:
         if not group.members.filter(id=assigned_to_id).exists():
            return Response(
                {"error": "User must be a member of the group"},
                status=400
            )

        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# =========================
# TASK DETAIL (UPDATE ONLY WITH RULES)
# =========================

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):

    task = get_object_or_404(Task, pk=pk)
    user = request.user

    # =========================
    # STUDENT RULE
    # =========================
    if user.role == 'student':

        if task.assigned_to != user:
            return Response(
                {"error": "You can only update your own tasks"},
                status=403
            )

    # =========================
    # LEADER RULE
    # =========================
    if user.role == 'leader':

        if task.group.leader != user:
            return Response(
                {"error": "You can only update tasks in your group"},
                status=403
            )

    serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)
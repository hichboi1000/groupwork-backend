from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Unit, Assignment, GroupAssignment, Submission
from .serializers import (
    UnitSerializer,
    AssignmentSerializer,
    GroupAssignmentSerializer,
    SubmissionSerializer
)


# =========================
# UNIT VIEWS
# =========================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def units(request):

    if request.method == 'GET':
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UnitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# =========================
# ASSIGNMENT VIEWS
# =========================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def assignments(request):

    if request.method == 'GET':
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# =========================
# GROUP ASSIGNMENT TRACKING
# =========================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def group_assignments(request):

    data = GroupAssignment.objects.all()
    serializer = GroupAssignmentSerializer(data, many=True)
    return Response(serializer.data)


# =========================
# SUBMISSIONS
# =========================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def submissions(request):

    if request.method == 'GET':
        data = Submission.objects.all()
        serializer = SubmissionSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(submitted_by=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
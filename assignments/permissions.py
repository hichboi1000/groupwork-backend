from rest_framework.permissions import BasePermission


# =========================
# LECTURER ONLY
# =========================
class IsLecturer(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'lecturer'
        )


# =========================
# GROUP LEADER ONLY
# =========================
class IsLeader(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'leader'
        )


# =========================
# CLASS REP ONLY
# =========================
class IsRep(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'rep'
        )


# =========================
# STUDENT ONLY
# =========================
class IsStudent(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'student'
        )
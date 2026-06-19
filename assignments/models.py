from django.db import models
from django.conf import settings


# 1. UNIT (created dynamically by lecturers or reps)
class Unit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=20, unique=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_units'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 2. ASSIGNMENT (belongs to a unit)
class Assignment(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name='assignments'
    )

    deadline = models.DateTimeField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_assignments'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 3. GROUP ↔ ASSIGNMENT LINK (tracks progress per group)
class GroupAssignment(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
    ]

    group = models.ForeignKey(
        'groups.Group',
        on_delete=models.CASCADE,
        related_name='group_assignments'
    )

    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name='group_assignments'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    submitted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.group.name} - {self.assignment.title}"


# 4. SUBMISSION (final work submitted by group leader)
class Submission(models.Model):

    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    group = models.ForeignKey(
        'groups.Group',
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    content = models.TextField(blank=True, null=True)

    file = models.FileField(
        upload_to='submissions/',
        blank=True,
        null=True
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group.name} - {self.assignment.title}"
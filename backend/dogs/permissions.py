from rest_framework import permissions


class CanDeleteUpdateDog(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.role != "CIVILIAN":
            return False
        
        return obj.reports.filter(reported_by = request.user).exists()
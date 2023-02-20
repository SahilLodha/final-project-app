from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.shortcuts import redirect


class CustomerMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_customer:
                return self.handle_no_permission()
        else:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class VendorMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_vendor:
                return self.handle_no_permission()
        else:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


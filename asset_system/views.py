from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from accounts.views import check_role_pastorate, check_role_mis
from .models import Asset, Location, MaintenanceRecord, Department
from .forms import AssetForm, LocationForm, MaintenanceRecordForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'assets/asset_list.html', {'assets': assets})


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def asset_detail(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    return render(request, 'assets/asset_detail.html', {'asset': asset})


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def asset_create(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save()
            return redirect('asset_detail', pk=asset.pk)
    else:
        form = AssetForm()
    return render(request, 'assets/asset_form.html', {'form': form})



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def asset_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            asset = form.save()
            return redirect('asset_detail', pk=asset.pk)
    else:
        form = AssetForm(instance=asset)
    return render(request, 'assets/asset_form.html', {'form': form})




@login_required(login_url='login')
@user_passes_test(check_role_mis)
def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    asset.delete()
    return redirect('asset_list')






from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, AssetCategory
from .forms import DepartmentForm, AssetCategoryForm

# Department Views
@login_required(login_url='login')
@user_passes_test(check_role_mis)
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'assets/department_list.html', {'departments': departments})


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'assets/department_detail.html', {'department': department})



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'assets/department_form.html', {'form': form})



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'assets/department_form.html', {'form': form})



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect('department_list')

# Category Views


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def category_list(request):
    categories = AssetCategory.objects.all()
    return render(request, 'assets/category_list.html', {'categories': categories})




@login_required(login_url='login')
@user_passes_test(check_role_mis)
def category_detail(request, pk):
    category = get_object_or_404(AssetCategory, pk=pk)
    return render(request, 'assets/category_detail.html', {'category': category})



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def category_create(request):
    if request.method == "POST":
        form = AssetCategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = AssetCategoryForm()
    return render(request, 'assets/category_form.html', {'form': form})




@login_required(login_url='login')
@user_passes_test(check_role_mis)
def category_edit(request, pk):
    category = get_object_or_404(AssetCategory, pk=pk)
    if request.method == "POST":
        form = AssetCategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = AssetCategoryForm(instance=category)
    return render(request, 'assets/category_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def category_delete(request, pk):
    category = get_object_or_404(AssetCategory, pk=pk)
    category.delete()
    return redirect('category_list')







# Location Views
@login_required(login_url='login')
@user_passes_test(check_role_mis)
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'assets/location_list.html', {'locations': locations})



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'assets/location_detail.html', {'location': location})




@login_required(login_url='login')
@user_passes_test(check_role_mis)
def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'assets/location_form.html', {'form': form})





@login_required(login_url='login')
@user_passes_test(check_role_mis)
def location_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'assets/location_form.html', {'form': form})



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    location.delete()
    return redirect('location_list')


from django.shortcuts import render, redirect
from .forms import MaintenanceRecordForm



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def maintenance_record_create(request):
    if request.method == 'POST':
        form = MaintenanceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_record_list')  # Replace with your URL name for list view
    else:
        form = MaintenanceRecordForm()
    
    return render(request, 'assets/maintenance_record_create.html', {'form': form})




from django.shortcuts import render
from .models import MaintenanceRecord


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def maintenance_record_list(request):
    maintenance_records = MaintenanceRecord.objects.all()
    context = {
        'maintenance_records': maintenance_records
    }
    return render(request, 'assets/maintenance/maintenance_record_list.html', context)





from django.shortcuts import get_object_or_404, render
from .models import MaintenanceRecord



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def maintenance_record_detail(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    return render(request, 'assets/maintenance_record_detail.html', {'record': record})



from django.shortcuts import get_object_or_404, redirect, render
from .models import MaintenanceRecord
from .forms import MaintenanceRecordForm



@login_required(login_url='login')
@user_passes_test(check_role_mis)
def maintenance_record_edit(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == 'POST':
        form = MaintenanceRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('maintenance_record_detail', pk=pk)
    else:
        form = MaintenanceRecordForm(instance=record)
    return render(request, 'assets/maintenance_record_edit.html', {'form': form})






from django.shortcuts import get_object_or_404, redirect
from .models import MaintenanceRecord


@login_required(login_url='login')
@user_passes_test(check_role_mis)
def maintenance_record_delete(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('some_redirect_url_after_delete')  # Redirect to appropriate URL after deletion
    return render(request, 'assets/maintenance_record_confirm_delete.html', {'record': record})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import FitnessClass
from .forms import FitnessClassForm
from django.utils.timezone import now

@login_required
def class_schedule(request):
    # Get all classes from the database
    classes = FitnessClass.objects.all()

    # Prepare a list of tuples (day, classes) where each day has its respective classes
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    class_by_day = [(day, classes.filter(day=day)) for day in days]

    return render(request, 'fitness_class/schedule.html', {
        'class_by_day': class_by_day
    })


def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def add_class(request):
    if request.method == "POST":
        name = request.POST.get("name")
        day = request.POST.get("day")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        if name and day and start_time and end_time:
            # Create and save the new class
            FitnessClass.objects.create(
                name=name,
                day=day,
                start_time=start_time,
                end_time=end_time
            )
            # Redirect to the class schedule after saving
            return redirect("class_schedule")

    return render(request, "fitness_class/add_class.html")


@login_required
@user_passes_test(is_admin)
def edit_class(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    if request.method == 'POST':
        form = FitnessClassForm(request.POST, instance=fitness_class)
        if form.is_valid():
            form.save()
            return redirect('class_schedule')
    else:
        form = FitnessClassForm(instance=fitness_class)
    return render(request, 'fitness_class/edit_class.html', {'form': form, 'fitness_class': fitness_class})


@login_required
@user_passes_test(is_admin)
def delete_class(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    if request.method == 'POST':
        fitness_class.delete()
        return redirect('class_schedule')
    return render(request, 'fitness_class/delete_class.html', {'fitness_class': fitness_class})

from django.core.cache import cache
from .models import Form1_assement,StaffProfile
from django.db.models import Avg
from django.db.models import Count, Q


CACHE_TTL = 10  # seconds


def get_dashboard_status(employee):  # set incharge html page into cache
    cache_key = f"dashboard_status:{employee.id}"   # cache key 
    status = cache.get(cache_key)    # get the saved cache


    if status:
        return cache.get(cache_key)   # check cache is exist
    

    # Aggregate counts in one query
    stats = Form1_assement.objects.filter(evaluator_name=employee).aggregate(
        total_forms=Count('id'),
        pending_forms=Count('id', filter=Q(is_approved=False)),
        approved_forms=Count('id', filter=Q(is_approved=True)),
    )

    
    total_forms = stats['total_forms']
    pending_forms = stats['pending_forms']
    approved_forms = stats['approved_forms']

    # total_staffs = StaffProfile.objects.filter(location__incharge=employee).count()
    if total_forms > 0:
        average_score = round((approved_forms / total_forms) * 100, 2)
    else:
        average_score = 0

    status = {
        "total_forms":total_forms,
        "pending_forms":pending_forms,
        "approved_forms":approved_forms,
        "average_score":average_score,
        # "total_staffs":total_staffs,
    }  # collect data from db

    cache.set(cache_key,status,CACHE_TTL) # create the cache
    return status




def get_dashboard_stats_all():
    cache_key = "dashboard_stats:all"
    stats = cache.get(cache_key)
    if stats:
        return stats

    total_forms = Form1_assement.objects.count()
    pending_forms = Form1_assement.objects.filter(is_approved=False).count()
    approved_forms = Form1_assement.objects.filter(is_approved=True).count()
    average_score = Form1_assement.objects.aggregate_avg("score") or 0

    stats = {
        "total_forms": total_forms,
        "pending_forms": pending_forms,
        "approved_forms": approved_forms,
        "average_score": average_score,
    }
    cache.set(cache_key, stats, CACHE_TTL)
    return stats
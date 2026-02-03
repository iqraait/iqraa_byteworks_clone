ROLE_REDIRECTS = {
    "is_superint": ("nursing_department", "nursing_admin_dashboard"),
    "is_incharge": ("nursing_department", "InchargeDashboard"),
    "is_staff_nurse": ("nursing_department", "my_forms"),

}

ROLE_PRIORITY = ["is_incharge","is_superint","is_staff_nurse"]




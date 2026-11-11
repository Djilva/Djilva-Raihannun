from admin import Admin

# Membuat instance Admin dari modul admin
super_admin = Admin("Kang", "Haerin", 20, "Surabaya")

# Menjalankan method untuk membuktikan semuanya bekerja
super_admin.describe_user()
print()
super_admin.privileges.show_privileges()
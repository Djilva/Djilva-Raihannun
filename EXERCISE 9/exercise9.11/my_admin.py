from user_admin import Admin

# Membuat instance Admin
admin_user = Admin("Pham", "Hanni", 22, "Yogyakarta")

# Memanggil method describe_user dan show_privileges
admin_user.describe_user()
print()
admin_user.privileges.show_privileges()
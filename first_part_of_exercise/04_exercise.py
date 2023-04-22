
first_unit_name = "футов"
length_name = float(input("Введите длину вашего участка : "))
print("Длина участка составляет : ", length_name, first_unit_name)

width_name = float(input("Введите ширину вашего участка : "))
print("Ширина участка составляет :", width_name, first_unit_name)

second_unit_name = "акров"
area_name = (length_name * width_name) / 43560

print("Площадь вашего участка составялет : ", round(area_name, 2), second_unit_name)
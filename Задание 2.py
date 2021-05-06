# Заданное число секунд
the_specified_number_of_seconds = int(input('Введите время в секундах '))

# Число секунд в минуте
number_of_seconds_in_a_minute = 60
# Число минут в часе
number_of_minutes_in_a_hour = 60

# Число секунд в часе       = Число секунд в минуте         * число минут в часе
number_of_seconds_in_a_hour = number_of_seconds_in_a_minute * number_of_minutes_in_a_hour

# Время в часах(//) =  Заданное число секунд        # Число секунд в часе
time_in_hours = (the_specified_number_of_seconds // number_of_seconds_in_a_hour)
# Остаточное время в секундах (%)
remaining_time_in_seconds = the_specified_number_of_seconds % number_of_seconds_in_a_hour

# Если остаточное время в секундах больше или равно числу секунд в минуте, то:
if remaining_time_in_seconds >= number_of_seconds_in_a_minute:
    # Время в минутах равно остаточному времени в секундах нацело делим на число секунд в минуте
    time_in_minutes = remaining_time_in_seconds // number_of_seconds_in_a_minute
    # Время в секундах равно остатку при делении остаточного времени в секундах на число секунд в минуте
    time_in_seconds = remaining_time_in_seconds % number_of_seconds_in_a_minute
else:  # Иначе:
    # В ремя в секундах равно остаточному времени в секундах
    time_in_seconds = remaining_time_in_seconds
    # Время в минутах равно нулю (0)
    time_in_minutes = 0

print(str(time_in_hours), ':', str(time_in_minutes), ':', str(time_in_seconds))

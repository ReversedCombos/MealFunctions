def meal_tip_function(meal_tip_percentage):
    meal_tip_total = (meal_Total / 100) * meal_tip_percentage
    return(meal_tip_total)
def meal_people_function(meal_num_people):
    meal_tip_total = meal_tip_function()
    meal_unit_total = (meal_Total + meal_tip_total) / meal_num_people
    return(meal_unit_total)
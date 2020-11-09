class DataStore:
    def __init__(self):
        pass

    def bmi_calc(self, height, weight):
        bmi = round((weight / ((height / 100) * (height / 100))), 1)
        return bmi

    def bmr_calc(self,gender, height, weight, age, activity):
        if gender == 'male':
            start_value = 66
            weight_modifier = 13.7
            height_modifier = 5
            age_modifier = 6.8
        else:
            start_value = 655
            weight_modifier = 9.6
            height_modifier = 1.8
            age_modifier = 4.7
        if activity == 'sedentary':
            activity_modifier = 1.2
        elif activity == 'lightly':
            activity_modifier = 1.375
        elif activity == 'moderately':
            activity_modifier = 1.5
        elif activity == 'very':
            activity_modifier = 1.725
        else:
            activity_modifier = 1.9

        bmr = int((start_value +
                   (weight_modifier * weight) +
                   (height_modifier * height) +
                   (age_modifier * age) *
                   activity_modifier))
        return bmr
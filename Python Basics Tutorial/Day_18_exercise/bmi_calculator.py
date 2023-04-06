'''
Author: Piyush More
Description: BMI Calculator.
'''

# Taking inputs from the user.
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

# Calculating BMI of user and 
bmi = round(weight/(height**2), 2)

# Displaying BMI and health condition to user.
if bmi < 18.5:
    print("Your BMI Index is {} and this is considered as Under weight.".format(bmi))
elif bmi >= 18.5 and bmi < 24.9:
    print("Your BMI Index is {} and this is considered as Normal weight.".format(bmi))
elif bmi >= 25.0 and bmi < 29.9:
    print("Your BMI Index is {} and this is considered as Over weight.".format(bmi))
else:
    print("Your BMI Index is {} and this is considered as Obese.".format(bmi))

# Asking users for suggestions of Diet with respect to their BMI and Health Status.
food_suggestion = input("We would like to get some suggestions for your diet, just type 'yes' if needed or 'q' to skip: ")

# Display suggestions of diet.
if food_suggestion.lower() == 'yes':
    if bmi < 18.5:
        print('''Some common daily food items you can consume in order to get back into Normal weight are following:
            1. Whole milk: High in calories and healthy fats, whole milk is an excellent choice for underweight individuals looking to gain weight.

            2. Avocado: Avocados are packed with healthy fats and calories, making them a great addition to smoothies, salads, or as a spread on toast.

            3. Nuts and seeds: Almonds, walnuts, chia seeds, and flaxseeds are all great sources of healthy fats, protein, and fiber. They can be added to smoothies, oatmeal, or eaten as a snack.
            
            4.Dried fruits: Dates, raisins, and prunes are high in calories and nutrients, making them a healthy addition to breakfast, snacks, or desserts.
            ''')
    elif bmi >= 18.5 and bmi < 24.9:
        print('''Some common daily food items you can consume in order to get back into Normal weight are following:
                1. Fruits and vegetables: Eating a variety of fresh fruits and vegetables can help you maintain a healthy weight and provide essential vitamins, minerals, and fiber.
                Choose colorful fruits and vegetables like spinach, kale, berries, and citrus fruits.

                2. Whole grains: Whole grains like brown rice, quinoa, and whole-wheat bread are a good source of fiber and help maintain a healthy weight.

                3. Legumes: Lentils, chickpeas, and black beans are high in protein and fiber, making them a great choice for meals and snacks.

                4. Nuts and seeds: Almonds, walnuts, chia seeds, and flaxseeds are all great sources of healthy fats, protein, and fiber. They can be added to smoothies, oatmeal, or eaten as a snack.

                5. Low-fat dairy: Low-fat milk, yogurt, and cheese are a good source of calcium and protein. They can be included in breakfast or as a snack.

                6. Lean protein: Choose lean sources of protein like chicken, fish, and tofu. Avoid fried and processed meats.

                7. Herbs and spices: Turmeric, ginger, garlic, and cinnamon have anti-inflammatory properties and can be added to meals for flavor and health benefits.''')
    elif bmi >= 25.0 and bmi < 29.9:
        print('''Some common daily food items you can consume in order to get back into Normal weight are following:
                1. Fruits and vegetables: Eating a variety of fresh fruits and vegetables can help you feel full and satisfied while providing essential vitamins, minerals, and fiber. Choose colorful fruits and vegetables like spinach, kale, berries, and citrus fruits.

                2. Whole grains: Swap refined grains for whole grains like brown rice, quinoa, and whole-wheat bread to increase fiber intake and promote feelings of fullness.

                3. Legumes: Lentils, chickpeas, and black beans are high in protein and fiber, making them a great choice for meals and snacks.

                4. Lean protein: Choose lean sources of protein like chicken, fish, and tofu. Avoid fried and processed meats.
        ''')
    elif bmi >= 30.0:
        print('''Some common daily food items you can consume in order to get back into Normal weight are following:
                1. Fruits and vegetables: Eating a variety of fresh fruits and vegetables can help you feel full and satisfied while providing essential vitamins, minerals, and fiber. Choose colorful fruits and vegetables like spinach, kale, berries, and citrus fruits.

                2. Whole grains: Swap refined grains for whole grains like brown rice, quinoa, and whole-wheat bread to increase fiber intake and promote feelings of fullness.

                3. Legumes: Lentils, chickpeas, and black beans are high in protein and fiber, making them a great choice for meals and snacks.

                4. Lean protein: Choose lean sources of protein like chicken, fish, and tofu. Avoid fried and processed meats.
        ''')
else:
    print("Thanks have a great day. Enjoy your food.")

# Asking user whether he wants to get suggetsions on Body exercises.
exercise_suggestion = input("We would also like give some suggestions on exercises for your health, just type 'yes' if needed or 'q' to skip: ")

# Displaying list of suggestions of body exercises.
if exercise_suggestion.lower() == 'yes':
    if bmi < 18.5:
        print('''1. Exercises for underweight individuals:
                 a. Strength training exercises like push-ups, squats, and lunges can help to build muscle mass and increase body weight.
                 b. Cardiovascular exercises like jogging, cycling, or swimming can help to improve endurance and increase calorie intake.''')
    elif bmi >= 18.5 and bmi < 24.9:
        print('''2. Exercises for normal weight individuals:
                 a. Walking: Walking is a simple yet effective form of exercise that can be done anywhere, anytime. It helps to maintain cardiovascular health, improves mood, and reduces stress levels.

                 b. Jogging/Running: If you are looking for a more intense workout, jogging or running can be a great option. This exercise can help to burn calories, improve endurance and strengthen the legs.

                 c. Cycling: Cycling is a low-impact exercise that can help to improve cardiovascular fitness, burn calories, and strengthen the legs. You can use a stationary bike or go for a ride outdoors.

                 d. Jumping jacks: Jumping jacks are a simple and effective exercise that can be done anywhere. They can help to improve cardiovascular fitness, coordination, and burn calories.

                 e. Squats: Squats are a great exercise to strengthen the legs and glutes. They can be done without any equipment and can be modified for different fitness levels.

                 f. Lunges: Lunges are another exercise that can help to strengthen the legs and glutes. They can be done without any equipment and can be modified for different fitness levels.

                 g. Push-ups: Push-ups are a great exercise to strengthen the chest, arms, and shoulders. They can be done without any equipment and can be modified for different fitness levels.

                 h. Plank: Plank is a core strengthening exercise that can be done without any equipment. It can help to improve posture, strengthen the core, and reduce the risk of back pain.''')
    elif bmi >= 25.0 and bmi < 29.9:
        print('''2. Exercises for overweight individuals:
                 a. Brisk walking is a low-impact exercise that can help to improve cardiovascular health and burn calories.
                 b. High-intensity interval training (HIIT) is a series of short, intense exercises that can help to burn fat and improve cardiovascular health.
                 c. Dancing is a fun way to burn calories and improve overall fitness.''')
    else:
        print('''3. Exercises for obese individuals:
                 a. Low-impact exercises like water aerobics, walking, or cycling can help to reduce the risk of injury and improve cardiovascular health.
                 b. Chair exercises like seated leg lifts, arm circles, and seated marches can help to improve strength and flexibility.
                 c. Yoga can help to improve flexibility, balance, and overall fitness.''')
else:
    print("Enjoy your day.")

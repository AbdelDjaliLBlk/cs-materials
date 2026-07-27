import 'package:flutter/material.dart';
import 'package:flutter_application_1/models/meal.dart';
import 'package:flutter_application_1/models/meals_of_a_day.dart';
import 'package:flutter_application_1/screens/signup_screen.dart';
import 'screens/login_screen.dart';
import 'screens/meals_of_a_day_screen.dart';
import 'screens/home_screen.dart';
import 'screens/add_new_meal_screen.dart';
import 'screens/ingredients_of_a_meal_screen.dart';
import 'package:hive/hive.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized(); 
  await Hive.initFlutter();
  Hive.registerAdapter(MealAdapter()); 
  Hive.registerAdapter(MealsOfADayAdapter()); 
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My Meal Planner',
      theme: ThemeData(
        appBarTheme: const AppBarTheme(
          backgroundColor: Color.fromARGB(255, 0, 0, 0),
          titleTextStyle: TextStyle(
            color: Color.fromARGB(255, 255, 153, 0),
            fontSize: 18,
            fontWeight: FontWeight.bold,
          ),
          iconTheme: IconThemeData(
            color: Color.fromARGB(255, 255, 153, 0),
          ),
        ),
      ),
      home: HomeScreen(),
      routes: {
      '/login': (context) => LoginScreen(),
      '/signup': (context) => SignupScreen(),
      '/home': (context) => HomeScreen(),

      '/mealsOfADay': (context) {
        return MealsOfADayScreen(day: 'Wednesday');
      },
      '/addMeal': (context) => AddNewMealScreen(),
      '/ingredients': (context) {
        final mealName = ModalRoute.of(context)!.settings.arguments as String;
        return IngredientsOfAMealScreen(mealName: mealName);
      },
    },
    debugShowCheckedModeBanner: false, 
    );
  }
}

import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:flutter_application_1/models/meals_of_a_day.dart';
import 'package:flutter_application_1/models/meal.dart';
import '../components/week_days_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late Box<MealsOfADay> dayMealsBox;
  bool _isLoading = true;

  final List<MealsOfADay> weekDaysList = [
    MealsOfADay(
      day: "Monday",
      listOfMealsOfDay: [
        Meal(
          name: "Pizza",
          imgPath: "assets/images/pizza.jpg",
          listOfIngredient: ["Cheese", "Tomato", "Olive"],
        ),
        Meal(
          name: "Tagine",
          imgPath: "assets/images/tagine.jpg",
          listOfIngredient: ["Meat", "Potatoes", "Spices"],
        ),
      ],
    ),
    MealsOfADay(
      day: "Tuesday",
      listOfMealsOfDay: [
        Meal(
          name: "Burger",
          imgPath: "assets/images/burger.jpg",
          listOfIngredient: ["Meat", "Cheese", "Bread"],
        ),
      ],
    ),
    MealsOfADay(
      day: "Friday",
      listOfMealsOfDay: [
        Meal(
          name: "Couscous",
          imgPath: "assets/images/couscous.jpg",
          listOfIngredient: ["Semolina", "Vegetables", "Meat"],
        ),
      ],
    ),
  ];

  @override
  void initState() {
    super.initState();
    _initializeHive();
  }

  Future<void> _initializeHive() async {
    dayMealsBox = await Hive.openBox<MealsOfADay>('MealsBDD');

    if (dayMealsBox.isEmpty) {
      for (var e in weekDaysList) {
        await dayMealsBox.put(e.day, e);
      }
    }

    setState(() {
      _isLoading = false; // Hive ready, rebuild UI
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: const Text('Home Page'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.exit_to_app),
            onPressed: () {
              Navigator.pushNamedAndRemoveUntil(
                context,
                '/login',
                (route) => false,
              );
            },
          ),
        ],
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(12),
        itemCount: dayMealsBox.length,
        itemBuilder: (context, index) {
          final dayData = dayMealsBox.getAt(index)!;
          return WeekDaysCard(dayAndItsMealsList: dayData);
        },
      ),
    );
  }
}

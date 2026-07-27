import 'package:flutter/material.dart';
import '../components/meal_card.dart';

class MealsOfADayScreen extends StatefulWidget {
  final String day;
  const MealsOfADayScreen({required this.day, super.key});

  @override
  _MealsOfADayScreenState createState() => _MealsOfADayScreenState();
}

class _MealsOfADayScreenState extends State<MealsOfADayScreen> {
  List<Map<String, String>> meals = [
    {"name": "Pizza", "image": "assets/images/pizza.jpg"},
    {"name": "Tagine", "image": "assets/images/tagine.jpg"},
    {"name": "Couscous", "image": "assets/images/couscous.jpg"},
    {"name": "Burger", "image": "assets/images/burger.jpg"},
    
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Meals for ${widget.day}"),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () {},
          ),
        IconButton(
          icon: const Icon(Icons.exit_to_app),
          onPressed: () {
            Navigator.pushNamedAndRemoveUntil(
              context,
              '/login',
              (route) => false,
            );
          },
        )
        ],
      ),
      body: ListView.builder(
        itemCount: meals.length,
        itemBuilder: (ctx, index) {
          final m = meals[index];
          return MealCard(
            mealName: m["name"]!,
            imagePath: m["image"]!,
            parentContext: context,              
            onDelete: (){},
          );
        },
      ),
    );
  }
}
